[ Mathematics in Lean ](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/index.html)
  * [1. Introduction](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C01_Introduction.html)
  * [2. Basics](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C02_Basics.html)
  * [3. Logic](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C03_Logic.html)
  * [4. Sets and Functions](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C04_Sets_and_Functions.html)
  * [5. Elementary Number Theory](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C05_Elementary_Number_Theory.html)
  * [6. Discrete Mathematics](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C06_Discrete_Mathematics.html)
  * [7. Structures](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html)
  * [8. Hierarchies](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C08_Hierarchies.html)
  * [9. Groups and Rings](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html)
  * [10. Linear algebra](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C10_Linear_Algebra.html)
  * [](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html)
    * [11.1. Filters](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#filters)
    * [](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#metric-spaces)
      * [11.2.1. Convergence and continuity](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#convergence-and-continuity)
      * [11.2.2. Balls, open sets and closed sets](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#balls-open-sets-and-closed-sets)
      * [11.2.3. Compactness](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#compactness)
      * [11.2.4. Uniformly continuous functions](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#uniformly-continuous-functions)
      * [11.2.5. Completeness](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#completeness)
    * [](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#topological-spaces)
      * [11.3.1. Fundamentals](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#fundamentals)
      * [11.3.2. Separation and countability](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#separation-and-countability)
      * [11.3.3. Compactness](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#id5)
  * [12. Differential Calculus](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C12_Differential_Calculus.html)
  * [13. Integration and Measure Theory](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C13_Integration_and_Measure_Theory.html)


  * [Index](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/genindex.html)


[Mathematics in Lean](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/index.html)
  * [](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/index.html)
  * 11. Topology
  * [ View page source](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/_sources/C11_Topology.rst.txt)


* * *
#  11. Topology[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#index-0 "Link to this heading")
Calculus is based on the concept of a function, which is used to model quantities that depend on one another. For example, it is common to study quantities that change over time. The notion of a _limit_ is also fundamental. We may say that the limit of a function f(x) is a value b as x approaches a value a, or that f(x) _converges to_ b as x approaches a. Equivalently, we may say that f(x) approaches b as x approaches a value a, or that it _tends to_ b as x tends to a. We have already begun to consider such notions in [Section 3.6](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C03_Logic.html#sequences-and-convergence).
_Topology_ is the abstract study of limits and continuity. Having covered the essentials of formalization in Chapters [2](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C02_Basics.html#basics) to [7](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#structures), in this chapter, we will explain how topological notions are formalized in Mathlib. Not only do topological abstractions apply in much greater generality, but they also, somewhat paradoxically, make it easier to reason about limits and continuity in concrete instances.
Topological notions build on quite a few layers of mathematical structure. The first layer is naive set theory, as described in [Chapter 4](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C04_Sets_and_Functions.html#sets-and-functions). The next layer is the theory of _filters_ , which we will describe in [Section 11.1](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#filters). On top of that, we layer the theories of _topological spaces_ , _metric spaces_ , and a slightly more exotic intermediate notion called a _uniform space_.
Whereas previous chapters relied on mathematical notions that were likely familiar to you, the notion of a filter is less well known, even to many working mathematicians. The notion is essential, however, for formalizing mathematics effectively. Let us explain why. Let `f : ℝ → ℝ` be any function. We can consider the limit of `f x` as `x` approaches some value `x₀`, but we can also consider the limit of `f x` as `x` approaches infinity or negative infinity. We can moreover consider the limit of `f x` as `x` approaches `x₀` from the right, conventionally written `x₀⁺`, or from the left, written `x₀⁻`. There are variations where `x` approaches `x₀` or `x₀⁺` or `x₀⁻` but is not allowed to take on the value `x₀` itself. This results in at least eight ways that `x` can approach something. We can also restrict to rational values of `x` or place other constraints on the domain, but let’s stick to those 8 cases.
We have a similar variety of options on the codomain: we can specify that `f x` approaches a value from the left or right, or that it approaches positive or negative infinity, and so on. For example, we may wish to say that `f x` tends to `+∞` when `x` tends to `x₀` from the right without being equal to `x₀`. This results in 64 different kinds of limit statements, and we haven’t even begun to deal with limits of sequences, as we did in [Section 3.6](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C03_Logic.html#sequences-and-convergence).
The problem is compounded even further when it comes to the supporting lemmas. For instance, limits compose: if `f x` tends to `y₀` when `x` tends to `x₀` and `g y` tends to `z₀` when `y` tends to `y₀` then `g ∘ f x` tends to `z₀` when `x` tends to `x₀`. There are three notions of “tends to” at play here, each of which can be instantiated in any of the eight ways described in the previous paragraph. This results in 512 lemmas, a lot to have to add to a library! Informally, mathematicians generally prove two or three of these and simply note that the rest can be proved “in the same way.” Formalizing mathematics requires making the relevant notion of “sameness” fully explicit, and that is exactly what Bourbaki’s theory of filters manages to do.
##  11.1. Filters[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#filters "Link to this heading")
A _filter_ on a type `X` is a collection of sets of `X` that satisfies three conditions that we will spell out below. The notion supports two related ideas:
  * _limits_ , including all the kinds of limits discussed above: finite and infinite limits of sequences, finite and infinite limits of functions at a point or at infinity, and so on.
  * _things happening eventually_ , including things happening for large enough `n : ℕ`, or sufficiently near a point `x`, or for sufficiently close pairs of points, or almost everywhere in the sense of measure theory. Dually, filters can also express the idea of _things happening often_ : for arbitrarily large `n`, at a point in any neighborhood of a given point, etc.


The filters that correspond to these descriptions will be defined later in this section, but we can already name them:
  * `(atTop : Filter ℕ)`, made of sets of `ℕ` containing `{n | n ≥ N}` for some `N`
  * `𝓝 x`, made of neighborhoods of `x` in a topological space
  * `𝓤 X`, made of entourages of a uniform space (uniform spaces generalize metric spaces and topological groups)
  * `μ.ae` , made of sets whose complement has zero measure with respect to a measure `μ`.


The general definition is as follows: a filter `F : Filter X` is a collection of sets `F.sets : Set (Set X)` satisfying the following:
  * `F.univ_sets : univ ∈ F.sets`
  * `F.sets_of_superset : ∀ {U V}, U ∈ F.sets → U ⊆ V → V ∈ F.sets`
  * `F.inter_sets : ∀ {U V}, U ∈ F.sets → V ∈ F.sets → U ∩ V ∈ F.sets`.


The first condition says that the set of all elements of `X` belongs to `F.sets`. The second condition says that if `U` belongs to `F.sets` then anything containing `U` also belongs to `F.sets`. The third condition says that `F.sets` is closed under finite intersections. In Mathlib, a filter `F` is defined to be a structure bundling `F.sets` and its three properties, but the properties carry no additional data, and it is convenient to blur the distinction between `F` and `F.sets`. We therefore define `U ∈ F` to mean `U ∈ F.sets`. This explains why the word `sets` appears in the names of some lemmas that that mention `U ∈ F`.
It may help to think of a filter as defining a notion of a “sufficiently large” set. The first condition then says that `univ` is sufficiently large, the second one says that a set containing a sufficiently large set is sufficiently large and the third one says that the intersection of two sufficiently large sets is sufficiently large.
It may be even more useful to think of a filter on a type `X` as a generalized element of `Set X`. For instance, `atTop` is the “set of very large numbers” and `𝓝 x₀` is the “set of points very close to `x₀`.” One manifestation of this view is that we can associate to any `s : Set X` the so-called _principal filter_ consisting of all sets that contain `s`. This definition is already in Mathlib and has a notation `𝓟` (localized in the `Filter` namespace). For the purpose of demonstration, we ask you to take this opportunity to work out the definition here.

```
def principal {α : Type*} (s : Set α) : Filter α
    where
  sets := { t | s ⊆ t }
  univ_sets := sorry
  sets_of_superset := sorry
  inter_sets := sorry

```

For our second example, we ask you to define the filter `atTop : Filter ℕ`. (We could use any type with a preorder instead of `ℕ`.)

```
example : Filter ℕ :=
  { sets := { s | ∃ a, ∀ b, a ≤ b → b ∈ s }
    univ_sets := sorry
    sets_of_superset := sorry
    inter_sets := sorry }

```

We can also directly define the filter `𝓝 x` of neighborhoods of any `x : ℝ`. In the real numbers, a neighborhood of `x` is a set containing an open interval (x0−ε,x0+ε), defined in Mathlib as `Ioo (x₀ - ε) (x₀ + ε)`. (This notion of a neighborhood is only a special case of a more general construction in Mathlib.)
With these examples, we can already define what it means for a function `f : X → Y` to converge to some `G : Filter Y` along some `F : Filter X`, as follows:

```
def Tendsto₁ {X Y : Type*} (f : X → Y) (F : Filter X) (G : Filter Y) :=
  ∀ V ∈ G, f ⁻¹' V ∈ F

```

When `X` is `ℕ` and `Y` is `ℝ`, `Tendsto₁ u atTop (𝓝 x)` is equivalent to saying that the sequence `u : ℕ → ℝ` converges to the real number `x`. When both `X` and `Y` are `ℝ`, `Tendsto f (𝓝 x₀) (𝓝 y₀)` is equivalent to the familiar notion ₀₀limx→x₀f(x)=y₀. All of the other kinds of limits mentioned in the introduction are also equivalent to instances of `Tendsto₁` for suitable choices of filters on the source and target.
The notion `Tendsto₁` above is definitionally equivalent to the notion `Tendsto` that is defined in Mathlib, but the latter is defined more abstractly. The problem with the definition of `Tendsto₁` is that it exposes a quantifier and elements of `G`, and it hides the intuition that we get by viewing filters as generalized sets. We can hide the quantifier `∀ V` and make the intuition more salient by using more algebraic and set-theoretic machinery. The first ingredient is the _pushforward_ operation f∗ associated to any map `f : X → Y`, denoted `Filter.map f` in Mathlib. Given a filter `F` on `X`, `Filter.map f F : Filter Y` is defined so that `V ∈ Filter.map f F ↔ f ⁻¹' V ∈ F` holds definitionally. In the example file we’ve opened the `Filter` namespace so that `Filter.map` can be written as `map`. This means that we can rewrite the definition of `Tendsto` using the order relation on `Filter Y`, which is reversed inclusion of the set of members. In other words, given `G H : Filter Y`, we have `G ≤ H ↔ ∀ V : Set Y, V ∈ H → V ∈ G`.

```
def Tendsto₂ {X Y : Type*} (f : X → Y) (F : Filter X) (G : Filter Y) :=
  map f F ≤ G

example {X Y : Type*} (f : X → Y) (F : Filter X) (G : Filter Y) :
    Tendsto₂ f F G ↔ Tendsto₁ f F G :=
  Iff.rfl

```

It may seem that the order relation on filters is backward. But recall that we can view filters on `X` as generalized elements of `Set X`, via the inclusion of `𝓟 : Set X → Filter X` which maps any set `s` to the corresponding principal filter. This inclusion is order preserving, so the order relation on `Filter` can indeed be seen as the natural inclusion relation between generalized sets. In this analogy, pushforward is analogous to the direct image. And, indeed, `map f (𝓟 s) = 𝓟 (f '' s)`.
We can now understand intuitively why a sequence `u : ℕ → ℝ` converges to a point `x₀` if and only if we have `map u atTop ≤ 𝓝 x₀`. The inequality means the “direct image under `u`” of “the set of very big natural numbers” is “included” in “the set of points very close to `x₀`.”
As promised, the definition of `Tendsto₂` does not exhibit any quantifiers or sets. It also leverages the algebraic properties of the pushforward operation. First, each `Filter.map f` is monotone. And, second, `Filter.map` is compatible with composition.

```
#check (@Filter.map_mono : ∀ {α β} {m : α → β}, Monotone (map m))

#check
  (@Filter.map_map :
    ∀ {α β γ} {f : Filter α} {m : α → β} {m' : β → γ}, map m' (map m f) = map (m' ∘ m) f)

```

Together these two properties allow us to prove that limits compose, yielding in one shot all 512 variants of the composition lemma described in the introduction, and lots more. You can practice proving the following statement using either the definition of `Tendsto₁` in terms of the universal quantifier or the algebraic definition, together with the two lemmas above.

```
example {X Y Z : Type*} {F : Filter X} {G : Filter Y} {H : Filter Z} {f : X → Y} {g : Y → Z}
    (hf : Tendsto₁ f F G) (hg : Tendsto₁ g G H) : Tendsto₁ (g ∘ f) F H :=
  sorry

```

The pushforward construction uses a map to push filters from the map source to the map target. There also a _pullback_ operation, `Filter.comap`, going in the other direction. This generalizes the preimage operation on sets. For any map `f`, `Filter.map f` and `Filter.comap f` form what is known as a _Galois connection_ , which is to say, they satisfy
> `Filter.map_le_iff_le_comap : Filter.map f F ≤ G ↔ F ≤ Filter.comap f G`
for every `F` and `G`. This operation could be used to provided another formulation of `Tendsto` that would be provably (but not definitionally) equivalent to the one in Mathlib.
The `comap` operation can be used to restrict filters to a subtype. For instance, suppose we have `f : ℝ → ℝ`, `x₀ : ℝ` and `y₀ : ℝ`, and suppose we want to state that `f x` approaches `y₀` when `x` approaches `x₀` within the rational numbers. We can pull the filter `𝓝 x₀` back to `ℚ` using the coercion map `(↑) : ℚ → ℝ` and state `Tendsto (f ∘ (↑) : ℚ → ℝ) (comap (↑) (𝓝 x₀)) (𝓝 y₀)`.

```
variable (f : ℝ → ℝ) (x₀ y₀ : ℝ)

#check comap ((↑) : ℚ → ℝ) (𝓝 x₀)

#check Tendsto (f ∘ (↑)) (comap ((↑) : ℚ → ℝ) (𝓝 x₀)) (𝓝 y₀)

```

The pullback operation is also compatible with composition, but it is _contravariant_ , which is to say, it reverses the order of the arguments.

```
section
variable {α β γ : Type*} (F : Filter α) {m : γ → β} {n : β → α}

#check (comap_comap : comap m (comap n F) = comap (n ∘ m) F)

end

```

Let’s now shift attention to the plane `ℝ × ℝ` and try to understand how the neighborhoods of a point `(x₀, y₀)` are related to `𝓝 x₀` and `𝓝 y₀`. There is a product operation `Filter.prod : Filter X → Filter Y → Filter (X × Y)`, denoted by `×ˢ`, which answers this question:

```
example : 𝓝 (x₀, y₀) = 𝓝 x₀ ×ˢ 𝓝 y₀ :=
  nhds_prod_eq

```

The product operation is defined in terms of the pullback operation and the `inf` operation:
> `F ×ˢ G = (comap Prod.fst F) ⊓ (comap Prod.snd G)`.
Here the `inf` operation refers to the lattice structure on `Filter X` for any type `X`, whereby `F ⊓ G` is the greatest filter that is smaller than both `F` and `G`. Thus the `inf` operation generalizes the notion of the intersection of sets.
A lot of proofs in Mathlib use all of the aforementioned structure (`map`, `comap`, `inf`, `sup`, and `prod`) to give algebraic proofs about convergence without ever referring to members of filters. You can practice doing this in a proof of the following lemma, unfolding the definition of `Tendsto` and `Filter.prod` if needed.

```
#check le_inf_iff

example (f : ℕ → ℝ × ℝ) (x₀ y₀ : ℝ) :
    Tendsto f atTop (𝓝 (x₀, y₀)) ↔
      Tendsto (Prod.fst ∘ f) atTop (𝓝 x₀) ∧ Tendsto (Prod.snd ∘ f) atTop (𝓝 y₀) :=
  sorry

```

The ordered type `Filter X` is actually a _complete_ lattice, which is to say, there is a bottom element, there is a top element, and every set of filters on `X` has an `Inf` and a `Sup`.
Note that given the second property in the definition of a filter (if `U` belongs to `F` then anything larger than `U` also belongs to `F`), the first property (the set of all inhabitants of `X` belongs to `F`) is equivalent to the property that `F` is not the empty collection of sets. This shouldn’t be confused with the more subtle question as to whether the empty set is an _element_ of `F`. The definition of a filter does not prohibit `∅ ∈ F`, but if the empty set is in `F` then every set is in `F`, which is to say, `∀ U : Set X, U ∈ F`. In this case, `F` is a rather trivial filter, which is precisely the bottom element of the complete lattice `Filter X`. This contrasts with the definition of filters in Bourbaki, which doesn’t allow filters containing the empty set.
Because we include the trivial filter in our definition, we sometimes need to explicitly assume nontriviality in some lemmas. In return, however, the theory has nicer global properties. We have already seen that including the trivial filter gives us a bottom element. It also allows us to define `principal : Set X → Filter X`, which maps `∅` to `⊥`, without adding a precondition to rule out the empty set. And it allows us to define the pullback operation without a precondition as well. Indeed, it can happen that `comap f F = ⊥` although `F ≠ ⊥`. For instance, given `x₀ : ℝ` and `s : Set ℝ`, the pullback of `𝓝 x₀` under the coercion from the subtype corresponding to `s` is nontrivial if and only if `x₀` belongs to the closure of `s`.
In order to manage lemmas that do need to assume some filter is nontrivial, Mathlib has a type class `Filter.NeBot`, and the library has lemmas that assume `(F : Filter X) [F.NeBot]`. The instance database knows, for example, that `(atTop : Filter ℕ).NeBot`, and it knows that pushing forward a nontrivial filter gives a nontrivial filter. As a result, a lemma assuming `[F.NeBot]` will automatically apply to `map u atTop` for any sequence `u`.
Our tour of the algebraic properties of filters and their relation to limits is essentially done, but we have not yet justified our claim to have recaptured the usual limit notions. Superficially, it may seem that `Tendsto u atTop (𝓝 x₀)` is stronger than the notion of convergence defined in [Section 3.6](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C03_Logic.html#sequences-and-convergence) because we ask that _every_ neighborhood of `x₀` has a preimage belonging to `atTop`, whereas the usual definition only requires this for the standard neighborhoods `Ioo (x₀ - ε) (x₀ + ε)`. The key is that, by definition, every neighborhood contains such a standard one. This observation leads to the notion of a _filter basis_.
Given `F : Filter X`, a family of sets `s : ι → Set X` is a basis for `F` if for every set `U`, we have `U ∈ F` if and only if it contains some `s i`. In other words, formally speaking, `s` is a basis if it satisfies `∀ U : Set X, U ∈ F ↔ ∃ i, s i ⊆ U`. It is even more flexible to consider a predicate on `ι` that selects only some of the values `i` in the indexing type. In the case of `𝓝 x₀`, we want `ι` to be `ℝ`, we write `ε` for `i`, and the predicate should select the positive values of `ε`. So the fact that the sets `Ioo  (x₀ - ε) (x₀ + ε)` form a basis for the neighborhood topology on `ℝ` is stated as follows:

```
example (x₀ : ℝ) : HasBasis (𝓝 x₀) (fun ε : ℝ ↦ 0 < ε) fun ε ↦ Ioo (x₀ - ε) (x₀ + ε) :=
  nhds_basis_Ioo_pos x₀

```

There is also a nice basis for the filter `atTop`. The lemma `Filter.HasBasis.tendsto_iff` allows us to reformulate a statement of the form `Tendsto f F G` given bases for `F` and `G`. Putting these pieces together gives us essentially the notion of convergence that we used in [Section 3.6](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C03_Logic.html#sequences-and-convergence).

```
example (u : ℕ → ℝ) (x₀ : ℝ) :
    Tendsto u atTop (𝓝 x₀) ↔ ∀ ε > 0, ∃ N, ∀ n ≥ N, u n ∈ Ioo (x₀ - ε) (x₀ + ε) := by
  have : atTop.HasBasis (fun _ : ℕ ↦ True) Ici := atTop_basis
  rw [this.tendsto_iff (nhds_basis_Ioo_pos x₀)]
  simp

```

We now show how filters facilitate working with properties that hold for sufficiently large numbers or for points that are sufficiently close to a given point. In [Section 3.6](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C03_Logic.html#sequences-and-convergence), we were often faced with the situation where we knew that some property `P n` holds for sufficiently large `n` and that some other property `Q n` holds for sufficiently large `n`. Using `cases` twice gave us `N_P` and `N_Q` satisfying `∀ n ≥ N_P, P n` and `∀ n ≥ N_Q, Q n`. Using `set N := max N_P N_Q`, we could eventually prove `∀ n ≥ N, P n ∧ Q n`. Doing this repeatedly becomes tiresome.
We can do better by noting that the statement “`P n` and `Q n` hold for large enough `n`” means that we have `{n | P n} ∈ atTop` and `{n | Q n} ∈ atTop`. The fact that `atTop` is a filter implies that the intersection of two elements of `atTop` is again in `atTop`, so we have `{n | P n ∧ Q n} ∈ atTop`. Writing `{n | P n} ∈ atTop` is unpleasant, but we can use the more suggestive notation `∀ᶠ n in atTop, P n`. Here the superscripted `f` stands for “Filter.” You can think of the notation as saying that for all `n` in the “set of very large numbers,” `P n` holds. The `∀ᶠ` notation stands for `Filter.Eventually`, and the lemma `Filter.Eventually.and` uses the intersection property of filters to do what we just described:

```
example (P Q : ℕ → Prop) (hP : ∀ᶠ n in atTop, P n) (hQ : ∀ᶠ n in atTop, Q n) :
    ∀ᶠ n in atTop, P n ∧ Q n :=
  hP.and hQ

```

This notation is so convenient and intuitive that we also have specializations when `P` is an equality or inequality statement. For example, let `u` and `v` be two sequences of real numbers, and let us show that if `u n` and `v n` coincide for sufficiently large `n` then `u` tends to `x₀` if and only if `v` tends to `x₀`. First we’ll use the generic `Eventually` and then the one specialized for the equality predicate, `EventuallyEq`. The two statements are definitionally equivalent so the same proof work in both cases.

```
example (u v : ℕ → ℝ) (h : ∀ᶠ n in atTop, u n = v n) (x₀ : ℝ) :
    Tendsto u atTop (𝓝 x₀) ↔ Tendsto v atTop (𝓝 x₀) :=
  tendsto_congr' h

example (u v : ℕ → ℝ) (h : u =ᶠ[atTop] v) (x₀ : ℝ) :
    Tendsto u atTop (𝓝 x₀) ↔ Tendsto v atTop (𝓝 x₀) :=
  tendsto_congr' h

```

It is instructive to review the definition of filters in terms of `Eventually`. Given `F : Filter X`, for any predicates `P` and `Q` on `X`,
  * the condition `univ ∈ F` ensures `(∀ x, P x) → ∀ᶠ x in F, P x`,
  * the condition `U ∈ F → U ⊆ V → V ∈ F` ensures `(∀ᶠ x in F, P x) → (∀ x, P x → Q x) → ∀ᶠ x in F, Q x`, and
  * the condition `U ∈ F → V ∈ F → U ∩ V ∈ F` ensures `(∀ᶠ x in F, P x) → (∀ᶠ x in F, Q x) → ∀ᶠ x in F, P x ∧ Q x`.



```
#check Eventually.of_forall
#check Eventually.mono
#check Eventually.and

```

The second item, corresponding to `Eventually.mono`, supports nice ways of using filters, especially when combined with `Eventually.and`. The `filter_upwards` tactic allows us to combine them. Compare:

```
example (P Q R : ℕ → Prop) (hP : ∀ᶠ n in atTop, P n) (hQ : ∀ᶠ n in atTop, Q n)
    (hR : ∀ᶠ n in atTop, P n ∧ Q n → R n) : ∀ᶠ n in atTop, R n := by
  apply (hP.and (hQ.and hR)).mono
  rintro n ⟨h, h', h''⟩
  exact h'' ⟨h, h'⟩

example (P Q R : ℕ → Prop) (hP : ∀ᶠ n in atTop, P n) (hQ : ∀ᶠ n in atTop, Q n)
    (hR : ∀ᶠ n in atTop, P n ∧ Q n → R n) : ∀ᶠ n in atTop, R n := by
  filter_upwards [hP, hQ, hR] with n h h' h''
  exact h'' ⟨h, h'⟩

```

Readers who know about measure theory will note that the filter `μ.ae` of sets whose complement has measure zero (aka “the set consisting of almost every point”) is not very useful as the source or target of `Tendsto`, but it can be conveniently used with `Eventually` to say that a property holds for almost every point.
There is a dual version of `∀ᶠ x in F, P x`, which is occasionally useful: `∃ᶠ x in F, P x` means `{x | ¬P x} ∉ F`. For example, `∃ᶠ n in atTop, P n` means there are arbitrarily large `n` such that `P n` holds. The `∃ᶠ` notation stands for `Filter.Frequently`.
For a more sophisticated example, consider the following statement about a sequence `u`, a set `M`, and a value `x`:
> If `u` converges to `x` and `u n` belongs to `M` for sufficiently large `n` then `x` is in the closure of `M`.
This can be formalized as follows:
> `Tendsto u atTop (𝓝 x) → (∀ᶠ n in atTop, u n ∈ M) → x ∈ closure M`.
This is a special case of the theorem `mem_closure_of_tendsto` from the topology library. See if you can prove it using the quoted lemmas, using the fact that `ClusterPt x F` means `(𝓝 x ⊓ F).NeBot` and that, by definition, the assumption `∀ᶠ n in atTop, u n ∈ M` means `M ∈ map u atTop`.

```
#check mem_closure_iff_clusterPt
#check le_principal_iff
#check neBot_of_le

example (u : ℕ → ℝ) (M : Set ℝ) (x : ℝ) (hux : Tendsto u atTop (𝓝 x))
    (huM : ∀ᶠ n in atTop, u n ∈ M) : x ∈ closure M :=
  sorry

```

##  11.2. Metric spaces[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#metric-spaces "Link to this heading")
Examples in the previous section focus on sequences of real numbers. In this section we will go up a bit in generality and focus on metric spaces. A metric space is a type `X` equipped with a distance function `dist : X → X → ℝ` which is a generalization of the function `fun x y ↦ |x - y|` from the case where `X = ℝ`.
Introducing such a space is easy and we will check all properties required from the distance function.

```
variable {X : Type*} [MetricSpace X] (a b c : X)

#check (dist a b : ℝ)
#check (dist_nonneg : 0 ≤ dist a b)
#check (dist_eq_zero : dist a b = 0 ↔ a = b)
#check (dist_comm a b : dist a b = dist b a)
#check (dist_triangle a b c : dist a c ≤ dist a b + dist b c)

```

Note we also have variants where the distance can be infinite or where `dist a b` can be zero without having `a = b` or both. They are called `EMetricSpace`, `PseudoMetricSpace` and `PseudoEMetricSpace` respectively (here “e” stands for “extended”).
Note that our journey from `ℝ` to metric spaces jumped over the special case of normed spaces that also require linear algebra and will be explained as part of the calculus chapter.
###  11.2.1. Convergence and continuity[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#convergence-and-continuity "Link to this heading")
Using distance functions, we can already define convergent sequences and continuous functions between metric spaces. They are actually defined in a more general setting covered in the next section, but we have lemmas recasting the definition in terms of distances.

```
example {u : ℕ → X} {a : X} :
    Tendsto u atTop (𝓝 a) ↔ ∀ ε > 0, ∃ N, ∀ n ≥ N, dist (u n) a < ε :=
  Metric.tendsto_atTop

example {X Y : Type*} [MetricSpace X] [MetricSpace Y] {f : X → Y} :
    Continuous f ↔
      ∀ x : X, ∀ ε > 0, ∃ δ > 0, ∀ x', dist x' x < δ → dist (f x') (f x) < ε :=
  Metric.continuous_iff

```

A _lot_ of lemmas have some continuity assumptions, so we end up proving a lot of continuity results and there is a `continuity` tactic devoted to this task. Let’s prove a continuity statement that will be needed in an exercise below. Notice that Lean knows how to treat a product of two metric spaces as a metric space, so it makes sense to consider continuous functions from `X × X` to `ℝ`. In particular the (uncurried version of the) distance function is such a function.

```
example {X Y : Type*} [MetricSpace X] [MetricSpace Y] {f : X → Y} (hf : Continuous f) :
    Continuous fun p : X × X ↦ dist (f p.1) (f p.2) := by continuity

```

This tactic is a bit slow, so it is also useful to know how to do it by hand. We first need to use that `fun p : X × X ↦ f p.1` is continuous because it is the composition of `f`, which is continuous by assumption `hf`, and the projection `prod.fst` whose continuity is the content of the lemma `continuous_fst`. The composition property is `Continuous.comp` which is in the `Continuous` namespace so we can use dot notation to compress `Continuous.comp hf continuous_fst` into `hf.comp continuous_fst` which is actually more readable since it really reads as composing our assumption and our lemma. We can do the same for the second component to get continuity of `fun p : X × X ↦ f p.2`. We then assemble those two continuities using `Continuous.prod_mk` to get `(hf.comp continuous_fst).prod_mk (hf.comp continuous_snd) : Continuous (fun p : X × X ↦ (f p.1, f p.2))` and compose once more to get our full proof.

```
example {X Y : Type*} [MetricSpace X] [MetricSpace Y] {f : X → Y} (hf : Continuous f) :
    Continuous fun p : X × X ↦ dist (f p.1) (f p.2) :=
  continuous_dist.comp ((hf.comp continuous_fst).prodMk (hf.comp continuous_snd))

```

The combination of `Continuous.prod_mk` and `continuous_dist` via `Continuous.comp` feels clunky, even when heavily using dot notation as above. A more serious issue is that this nice proof requires a lot of planning. Lean accepts the above proof term because it is a full term proving a statement which is definitionally equivalent to our goal, the crucial definition to unfold being that of a composition of functions. Indeed our target function `fun p : X × X ↦ dist (f p.1) (f p.2)` is not presented as a composition. The proof term we provided proves continuity of `dist ∘ (fun p : X × X ↦ (f p.1, f p.2))` which happens to be definitionally equal to our target function. But if we try to build this proof gradually using tactics starting with `apply continuous_dist.comp` then Lean’s elaborator will fail to recognize a composition and refuse to apply this lemma. It is especially bad at this when products of types are involved.
A better lemma to apply here is `Continuous.dist {f g : X → Y} : Continuous f → Continuous g → Continuous (fun x ↦ dist (f x) (g x))` which is nicer to Lean’s elaborator and also provides a shorter proof when directly providing a full proof term, as can be seen from the following two new proofs of the above statement:

```
example {X Y : Type*} [MetricSpace X] [MetricSpace Y] {f : X → Y} (hf : Continuous f) :
    Continuous fun p : X × X ↦ dist (f p.1) (f p.2) := by
  apply Continuous.dist
  exact hf.comp continuous_fst
  exact hf.comp continuous_snd

example {X Y : Type*} [MetricSpace X] [MetricSpace Y] {f : X → Y} (hf : Continuous f) :
    Continuous fun p : X × X ↦ dist (f p.1) (f p.2) :=
  (hf.comp continuous_fst).dist (hf.comp continuous_snd)

```

Note that, without the elaboration issue coming from composition, another way to compress our proof would be to use `Continuous.prod_map` which is sometimes useful and gives as an alternate proof term `continuous_dist.comp (hf.prod_map hf)` which even shorter to type.
Since it is sad to decide between a version which is better for elaboration and a version which is shorter to type, let us wrap this discussion with a last bit of compression offered by `Continuous.fst'` which allows to compress `hf.comp continuous_fst` to `hf.fst'` (and the same with `snd`) and get our final proof, now bordering obfuscation.

```
example {X Y : Type*} [MetricSpace X] [MetricSpace Y] {f : X → Y} (hf : Continuous f) :
    Continuous fun p : X × X ↦ dist (f p.1) (f p.2) :=
  hf.fst'.dist hf.snd'

```

It’s your turn now to prove some continuity lemma. After trying the continuity tactic, you will need `Continuous.add`, `continuous_pow` and `continuous_id` to do it by hand.

```
example {f : ℝ → X} (hf : Continuous f) : Continuous fun x : ℝ ↦ f (x ^ 2 + x) :=
  sorry

```

So far we saw continuity as a global notion, but one can also define continuity at a point.

```
example {X Y : Type*} [MetricSpace X] [MetricSpace Y] (f : X → Y) (a : X) :
    ContinuousAt f a ↔ ∀ ε > 0, ∃ δ > 0, ∀ {x}, dist x a < δ → dist (f x) (f a) < ε :=
  Metric.continuousAt_iff

```

###  11.2.2. Balls, open sets and closed sets[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#balls-open-sets-and-closed-sets "Link to this heading")
Once we have a distance function, the most important geometric definitions are (open) balls and closed balls.

```
variable (r : ℝ)

example : Metric.ball a r = { b | dist b a < r } :=
  rfl

example : Metric.closedBall a r = { b | dist b a ≤ r } :=
  rfl

```

Note that r is any real number here, there is no sign restriction. Of course some statements do require a radius condition.

```
example (hr : 0 < r) : a ∈ Metric.ball a r :=
  Metric.mem_ball_self hr

example (hr : 0 ≤ r) : a ∈ Metric.closedBall a r :=
  Metric.mem_closedBall_self hr

```

Once we have balls, we can define open sets. They are actually defined in a more general setting covered in the next section, but we have lemmas recasting the definition in terms of balls.

```
example (s : Set X) : IsOpen s ↔ ∀ x ∈ s, ∃ ε > 0, Metric.ball x ε ⊆ s :=
  Metric.isOpen_iff

```

Then closed sets are sets whose complement is open. Their important property is they are closed under limits. The closure of a set is the smallest closed set containing it.

```
example {s : Set X} : IsClosed s ↔ IsOpen (sᶜ) :=
  isOpen_compl_iff.symm

example {s : Set X} (hs : IsClosed s) {u : ℕ → X} (hu : Tendsto u atTop (𝓝 a))
    (hus : ∀ n, u n ∈ s) : a ∈ s :=
  hs.mem_of_tendsto hu (Eventually.of_forall hus)

example {s : Set X} : a ∈ closure s ↔ ∀ ε > 0, ∃ b ∈ s, a ∈ Metric.ball b ε :=
  Metric.mem_closure_iff

```

Do the next exercise without using mem_closure_iff_seq_limit

```
example {u : ℕ → X} (hu : Tendsto u atTop (𝓝 a)) {s : Set X} (hs : ∀ n, u n ∈ s) :
    a ∈ closure s := by
  sorry

```

Remember from the filters sections that neighborhood filters play a big role in Mathlib. In the metric space context, the crucial point is that balls provide bases for those filters. The main lemmas here are `Metric.nhds_basis_ball` and `Metric.nhds_basis_closedBall` that claim this for open and closed balls with positive radius. The center point is an implicit argument so we can invoke `Filter.HasBasis.mem_iff` as in the following example.

```
example {x : X} {s : Set X} : s ∈ 𝓝 x ↔ ∃ ε > 0, Metric.ball x ε ⊆ s :=
  Metric.nhds_basis_ball.mem_iff

example {x : X} {s : Set X} : s ∈ 𝓝 x ↔ ∃ ε > 0, Metric.closedBall x ε ⊆ s :=
  Metric.nhds_basis_closedBall.mem_iff

```

###  11.2.3. Compactness[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#compactness "Link to this heading")
Compactness is an important topological notion. It distinguishes subsets of a metric space that enjoy the same kind of properties as segments in the reals compared to other intervals:
  * Any sequence with values in a compact set has a subsequence that converges in this set.
  * Any continuous function on a nonempty compact set with values in real numbers is bounded and attains its bounds somewhere (this is called the extreme value theorem).
  * Compact sets are closed sets.


Let us first check that the unit interval in the reals is indeed a compact set, and then check the above claims for compact sets in general metric spaces. In the second statement we only need continuity on the given set so we will use `ContinuousOn` instead of `Continuous`, and we will give separate statements for the minimum and the maximum. Of course all these results are deduced from more general versions, some of which will be discussed in later sections.

```
example : IsCompact (Set.Icc 0 1 : Set ℝ) :=
  isCompact_Icc

example {s : Set X} (hs : IsCompact s) {u : ℕ → X} (hu : ∀ n, u n ∈ s) :
    ∃ a ∈ s, ∃ φ : ℕ → ℕ, StrictMono φ ∧ Tendsto (u ∘ φ) atTop (𝓝 a) :=
  hs.tendsto_subseq hu

example {s : Set X} (hs : IsCompact s) (hs' : s.Nonempty) {f : X → ℝ}
      (hfs : ContinuousOn f s) :
    ∃ x ∈ s, ∀ y ∈ s, f x ≤ f y :=
  hs.exists_isMinOn hs' hfs

example {s : Set X} (hs : IsCompact s) (hs' : s.Nonempty) {f : X → ℝ}
      (hfs : ContinuousOn f s) :
    ∃ x ∈ s, ∀ y ∈ s, f y ≤ f x :=
  hs.exists_isMaxOn hs' hfs

example {s : Set X} (hs : IsCompact s) : IsClosed s :=
  hs.isClosed

```

We can also specify that a metric spaces is globally compact, using an extra `Prop`-valued type class:

```
example {X : Type*} [MetricSpace X] [CompactSpace X] : IsCompact (univ : Set X) :=
  isCompact_univ

```

In a compact metric space any closed set is compact, this is `IsClosed.isCompact`.
###  11.2.4. Uniformly continuous functions[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#uniformly-continuous-functions "Link to this heading")
We now turn to uniformity notions on metric spaces : uniformly continuous functions, Cauchy sequences and completeness. Again those are defined in a more general context but we have lemmas in the metric name space to access their elementary definitions. We start with uniform continuity.

```
example {X : Type*} [MetricSpace X] {Y : Type*} [MetricSpace Y] {f : X → Y} :
    UniformContinuous f ↔
      ∀ ε > 0, ∃ δ > 0, ∀ {a b : X}, dist a b < δ → dist (f a) (f b) < ε :=
  Metric.uniformContinuous_iff

```

In order to practice manipulating all those definitions, we will prove that continuous functions from a compact metric space to a metric space are uniformly continuous (we will see a more general version in a later section).
We will first give an informal sketch. Let `f : X → Y` be a continuous function from a compact metric space to a metric space. We fix `ε > 0` and start looking for some `δ`.
Let `φ : X × X → ℝ := fun p ↦ dist (f p.1) (f p.2)` and let `K := { p : X × X | ε ≤ φ p }`. Observe `φ` is continuous since `f` and distance are continuous. And `K` is clearly closed (use `isClosed_le`) hence compact since `X` is compact.
Then we discuss two possibilities using `eq_empty_or_nonempty`. If `K` is empty then we are clearly done (we can set `δ = 1` for instance). So let’s assume `K` is not empty, and use the extreme value theorem to choose `(x₀, x₁)` attaining the infimum of the distance function on `K`. We can then set `δ = dist x₀ x₁` and check everything works.

```
example {X : Type*} [MetricSpace X] [CompactSpace X]
      {Y : Type*} [MetricSpace Y] {f : X → Y}
    (hf : Continuous f) : UniformContinuous f := by
  sorry

```

###  11.2.5. Completeness[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#completeness "Link to this heading")
A Cauchy sequence in a metric space is a sequence whose terms get closer and closer to each other. There are a couple of equivalent ways to state that idea. In particular converging sequences are Cauchy. The converse is true only in so-called _complete_ spaces.

```
example (u : ℕ → X) :
    CauchySeq u ↔ ∀ ε > 0, ∃ N : ℕ, ∀ m ≥ N, ∀ n ≥ N, dist (u m) (u n) < ε :=
  Metric.cauchySeq_iff

example (u : ℕ → X) :
    CauchySeq u ↔ ∀ ε > 0, ∃ N : ℕ, ∀ n ≥ N, dist (u n) (u N) < ε :=
  Metric.cauchySeq_iff'

example [CompleteSpace X] (u : ℕ → X) (hu : CauchySeq u) :
    ∃ x, Tendsto u atTop (𝓝 x) :=
  cauchySeq_tendsto_of_complete hu

```

We’ll practice using this definition by proving a convenient criterion which is a special case of a criterion appearing in Mathlib. This is also a good opportunity to practice using big sums in a geometric context. In addition to the explanations from the filters section, you will probably need `tendsto_pow_atTop_nhds_zero_of_lt_one`, `Tendsto.mul` and `dist_le_range_sum_dist`.

```
theorem cauchySeq_of_le_geometric_two' {u : ℕ → X}
    (hu : ∀ n : ℕ, dist (u n) (u (n + 1)) ≤ (1 / 2) ^ n) : CauchySeq u := by
  rw [Metric.cauchySeq_iff']
  intro ε ε_pos
  obtain ⟨N, hN⟩ : ∃ N : ℕ, 1 / 2 ^ N * 2 < ε := by sorry
  use N
  intro n hn
  obtain ⟨k, rfl : n = N + k⟩ := le_iff_exists_add.mp hn
  calc
    dist (u (N + k)) (u N) = dist (u (N + 0)) (u (N + k)) := sorry
    _ ≤ ∑ i  ∈ range k, dist (u (N + i)) (u (N + (i + 1))) := sorry
    _ ≤ ∑ i  ∈ range k, (1 / 2 : ℝ) ^ (N + i) := sorry
    _ = 1 / 2 ^ N * ∑ i  ∈ range k, (1 / 2 : ℝ) ^ i := sorry
    _ ≤ 1 / 2 ^ N * 2 := sorry
    _ < ε := sorry

```

We are ready for the final boss of this section: Baire’s theorem for complete metric spaces! The proof skeleton below shows interesting techniques. It uses the `choose` tactic in its exclamation mark variant (you should experiment with removing this exclamation mark) and it shows how to define something inductively in the middle of a proof using `Nat.rec_on`.

```
open Metric

example [CompleteSpace X] (f : ℕ → Set X) (ho : ∀ n, IsOpen (f n)) (hd : ∀ n, Dense (f n)) :
    Dense (⋂ n, f n) := by
  let B : ℕ → ℝ := fun n ↦ (1 / 2) ^ n
  have Bpos : ∀ n, 0 < B n
  sorry
  /- Translate the density assumption into two functions `center` and `radius` associating
    to any n, x, δ, δpos a center and a positive radius such that
    `closedBall center radius` is included both in `f n` and in `closedBall x δ`.
    We can also require `radius ≤ (1/2)^(n+1)`, to ensure we get a Cauchy sequence later. -/
  have :
    ∀ (n : ℕ) (x : X),
      ∀ δ > 0, ∃ y : X, ∃ r > 0, r ≤ B (n + 1) ∧ closedBall y r ⊆ closedBall x δ ∩ f n :=
    by sorry
  choose! center radius Hpos HB Hball using this
  intro x
  rw [mem_closure_iff_nhds_basis nhds_basis_closedBall]
  intro ε εpos
  /- `ε` is positive. We have to find a point in the ball of radius `ε` around `x`
    belonging to all `f n`. For this, we construct inductively a sequence
    `F n = (c n, r n)` such that the closed ball `closedBall (c n) (r n)` is included
    in the previous ball and in `f n`, and such that `r n` is small enough to ensure
    that `c n` is a Cauchy sequence. Then `c n` converges to a limit which belongs
    to all the `f n`. -/
  let F : ℕ → X × ℝ := fun n ↦
    Nat.recOn n (Prod.mk x (min ε (B 0)))
      fun n p ↦ Prod.mk (center n p.1 p.2) (radius n p.1 p.2)
  let c : ℕ → X := fun n ↦ (F n).1
  let r : ℕ → ℝ := fun n ↦ (F n).2
  have rpos : ∀ n, 0 < r n := by sorry
  have rB : ∀ n, r n ≤ B n := by sorry
  have incl : ∀ n, closedBall (c (n + 1)) (r (n + 1)) ⊆ closedBall (c n) (r n) ∩ f n := by
    sorry
  have cdist : ∀ n, dist (c n) (c (n + 1)) ≤ B n := by sorry
  have : CauchySeq c := cauchySeq_of_le_geometric_two' cdist
  -- as the sequence `c n` is Cauchy in a complete space, it converges to a limit `y`.
  rcases cauchySeq_tendsto_of_complete this with ⟨y, ylim⟩
  -- this point `y` will be the desired point. We will check that it belongs to all
  -- `f n` and to `ball x ε`.
  use y
  have I : ∀ n, ∀ m ≥ n, closedBall (c m) (r m) ⊆ closedBall (c n) (r n) := by sorry
  have yball : ∀ n, y ∈ closedBall (c n) (r n) := by sorry
  sorry

```

##  11.3. Topological spaces[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#topological-spaces "Link to this heading")
###  11.3.1. Fundamentals[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#fundamentals "Link to this heading")
We now go up in generality and introduce topological spaces. We will review the two main ways to define topological spaces and then explain how the category of topological spaces is much better behaved than the category of metric spaces. Note that we won’t be using Mathlib category theory here, only having a somewhat categorical point of view.
The first way to think about the transition from metric spaces to topological spaces is that we only remember the notion of open sets (or equivalently the notion of closed sets). From this point of view, a topological space is a type equipped with a collection of sets that are called open sets. This collection has to satisfy a number of axioms presented below (this collection is slightly redundant but we will ignore that).

```
section
variable {X : Type*} [TopologicalSpace X]

example : IsOpen (univ : Set X) :=
  isOpen_univ

example : IsOpen (∅ : Set X) :=
  isOpen_empty

example {ι : Type*} {s : ι → Set X} (hs : ∀ i, IsOpen (s i)) : IsOpen (⋃ i, s i) :=
  isOpen_iUnion hs

example {ι : Type*} [Fintype ι] {s : ι → Set X} (hs : ∀ i, IsOpen (s i)) :
    IsOpen (⋂ i, s i) :=
  isOpen_iInter_of_finite hs

```

Closed sets are then defined as sets whose complement is open. A function between topological spaces is (globally) continuous if all preimages of open sets are open.

```
variable {Y : Type*} [TopologicalSpace Y]

example {f : X → Y} : Continuous f ↔ ∀ s, IsOpen s → IsOpen (f ⁻¹' s) :=
  continuous_def

```

With this definition we already see that, compared to metric spaces, topological spaces only remember enough information to talk about continuous functions: two topological structures on a type are the same if and only if they have the same continuous functions (indeed the identity function will be continuous in both direction if and only if the two structures have the same open sets).
However as soon as we move on to continuity at a point we see the limitations of the approach based on open sets. In Mathlib we frequently think of topological spaces as types equipped with a neighborhood filter `𝓝 x` attached to each point `x` (the corresponding function `X → Filter X` satisfies certain conditions explained further down). Remember from the filters section that these gadgets play two related roles. First `𝓝 x` is seen as the generalized set of points of `X` that are close to `x`. And then it is seen as giving a way to say, for any predicate `P : X → Prop`, that this predicate holds for points that are close enough to `x`. Let us state that `f : X → Y` is continuous at `x`. The purely filtery way is to say that the direct image under `f` of the generalized set of points that are close to `x` is contained in the generalized set of points that are close to `f x`. Recall this is spelled either `map f (𝓝 x) ≤ 𝓝 (f x)` or `Tendsto f (𝓝 x) (𝓝 (f x))`.

```
example {f : X → Y} {x : X} : ContinuousAt f x ↔ map f (𝓝 x) ≤ 𝓝 (f x) :=
  Iff.rfl

```

One can also spell it using both neighborhoods seen as ordinary sets and a neighborhood filter seen as a generalized set: “for any neighborhood `U` of `f x`, all points close to `x` are sent to `U`”. Note that the proof is again `Iff.rfl`, this point of view is definitionally equivalent to the previous one.

```
example {f : X → Y} {x : X} : ContinuousAt f x ↔ ∀ U ∈ 𝓝 (f x), ∀ᶠ x in 𝓝 x, f x ∈ U :=
  Iff.rfl

```

We now explain how to go from one point of view to the other. In terms of open sets, we can simply define members of `𝓝 x` as sets that contain an open set containing `x`.

```
example {x : X} {s : Set X} : s ∈ 𝓝 x ↔ ∃ t, t ⊆ s ∧ IsOpen t ∧ x ∈ t :=
  mem_nhds_iff

```

To go in the other direction we need to discuss the condition that `𝓝 : X → Filter X` must satisfy in order to be the neighborhood function of a topology.
The first constraint is that `𝓝 x`, seen as a generalized set, contains the set `{x}` seen as the generalized set `pure x` (explaining this weird name would be too much of a digression, so we simply accept it for now). Another way to say it is that if a predicate holds for points close to `x` then it holds at `x`.

```
example (x : X) : pure x ≤ 𝓝 x :=
  pure_le_nhds x

example (x : X) (P : X → Prop) (h : ∀ᶠ y in 𝓝 x, P y) : P x :=
  h.self_of_nhds

```

Then a more subtle requirement is that, for any predicate `P : X → Prop` and any `x`, if `P y` holds for `y` close to `x` then for `y` close to `x` and `z` close to `y`, `P z` holds. More precisely we have:

```
example {P : X → Prop} {x : X} (h : ∀ᶠ y in 𝓝 x, P y) : ∀ᶠ y in 𝓝 x, ∀ᶠ z in 𝓝 y, P z :=
  eventually_eventually_nhds.mpr h

```

Those two results characterize the functions `X → Filter X` that are neighborhood functions for a topological space structure on `X`. There is a still a function `TopologicalSpace.mkOfNhds : (X → Filter X) → TopologicalSpace X` but it will give back its input as a neighborhood function only if it satisfies the above two constraints. More precisely we have a lemma `TopologicalSpace.nhds_mkOfNhds` saying that in a different way and our next exercise deduces this different way from how we stated it above.

```
example {α : Type*} (n : α → Filter α) (H₀ : ∀ a, pure a ≤ n a)
    (H : ∀ a : α, ∀ p : α → Prop, (∀ᶠ x in n a, p x) → ∀ᶠ y in n a, ∀ᶠ x in n y, p x) :
    ∀ a, ∀ s ∈ n a, ∃ t ∈ n a, t ⊆ s ∧ ∀ a' ∈ t, s ∈ n a' := by
  sorry
end

```

Note that `TopologicalSpace.mkOfNhds` is not so frequently used, but it still good to know in what precise sense the neighborhood filters is all there is in a topological space structure.
The next thing to know in order to efficiently use topological spaces in Mathlib is that we use a lot of formal properties of `TopologicalSpace : Type u → Type u`. From a purely mathematical point of view, those formal properties are a very clean way to explain how topological spaces solve issues that metric spaces have. From this point of view, the issues solved by topological spaces is that metric spaces enjoy very little functoriality, and have very bad categorical properties in general. This comes on top of the fact already discussed that metric spaces contain a lot of geometrical information that is not topologically relevant.
Let us focus on functoriality first. A metric space structure can be induced on a subset or, equivalently, it can be pulled back by an injective map. But that’s pretty much everything. They cannot be pulled back by general map or pushed forward, even by surjective maps.
In particular there is no sensible distance to put on a quotient of a metric space or on an uncountable product of metric spaces. Consider for instance the type `ℝ → ℝ`, seen as a product of copies of `ℝ` indexed by `ℝ`. We would like to say that pointwise convergence of sequences of functions is a respectable notion of convergence. But there is no distance on `ℝ → ℝ` that gives this notion of convergence. Relatedly, there is no distance ensuring that a map `f : X → (ℝ → ℝ)` is continuous if and only if `fun x ↦ f x t` is continuous for every `t : ℝ`.
We now review the data used to solve all those issues. First we can use any map `f : X → Y` to push or pull topologies from one side to the other. Those two operations form a Galois connection.

```
variable {X Y : Type*}

example (f : X → Y) : TopologicalSpace X → TopologicalSpace Y :=
  TopologicalSpace.coinduced f

example (f : X → Y) : TopologicalSpace Y → TopologicalSpace X :=
  TopologicalSpace.induced f

example (f : X → Y) (T_X : TopologicalSpace X) (T_Y : TopologicalSpace Y) :
    TopologicalSpace.coinduced f T_X ≤ T_Y ↔ T_X ≤ TopologicalSpace.induced f T_Y :=
  coinduced_le_iff_le_induced

```

Those operations are compatible with composition of functions. As usual, pushing forward is covariant and pulling back is contravariant, see `coinduced_compose` and `induced_compose`. On paper we will use notations f∗T for `TopologicalSpace.coinduced f T` and f∗T for `TopologicalSpace.induced f T`.
Then the next big piece is a complete lattice structure on `TopologicalSpace X` for any given structure. If you think of topologies as being primarily the data of open sets then you expect the order relation on `TopologicalSpace X` to come from `Set (Set X)`, i.e. you expect `t ≤ t'` if a set `u` is open for `t'` as soon as it is open for `t`. However we already know that Mathlib focuses on neighborhoods more than open sets so, for any `x : X` we want the map from topological spaces to neighborhoods `fun T : TopologicalSpace X ↦ @nhds X T x` to be order preserving. And we know the order relation on `Filter X` is designed to ensure an order preserving `principal : Set X → Filter X`, allowing to see filters as generalized sets. So the order relation we do use on `TopologicalSpace X` is opposite to the one coming from `Set (Set X)`.

```
example {T T' : TopologicalSpace X} : T ≤ T' ↔ ∀ s, T'.IsOpen s → T.IsOpen s :=
  Iff.rfl

```

Now we can recover continuity by combining the push-forward (or pull-back) operation with the order relation.

```
example (T_X : TopologicalSpace X) (T_Y : TopologicalSpace Y) (f : X → Y) :
    Continuous f ↔ TopologicalSpace.coinduced f T_X ≤ T_Y :=
  continuous_iff_coinduced_le

```

With this definition and the compatibility of push-forward and composition, we get for free the universal property that, for any topological space Z, a function g:Y→Z is continuous for the topology f∗TX if and only if g∘f is continuous.
g continuous ⇔g∗(f∗TX)≤TZ⇔(g∘f)∗TX≤TZ⇔g∘f continuous

```
example {Z : Type*} (f : X → Y) (T_X : TopologicalSpace X) (T_Z : TopologicalSpace Z)
      (g : Y → Z) :
    @Continuous Y Z (TopologicalSpace.coinduced f T_X) T_Z g ↔
      @Continuous X Z T_X T_Z (g ∘ f) := by
  rw [continuous_iff_coinduced_le, coinduced_compose, continuous_iff_coinduced_le]

```

So we already get quotient topologies (using the projection map as `f`). This wasn’t using that `TopologicalSpace X` is a complete lattice for all `X`. Let’s now see how all this structure proves the existence of the product topology by abstract non-sense. We considered the case of `ℝ → ℝ` above, but let’s now consider the general case of `Π i, X i` for some `ι : Type*` and `X : ι → Type*`. We want, for any topological space `Z` and any function `f : Z → Π i, X i`, that `f` is continuous if and only if `(fun x ↦ x i) ∘ f` is continuous for all `i`. Let us explore that constraint “on paper” using notation pi for the projection `(fun (x : Π i, X i) ↦ x i)`:
(∀i,pi∘f continuous)⇔∀i,(pi∘f)∗TZ≤TXi⇔∀i,(pi)∗f∗TZ≤TXi⇔∀i,f∗TZ≤(pi)∗TXi⇔f∗TZ≤inf[(pi)∗TXi]
So we see that what is the topology we want on `Π i, X i`:

```
example (ι : Type*) (X : ι → Type*) (T_X : ∀ i, TopologicalSpace (X i)) :
    (Pi.topologicalSpace : TopologicalSpace (∀ i, X i)) =
      ⨅ i, TopologicalSpace.induced (fun x ↦ x i) (T_X i) :=
  rfl

```

This ends our tour of how Mathlib thinks that topological spaces fix defects of the theory of metric spaces by being a more functorial theory and having a complete lattice structure for any fixed type.
###  11.3.2. Separation and countability[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#separation-and-countability "Link to this heading")
We saw that the category of topological spaces have very nice properties. The price to pay for this is existence of rather pathological topological spaces. There are a number of assumptions you can make on a topological space to ensure its behavior is closer to what metric spaces do. The most important is `T2Space`, also called “Hausdorff”, that will ensure that limits are unique. A stronger separation property is `T3Space` that ensures in addition the RegularSpace property: each point has a basis of closed neighborhoods.

```
example [TopologicalSpace X] [T2Space X] {u : ℕ → X} {a b : X} (ha : Tendsto u atTop (𝓝 a))
    (hb : Tendsto u atTop (𝓝 b)) : a = b :=
  tendsto_nhds_unique ha hb

example [TopologicalSpace X] [RegularSpace X] (a : X) :
    (𝓝 a).HasBasis (fun s : Set X ↦ s ∈ 𝓝 a ∧ IsClosed s) id :=
  closed_nhds_basis a

```

Note that, in every topological space, each point has a basis of open neighborhood, by definition.

```
example [TopologicalSpace X] {x : X} :
    (𝓝 x).HasBasis (fun t : Set X ↦ t ∈ 𝓝 x ∧ IsOpen t) id :=
  nhds_basis_opens' x

```

Our main goal is now to prove the basic theorem which allows extension by continuity. From Bourbaki’s general topology book, I.8.5, Theorem 1 (taking only the non-trivial implication):
Let X be a topological space, A a dense subset of X, f:A→Y a continuous mapping of A into a T3 space Y. If, for each x in X, f(y) tends to a limit in Y when y tends to x while remaining in A then there exists a continuous extension φ of f to X.
Actually Mathlib contains a more general version of the above lemma, `IsDenseInducing.continuousAt_extend`, but we’ll stick to Bourbaki’s version here.
Remember that, given `A : Set X`, `↥A` is the subtype associated to `A`, and Lean will automatically insert that funny up arrow when needed. And the (inclusion) coercion map is `(↑) : A → X`. The assumption “tends to x while remaining in A” corresponds to the pull-back filter `comap (↑) (𝓝 x)`.
Let’s first prove an auxiliary lemma, extracted to simplify the context (in particular we don’t need Y to be a topological space here).

```
theorem aux {X Y A : Type*} [TopologicalSpace X] {c : A → X}
      {f : A → Y} {x : X} {F : Filter Y}
      (h : Tendsto f (comap c (𝓝 x)) F) {V' : Set Y} (V'_in : V' ∈ F) :
    ∃ V ∈ 𝓝 x, IsOpen V ∧ c ⁻¹' V ⊆ f ⁻¹' V' := by
  sorry

```

Let’s now turn to the main proof of the extension by continuity theorem.
When Lean needs a topology on `↥A` it will automatically use the induced topology. The only relevant lemma is `nhds_induced (↑) : ∀ a : ↥A, 𝓝 a = comap (↑) (𝓝 ↑a)` (this is actually a general lemma about induced topologies).
The proof outline is:
The main assumption and the axiom of choice give a function `φ` such that `∀ x, Tendsto f (comap (↑) (𝓝 x)) (𝓝 (φ x))` (because `Y` is Hausdorff, `φ` is entirely determined, but we won’t need that until we try to prove that `φ` indeed extends `f`).
Let’s first prove `φ` is continuous. Fix any `x : X`. Since `Y` is regular, it suffices to check that for every _closed_ neighborhood `V'` of `φ x`, `φ ⁻¹' V' ∈ 𝓝 x`. The limit assumption gives (through the auxiliary lemma above) some `V ∈ 𝓝 x` such `IsOpen V ∧ (↑) ⁻¹' V ⊆ f ⁻¹' V'`. Since `V ∈ 𝓝 x`, it suffices to prove `V ⊆ φ ⁻¹' V'`, i.e. `∀ y ∈ V, φ y ∈ V'`. Let’s fix `y` in `V`. Because `V` is _open_ , it is a neighborhood of `y`. In particular `(↑) ⁻¹' V ∈ comap (↑) (𝓝 y)` and a fortiori `f ⁻¹' V' ∈ comap (↑) (𝓝 y)`. In addition `comap (↑) (𝓝 y) ≠ ⊥` because `A` is dense. Because we know `Tendsto f (comap (↑) (𝓝 y)) (𝓝 (φ y))` this implies `φ y ∈ closure V'` and, since `V'` is closed, we have proved `φ y ∈ V'`.
It remains to prove that `φ` extends `f`. This is where the continuity of `f` enters the discussion, together with the fact that `Y` is Hausdorff.

```
example [TopologicalSpace X] [TopologicalSpace Y] [T3Space Y] {A : Set X}
    (hA : ∀ x, x ∈ closure A) {f : A → Y} (f_cont : Continuous f)
    (hf : ∀ x : X, ∃ c : Y, Tendsto f (comap (↑) (𝓝 x)) (𝓝 c)) :
    ∃ φ : X → Y, Continuous φ ∧ ∀ a : A, φ a = f a := by
  sorry

#check HasBasis.tendsto_right_iff

```

In addition to separation property, the main kind of assumption you can make on a topological space to bring it closer to metric spaces is countability assumption. The main one is first countability asking that every point has a countable neighborhood basis. In particular this ensures that closure of sets can be understood using sequences.

```
example [TopologicalSpace X] [FirstCountableTopology X]
      {s : Set X} {a : X} :
    a ∈ closure s ↔ ∃ u : ℕ → X, (∀ n, u n ∈ s) ∧ Tendsto u atTop (𝓝 a) :=
  mem_closure_iff_seq_limit

```

###  11.3.3. Compactness[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html#id5 "Link to this heading")
Let us now discuss how compactness is defined for topological spaces. As usual there are several ways to think about it and Mathlib goes for the filter version.
We first need to define cluster points of filters. Given a filter `F` on a topological space `X`, a point `x : X` is a cluster point of `F` if `F`, seen as a generalized set, has non-empty intersection with the generalized set of points that are close to `x`.
Then we can say that a set `s` is compact if every nonempty generalized set `F` contained in `s`, i.e. such that `F ≤ 𝓟 s`, has a cluster point in `s`.

```
variable [TopologicalSpace X]

example {F : Filter X} {x : X} : ClusterPt x F ↔ NeBot (𝓝 x ⊓ F) :=
  Iff.rfl

example {s : Set X} :
    IsCompact s ↔ ∀ (F : Filter X) [NeBot F], F ≤ 𝓟 s → ∃ a ∈ s, ClusterPt a F :=
  Iff.rfl

```

For instance if `F` is `map u atTop`, the image under `u : ℕ → X` of `atTop`, the generalized set of very large natural numbers, then the assumption `F ≤ 𝓟 s` means that `u n` belongs to `s` for `n` large enough. Saying that `x` is a cluster point of `map u atTop` says the image of very large numbers intersects the set of points that are close to `x`. In case `𝓝 x` has a countable basis, we can interpret this as saying that `u` has a subsequence converging to `x`, and we get back what compactness looks like in metric spaces.

```
example [FirstCountableTopology X] {s : Set X} {u : ℕ → X} (hs : IsCompact s)
    (hu : ∀ n, u n ∈ s) : ∃ a ∈ s, ∃ φ : ℕ → ℕ, StrictMono φ ∧ Tendsto (u ∘ φ) atTop (𝓝 a) :=
  hs.tendsto_subseq hu

```

Cluster points behave nicely with continuous functions.

```
variable [TopologicalSpace Y]

example {x : X} {F : Filter X} {G : Filter Y} (H : ClusterPt x F) {f : X → Y}
    (hfx : ContinuousAt f x) (hf : Tendsto f F G) : ClusterPt (f x) G :=
  ClusterPt.map H hfx hf

```

As an exercise, we will prove that the image of a compact set under a continuous map is compact. In addition to what we saw already, you should use `Filter.push_pull` and `NeBot.of_map`.

```
example [TopologicalSpace Y] {f : X → Y} (hf : Continuous f) {s : Set X} (hs : IsCompact s) :
    IsCompact (f '' s) := by
  intro F F_ne F_le
  have map_eq : map f (𝓟 s ⊓ comap f F) = 𝓟 (f '' s) ⊓ F := by sorry
  have Hne : (𝓟 s ⊓ comap f F).NeBot := by sorry
  have Hle : 𝓟 s ⊓ comap f F ≤ 𝓟 s := inf_le_left
  sorry

```

One can also express compactness in terms of open covers: `s` is compact if every family of open sets that cover `s` has a finite covering sub-family.

```
example {ι : Type*} {s : Set X} (hs : IsCompact s) (U : ι → Set X) (hUo : ∀ i, IsOpen (U i))
    (hsU : s ⊆ ⋃ i, U i) : ∃ t : Finset ι, s ⊆ ⋃ i ∈ t, U i :=
  hs.elim_finite_subcover U hUo hsU

```

[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C10_Linear_Algebra.html "10. Linear algebra") [Next ](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C12_Differential_Calculus.html "12. Differential Calculus")
* * *
© Copyright 2020-2025, Jeremy Avigad, Patrick Massot. Text licensed under CC BY 4.0.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 

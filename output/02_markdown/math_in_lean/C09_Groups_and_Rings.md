[ Mathematics in Lean ](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/index.html)
  * [1. Introduction](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C01_Introduction.html)
  * [2. Basics](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C02_Basics.html)
  * [3. Logic](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C03_Logic.html)
  * [4. Sets and Functions](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C04_Sets_and_Functions.html)
  * [5. Elementary Number Theory](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C05_Elementary_Number_Theory.html)
  * [6. Discrete Mathematics](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C06_Discrete_Mathematics.html)
  * [7. Structures](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html)
  * [8. Hierarchies](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C08_Hierarchies.html)
  * [](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html)
    * [](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#monoids-and-groups)
      * [9.1.1. Monoids and their morphisms](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#monoids-and-their-morphisms)
      * [9.1.2. Groups and their morphisms](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#groups-and-their-morphisms)
      * [9.1.3. Subgroups](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#subgroups)
      * [9.1.4. Concrete groups](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#concrete-groups)
      * [9.1.5. Group actions](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#group-actions)
      * [9.1.6. Quotient groups](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#quotient-groups)
    * [](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#rings)
      * [9.2.1. Rings, their units, morphisms and subrings](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#rings-their-units-morphisms-and-subrings)
      * [9.2.2. Ideals and quotients](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#ideals-and-quotients)
      * [9.2.3. Algebras and polynomials](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#algebras-and-polynomials)
  * [10. Linear algebra](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C10_Linear_Algebra.html)
  * [11. Topology](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html)
  * [12. Differential Calculus](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C12_Differential_Calculus.html)
  * [13. Integration and Measure Theory](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C13_Integration_and_Measure_Theory.html)


  * [Index](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/genindex.html)


[Mathematics in Lean](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/index.html)
  * [](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/index.html)
  * 9. Groups and Rings
  * [ View page source](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/_sources/C09_Groups_and_Rings.rst.txt)


* * *
#  9. Groups and Rings[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#groups-and-rings "Link to this heading")
We saw in [Section 2.2](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C02_Basics.html#proving-identities-in-algebraic-structures) how to reason about operations in groups and rings. Later, in [Section 7.2](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#section-algebraic-structures), we saw how to define abstract algebraic structures, such as group structures, as well as concrete instances such as the ring structure on the Gaussian integers. [Chapter 8](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C08_Hierarchies.html#hierarchies) explained how hierarchies of abstract structures are handled in Mathlib.
In this chapter we work with groups and rings in more detail. We won’t be able to cover every aspect of the treatment of these topics in Mathlib, especially since Mathlib is constantly growing. But we will provide entry points to the library and show how the essential concepts are used. There is some overlap with the discussion of [Chapter 8](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C08_Hierarchies.html#hierarchies), but here we will focus on how to use Mathlib instead of the design decisions behind the way the topics are treated. So making sense of some of the examples may require reviewing the background from [Chapter 8](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C08_Hierarchies.html#hierarchies).
##  9.1. Monoids and Groups[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#monoids-and-groups "Link to this heading")
###  9.1.1. Monoids and their morphisms[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#monoids-and-their-morphisms "Link to this heading")
Courses in abstract algebra often start with groups and then progress to rings, fields, and vector spaces. This involves some contortions when discussing multiplication on rings since the multiplication operation does not come from a group structure but many of the proofs carry over verbatim from group theory to this new setting. The most common fix, when doing mathematics with pen and paper, is to leave those proofs as exercises. A less efficient but safer and more formalization-friendly way of proceeding is to use monoids. A _monoid_ structure on a type M is an internal composition law that is associative and has a neutral element. Monoids are used primarily to accommodate both groups and the multiplicative structure of rings. But there are also a number of natural examples; for instance, the set of natural numbers equipped with addition forms a monoid.
From a practical point of view, you can mostly ignore monoids when using Mathlib. But you need to know they exist when you are looking for a lemma by browsing Mathlib files. Otherwise, you might end up looking for a statement in the group theory files when it is actually in the found with monoids because it does not require elements to be invertible.
The type of monoid structures on a type `M` is written `Monoid M`. The function `Monoid` is a type class so it will almost always appear as an instance implicit argument (in other words, in square brackets). By default, `Monoid` uses multiplicative notation for the operation; for additive notation use `AddMonoid` instead. The commutative versions of these structures add the prefix `Comm` before `Monoid`.

```
example {M : Type*} [Monoid M] (x : M) : x * 1 = x := mul_one x

example {M : Type*} [AddCommMonoid M] (x y : M) : x + y = y + x := add_comm x y

```

Note that although `AddMonoid` is found in the library, it is generally confusing to use additive notation with a non-commutative operation.
The type of morphisms between monoids `M` and `N` is called `MonoidHom M N` and written `M →* N`. Lean will automatically see such a morphism as a function from `M` to `N` when we apply it to elements of `M`. The additive version is called `AddMonoidHom` and written `M →+ N`.

```
example {M N : Type*} [Monoid M] [Monoid N] (x y : M) (f : M →* N) : f (x * y) = f x * f y :=
  f.map_mul x y

example {M N : Type*} [AddMonoid M] [AddMonoid N] (f : M →+ N) : f 0 = 0 :=
  f.map_zero

```

These morphisms are bundled maps, i.e. they package together a map and some of its properties. Remember that [Section 8.2](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C08_Hierarchies.html#section-hierarchies-morphisms) explains bundled maps; here we simply note the slightly unfortunate consequence that we cannot use ordinary function composition to compose maps. Instead, we need to use `MonoidHom.comp` and `AddMonoidHom.comp`.

```
example {M N P : Type*} [AddMonoid M] [AddMonoid N] [AddMonoid P]
    (f : M →+ N) (g : N →+ P) : M →+ P := g.comp f

```

###  9.1.2. Groups and their morphisms[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#groups-and-their-morphisms "Link to this heading")
We will have much more to say about groups, which are monoids with the extra property that every element has an inverse.

```
example {G : Type*} [Group G] (x : G) : x * x⁻¹ = 1 := mul_inv_cancel x

```

Similar to the `ring` tactic that we saw earlier, there is a `group` tactic that proves any identity that holds in any group. (Equivalently, it proves the identities that hold in free groups.)

```
example {G : Type*} [Group G] (x y z : G) : x * (y * z) * (x * z)⁻¹ * (x * y * x⁻¹)⁻¹ = 1 := by
  group

```

There is also a tactic for identities in commutative additive groups called `abel`.

```
example {G : Type*} [AddCommGroup G] (x y z : G) : z + x + (y - z - x) = y := by
  abel

```

Interestingly, a group morphism is nothing more than a monoid morphism between groups. So we can copy and paste one of our earlier examples, replacing `Monoid` with `Group`.

```
example {G H : Type*} [Group G] [Group H] (x y : G) (f : G →* H) : f (x * y) = f x * f y :=
  f.map_mul x y

```

Of course we do get some new properties, such as this one:

```
example {G H : Type*} [Group G] [Group H] (x : G) (f : G →* H) : f (x⁻¹) = (f x)⁻¹ :=
  f.map_inv x

```

You may be worried that constructing group morphisms will require us to do unnecessary work since the definition of monoid morphism enforces that neutral elements are sent to neutral elements while this is automatic in the case of group morphisms. In practice the extra work is not hard, but, to avoid it, there is a function building a group morphism from a function between groups that is compatible with the composition laws.

```
example {G H : Type*} [Group G] [Group H] (f : G → H) (h : ∀ x y, f (x * y) = f x * f y) :
    G →* H :=
  MonoidHom.mk' f h

```

There is also a type `MulEquiv` of group (or monoid) isomorphisms denoted by `≃*` (and `AddEquiv` denoted by `≃+` in additive notation). The inverse of `f : G ≃* H` is `MulEquiv.symm f : H ≃* G`, composition of `f` and `g` is `MulEquiv.trans f g`, and the identity isomorphism of `G` is `M̀ulEquiv.refl G`. Using anonymous projector notation, the first two can be written `f.symm` and `f.trans g` respectively. Elements of this type are automatically coerced to morphisms and functions when necessary.

```
example {G H : Type*} [Group G] [Group H] (f : G ≃* H) :
    f.trans f.symm = MulEquiv.refl G :=
  f.self_trans_symm

```

One can use `MulEquiv.ofBijective` to build an isomorphism from a bijective morphism. Doing so makes the inverse function noncomputable.

```
noncomputable example {G H : Type*} [Group G] [Group H]
    (f : G →* H) (h : Function.Bijective f) :
    G ≃* H :=
  MulEquiv.ofBijective f h

```

###  9.1.3. Subgroups[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#subgroups "Link to this heading")
Just as group morphisms are bundled, a subgroup of `G` is also a bundled structure consisting of a set in `G` with the relevant closure properties.

```
example {G : Type*} [Group G] (H : Subgroup G) {x y : G} (hx : x ∈ H) (hy : y ∈ H) :
    x * y ∈ H :=
  H.mul_mem hx hy

example {G : Type*} [Group G] (H : Subgroup G) {x : G} (hx : x ∈ H) :
    x⁻¹ ∈ H :=
  H.inv_mem hx

```

In the example above, it is important to understand that `Subgroup G` is the type of subgroups of `G`, rather than a predicate `IsSubgroup H` where `H` is an element of `Set G`. `Subgroup G` is endowed with a coercion to `Set G` and a membership predicate on `G`. See [Section 8.3](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C08_Hierarchies.html#section-hierarchies-subobjects) for an explanation of how and why this is done.
Of course, two subgroups are the same if and only if they have the same elements. This fact is registered for use with the `ext` tactic, which can be used to prove two subgroups are equal in the same way it is used to prove that two sets are equal.
To state and prove, for example, that `ℤ` is an additive subgroup of `ℚ`, what we really want is to construct a term of type `AddSubgroup ℚ` whose projection to `Set ℚ` is `ℤ`, or, more precisely, the image of `ℤ` in `ℚ`.

```
example : AddSubgroup ℚ where
  carrier := Set.range ((↑) : ℤ → ℚ)
  add_mem' := by
    rintro _ _ ⟨n, rfl⟩ ⟨m, rfl⟩
    use n + m
    simp
  zero_mem' := by
    use 0
    simp
  neg_mem' := by
    rintro _ ⟨n, rfl⟩
    use -n
    simp

```

Using type classes, Mathlib knows that a subgroup of a group inherits a group structure.

```
example {G : Type*} [Group G] (H : Subgroup G) : Group H := inferInstance

```

This example is subtle. The object `H` is not a type, but Lean automatically coerces it to a type by interpreting it as a subtype of `G`. So the above example can be restated more explicitly as:

```
example {G : Type*} [Group G] (H : Subgroup G) : Group {x : G // x ∈ H} := inferInstance

```

An important benefit of having a type `Subgroup G` instead of a predicate `IsSubgroup : Set G → Prop` is that one can easily endow `Subgroup G` with additional structure. Importantly, it has the structure of a complete lattice structure with respect to inclusion. For instance, instead of having a lemma stating that an intersection of two subgroups of `G` is again a subgroup, we have used the lattice operation `⊓` to construct the intersection. We can then apply arbitrary lemmas about lattices to the construction.
Let us check that the set underlying the infimum of two subgroups is indeed, by definition, their intersection.

```
example {G : Type*} [Group G] (H H' : Subgroup G) :
    ((H ⊓ H' : Subgroup G) : Set G) = (H : Set G) ∩ (H' : Set G) := rfl

```

It may look strange to have a different notation for what amounts to the intersection of the underlying sets, but the correspondence does not carry over to the supremum operation and set union, since a union of subgroups is not, in general, a subgroup. Instead one needs to use the subgroup generated by the union, which is done using `Subgroup.closure`.

```
example {G : Type*} [Group G] (H H' : Subgroup G) :
    ((H ⊔ H' : Subgroup G) : Set G) = Subgroup.closure ((H : Set G) ∪ (H' : Set G)) := by
  rw [Subgroup.sup_eq_closure]

```

Another subtlety is that `G` itself does not have type `Subgroup G`, so we need a way to talk about `G` seen as a subgroup of `G`. This is also provided by the lattice structure: the full subgroup is the top element of this lattice.

```
example {G : Type*} [Group G] (x : G) : x ∈ (⊤ : Subgroup G) := trivial

```

Similarly the bottom element of this lattice is the subgroup whose only element is the neutral element.

```
example {G : Type*} [Group G] (x : G) : x ∈ (⊥ : Subgroup G) ↔ x = 1 := Subgroup.mem_bot

```

As an exercise in manipulating groups and subgroups, you can define the conjugate of a subgroup by an element of the ambient group.

```
def conjugate {G : Type*} [Group G] (x : G) (H : Subgroup G) : Subgroup G where
  carrier := {a : G | ∃ h, h ∈ H ∧ a = x * h * x⁻¹}
  one_mem' := by
    dsimp
    sorry
  inv_mem' := by
    dsimp
    sorry
  mul_mem' := by
    dsimp
    sorry

```

Tying the previous two topics together, one can push forward and pull back subgroups using group morphisms. The naming convention in Mathlib is to call those operations `map` and `comap`. These are not the common mathematical terms, but they have the advantage of being shorter than “pushforward” and “direct image.”

```
example {G H : Type*} [Group G] [Group H] (G' : Subgroup G) (f : G →* H) : Subgroup H :=
  Subgroup.map f G'

example {G H : Type*} [Group G] [Group H] (H' : Subgroup H) (f : G →* H) : Subgroup G :=
  Subgroup.comap f H'

#check Subgroup.mem_map
#check Subgroup.mem_comap

```

In particular, the preimage of the bottom subgroup under a morphism `f` is a subgroup called the _kernel_ of `f`, and the range of `f` is also a subgroup.

```
example {G H : Type*} [Group G] [Group H] (f : G →* H) (g : G) :
    g ∈ MonoidHom.ker f ↔ f g = 1 :=
  f.mem_ker

example {G H : Type*} [Group G] [Group H] (f : G →* H) (h : H) :
    h ∈ MonoidHom.range f ↔ ∃ g : G, f g = h :=
  f.mem_range

```

As exercises in manipulating group morphisms and subgroups, let us prove some elementary properties. They are already proved in Mathlib, so do not use `exact?` too quickly if you want to benefit from these exercises.

```
section exercises
variable {G H : Type*} [Group G] [Group H]

open Subgroup

example (φ : G →* H) (S T : Subgroup H) (hST : S ≤ T) : comap φ S ≤ comap φ T := by
  sorry

example (φ : G →* H) (S T : Subgroup G) (hST : S ≤ T) : map φ S ≤ map φ T := by
  sorry

variable {K : Type*} [Group K]

-- Remember you can use the `ext` tactic to prove an equality of subgroups.
example (φ : G →* H) (ψ : H →* K) (U : Subgroup K) :
    comap (ψ.comp φ) U = comap φ (comap ψ U) := by
  sorry

-- Pushing a subgroup along one homomorphism and then another is equal to
-- pushing it forward along the composite of the homomorphisms.
example (φ : G →* H) (ψ : H →* K) (S : Subgroup G) :
    map (ψ.comp φ) S = map ψ (S.map φ) := by
  sorry

end exercises

```

Let us finish this introduction to subgroups in Mathlib with two very classical results. Lagrange theorem states the cardinality of a subgroup of a finite group divides the cardinality of the group. Sylow’s first theorem is a famous partial converse to Lagrange’s theorem.
While this corner of Mathlib is partly set up to allow computation, we can tell Lean to use nonconstructive logic anyway using the following `open scoped` command.

```
open scoped Classical


example {G : Type*} [Group G] (G' : Subgroup G) : Nat.card G' ∣ Nat.card G :=
  ⟨G'.index, mul_comm G'.index _ ▸ G'.index_mul_card.symm⟩

open Subgroup

example {G : Type*} [Group G] [Finite G] (p : ℕ) {n : ℕ} [Fact p.Prime]
    (hdvd : p ^ n ∣ Nat.card G) : ∃ K : Subgroup G, Nat.card K = p ^ n :=
  Sylow.exists_subgroup_card_pow_prime p hdvd

```

The next two exercises derive a corollary of Lagrange’s lemma. (This is also already in Mathlib, so do not use `exact?` too quickly.)

```
lemma eq_bot_iff_card {G : Type*} [Group G] {H : Subgroup G} :
    H = ⊥ ↔ Nat.card H = 1 := by
  suffices (∀ x ∈ H, x = 1) ↔ ∃ x ∈ H, ∀ a ∈ H, a = x by
    simpa [eq_bot_iff_forall, Nat.card_eq_one_iff_exists]
  sorry

#check card_dvd_of_le

lemma inf_bot_of_coprime {G : Type*} [Group G] (H K : Subgroup G)
    (h : (Nat.card H).Coprime (Nat.card K)) : H ⊓ K = ⊥ := by
  sorry

```

###  9.1.4. Concrete groups[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#concrete-groups "Link to this heading")
One can also manipulate concrete groups in Mathlib, although this is typically more complicated than working with the abstract theory. For instance, given any type `X`, the group of permutations of `X` is `Equiv.Perm X`. In particular the symmetric group Sn is `Equiv.Perm (Fin n)`. One can state abstract results about this group, for instance saying that `Equiv.Perm X` is generated by cycles if `X` is finite.

```
open Equiv

example {X : Type*} [Finite X] : Subgroup.closure {σ : Perm X | Perm.IsCycle σ} = ⊤ :=
  Perm.closure_isCycle

```

One can be fully concrete and compute actual products of cycles. Below we use the `#simp` command, which calls the `simp` tactic on a given expression. The notation `c[]` is used to define a cyclic permutation. In the example, the result is a permutation of `ℕ`. One could use a type ascription such as `(1 : Fin 5)` on the first number appearing to make it a computation in `Perm (Fin 5)`.

```
#simp [mul_assoc] c[1, 2, 3] * c[2, 3, 4]

```

Another way to work with concrete groups is to use free groups and group presentations. The free group on a type `α` is `FreeGroup α` and the inclusion map is `FreeGroup.of : α → FreeGroup α`. For instance let us define a type `S` with three elements denoted by `a`, `b` and `c`, and the element `ab⁻¹` of the corresponding free group.

```
section FreeGroup

inductive S | a | b | c

open S

def myElement : FreeGroup S := (.of a) * (.of b)⁻¹

```

Note that we gave the expected type of the definition so that Lean knows that `.of` means `FreeGroup.of`.
The universal property of free groups is embodied as the equivalence `FreeGroup.lift`. For example, let us define the group morphism from `FreeGroup S` to `Perm (Fin 5)` that sends `a` to `c[1, 2, 3]`, `b` to `c[2, 3, 1]`, and `c` to `c[2, 3]`,

```
def myMorphism : FreeGroup S →* Perm (Fin 5) :=
  FreeGroup.lift fun | .a => c[1, 2, 3]
                     | .b => c[2, 3, 1]
                     | .c => c[2, 3]

```

As a last concrete example, let us see how to define a group generated by a single element whose cube is one (so that group will be isomorphic to Z/3) and build a morphism from that group to `Perm (Fin 5)`.
As a type with exactly one element, we will use `Unit` whose only element is denoted by `()`. The function `PresentedGroup` takes a set of relations, i.e. a set of elements of some free group, and returns a group that is this free group quotiented by a normal subgroup generated by relations. (We will see how to handle more general quotients in [Section 9.1.6](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#quotient-groups).) Since we somehow hide this behind a definition, we use `deriving Group` to force creation of a group instance on `myGroup`.

```
def myGroup := PresentedGroup {.of () ^ 3} deriving Group

```

The universal property of presented groups ensures that morphisms out of this group can be built from functions that send the relations to the neutral element of the target group. So we need such a function and a proof that the condition holds. Then we can feed this proof to `PresentedGroup.toGroup` to get the desired group morphism.

```
def myMap : Unit → Perm (Fin 5)
| () => c[1, 2, 3]

lemma compat_myMap :
    ∀ r ∈ ({.of () ^ 3} : Set (FreeGroup Unit)), FreeGroup.lift myMap r = 1 := by
  rintro _ rfl
  simp
  decide

def myNewMorphism : myGroup →* Perm (Fin 5) := PresentedGroup.toGroup compat_myMap

end FreeGroup

```

###  9.1.5. Group actions[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#group-actions "Link to this heading")
One important way that group theory interacts with the rest of mathematics is through the use of group actions. An action of a group `G` on some type `X` is nothing more than a morphism from `G` to `Equiv.Perm X`. So in a sense group actions are already covered by the previous discussion. But we don’t want to carry this morphism around; instead, we want it to be inferred automatically by Lean as much as possible. So we have a type class for this, which is `MulAction G X`. The downside of this setup is that having multiple actions of the same group on the same type requires some contortions, such as defining type synonyms, each of which carries different type class instances.
This allows us in particular to use `g • x` to denote the action of a group element `g` on a point `x`.

```
noncomputable section GroupActions

example {G X : Type*} [Group G] [MulAction G X] (g g': G) (x : X) :
    g • (g' • x) = (g * g') • x :=
  (mul_smul g g' x).symm

```

There is also a version for additive group called `AddAction`, where the action is denoted by `+ᵥ`. This is used for instance in the definition of affine spaces.

```
example {G X : Type*} [AddGroup G] [AddAction G X] (g g' : G) (x : X) :
    g +ᵥ (g' +ᵥ x) = (g + g') +ᵥ x :=
  (add_vadd g g' x).symm

```

The underlying group morphism is called `MulAction.toPermHom`.

```
open MulAction

example {G X : Type*} [Group G] [MulAction G X] : G →* Equiv.Perm X :=
  toPermHom G X

```

As an illustration let us see how to define the Cayley isomorphism embedding of any group `G` into a permutation group, namely `Perm G`.

```
def CayleyIsoMorphism (G : Type*) [Group G] : G ≃* (toPermHom G G).range :=
  Equiv.Perm.subgroupOfMulAction G G

```

Note that nothing before the above definition required having a group rather than a monoid (or any type endowed with a multiplication operation really).
The group condition really enters the picture when we will want to partition `X` into orbits. The corresponding equivalence relation on `X` is called `MulAction.orbitRel`. It is not declared as a global instance.

```
example {G X : Type*} [Group G] [MulAction G X] : Setoid X := orbitRel G X

```

Using this we can state that `X` is partitioned into orbits under the action of `G`. More precisely, we get a bijection between `X` and the dependent product `(ω : orbitRel.Quotient G X) × (orbit G (Quotient.out' ω))` where `Quotient.out' ω` simply chooses an element that projects to `ω`. Recall that elements of this dependent product are pairs `⟨ω, x⟩` where the type `orbit G (Quotient.out' ω)` of `x` depends on `ω`.

```
example {G X : Type*} [Group G] [MulAction G X] :
    X ≃ (ω : orbitRel.Quotient G X) × (orbit G (Quotient.out ω)) :=
  MulAction.selfEquivSigmaOrbits G X

```

In particular, when X is finite, this can be combined with `Fintype.card_congr` and `Fintype.card_sigma` to deduce that the cardinality of `X` is the sum of the cardinalities of the orbits. Furthermore, the orbits are in bijection with the quotient of `G` under the action of the stabilizers by left translation. This action of a subgroup by left-translation is used to define quotients of a group by a subgroup with notation / so we can use the following concise statement.

```
example {G X : Type*} [Group G] [MulAction G X] (x : X) :
    orbit G x ≃ G ⧸ stabilizer G x :=
  MulAction.orbitEquivQuotientStabilizer G x

```

An important special case of combining the above two results is when `X` is a group `G` equipped with the action of a subgroup `H` by translation. In this case all stabilizers are trivial so every orbit is in bijection with `H` and we get:

```
example {G : Type*} [Group G] (H : Subgroup G) : G ≃ (G ⧸ H) × H :=
  groupEquivQuotientProdSubgroup

```

This is the conceptual variant of the version of Lagrange theorem that we saw above. Note this version makes no finiteness assumption.
As an exercise for this section, let us build the action of a group on its subgroup by conjugation, using our definition of `conjugate` from a previous exercise.

```
variable {G : Type*} [Group G]

lemma conjugate_one (H : Subgroup G) : conjugate 1 H = H := by
  sorry

instance : MulAction G (Subgroup G) where
  smul := conjugate
  one_smul := by
    sorry
  mul_smul := by
    sorry

end GroupActions

```

###  9.1.6. Quotient groups[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#quotient-groups "Link to this heading")
In the above discussion of subgroups acting on groups, we saw the quotient `G ⧸ H` appear. In general this is only a type. It can be endowed with a group structure such that the quotient map is a group morphism if and only if `H` is a normal subgroup (and this group structure is then unique).
The normality assumption is a type class `Subgroup.Normal` so that type class inference can use it to derive the group structure on the quotient.

```
noncomputable section QuotientGroup

example {G : Type*} [Group G] (H : Subgroup G) [H.Normal] : Group (G ⧸ H) := inferInstance

example {G : Type*} [Group G] (H : Subgroup G) [H.Normal] : G →* G ⧸ H :=
  QuotientGroup.mk' H

```

The universal property of quotient groups is accessed through `QuotientGroup.lift`: a group morphism `φ` descends to `G ⧸ N` as soon as its kernel contains `N`.

```
example {G : Type*} [Group G] (N : Subgroup G) [N.Normal] {M : Type*}
    [Group M] (φ : G →* M) (h : N ≤ MonoidHom.ker φ) : G ⧸ N →* M :=
  QuotientGroup.lift N φ h

```

The fact that the target group is called `M` is the above snippet is a clue that having a monoid structure on `M` would be enough.
An important special case is when `N = ker φ`. In that case the descended morphism is injective and we get a group isomorphism onto its image. This result is often called the first isomorphism theorem.

```
example {G : Type*} [Group G] {M : Type*} [Group M] (φ : G →* M) :
    G ⧸ MonoidHom.ker φ →* MonoidHom.range φ :=
  QuotientGroup.quotientKerEquivRange φ

```

Applying the universal property to a composition of a morphism `φ : G →* G'` with a quotient group projection `Quotient.mk' N'`, we can also aim for a morphism from `G ⧸ N` to `G' ⧸ N'`. The condition required on `φ` is usually formulated by saying “`φ` should send `N` inside `N'`.” But this is equivalent to asking that `φ` should pull `N'` back over `N`, and the latter condition is nicer to work with since the definition of pullback does not involve an existential quantifier.

```
example {G G': Type*} [Group G] [Group G']
    {N : Subgroup G} [N.Normal] {N' : Subgroup G'} [N'.Normal]
    {φ : G →* G'} (h : N ≤ Subgroup.comap φ N') : G ⧸ N →* G' ⧸ N':=
  QuotientGroup.map N N' φ h

```

One subtle point to keep in mind is that the type `G ⧸ N` really depends on `N` (up to definitional equality), so having a proof that two normal subgroups `N` and `M` are equal is not enough to make the corresponding quotients equal. However the universal properties does give an isomorphism in this case.

```
example {G : Type*} [Group G] {M N : Subgroup G} [M.Normal]
    [N.Normal] (h : M = N) : G ⧸ M ≃* G ⧸ N := QuotientGroup.quotientMulEquivOfEq h

```

As a final series of exercises for this section, we will prove that if `H` and `K` are disjoint normal subgroups of a finite group `G` such that the product of their cardinalities is equal to the cardinality of `G` then `G` is isomorphic to `H × K`. Recall that disjoint in this context means `H ⊓ K = ⊥`.
We start with playing a bit with Lagrange’s lemma, without assuming the subgroups are normal or disjoint.

```
section
variable {G : Type*} [Group G] {H K : Subgroup G}

open MonoidHom

#check Nat.card_pos -- The nonempty argument will be automatically inferred for subgroups
#check Subgroup.index_eq_card
#check Subgroup.index_mul_card
#check Nat.eq_of_mul_eq_mul_right

lemma aux_card_eq [Finite G] (h' : Nat.card G = Nat.card H * Nat.card K) :
    Nat.card (G ⧸ H) = Nat.card K := by
  sorry

```

From now on, we assume that our subgroups are normal and disjoint, and we assume the cardinality condition. Now we construct the first building block of the desired isomorphism.

```
variable [H.Normal] [K.Normal] [Fintype G] (h : Disjoint H K)
  (h' : Nat.card G = Nat.card H * Nat.card K)

#check Nat.bijective_iff_injective_and_card
#check ker_eq_bot_iff
#check restrict
#check ker_restrict

def iso₁ : K ≃* G ⧸ H := by
  sorry

```

Now we can define our second building block. We will need `MonoidHom.prod`, which builds a morphism from `G₀` to `G₁ × G₂` out of morphisms from `G₀` to `G₁` and `G₂`.

```
def iso₂ : G ≃* (G ⧸ K) × (G ⧸ H) := by
  sorry

```

We are ready to put all pieces together.

```
#check MulEquiv.prodCongr

def finalIso : G ≃* H × K :=
  sorry

```

##  9.2. Rings[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#rings "Link to this heading")
###  9.2.1. Rings, their units, morphisms and subrings[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#rings-their-units-morphisms-and-subrings "Link to this heading")
The type of ring structures on a type `R` is `Ring R`. The variant where multiplication is assumed to be commutative is `CommRing R`. We have already seen that the `ring` tactic will prove any equality that follows from the axioms of a commutative ring.

```
example {R : Type*} [CommRing R] (x y : R) : (x + y) ^ 2 = x ^ 2 + y ^ 2 + 2 * x * y := by ring

```

More exotic variants do not require that the addition on `R` forms a group but only an additive monoid. The corresponding type classes are `Semiring R` and `CommSemiring R`. The type of natural numbers is an important instance of `CommSemiring R`, as is any type of functions taking values in the natural numbers. Another important example is the type of ideals in a ring, which will be discussed below. The name of the `ring` tactic is doubly misleading, since it assumes commutativity but works in semirings as well. In other words, it applies to any `CommSemiring`.

```
example (x y : ℕ) : (x + y) ^ 2 = x ^ 2 + y ^ 2 + 2 * x * y := by ring

```

There are also versions of the ring and semiring classes that do not assume the existence of a multiplicative unit or the associativity of multiplication. We will not discuss those here.
Some concepts that are traditionally taught in an introduction to ring theory are actually about the underlying multiplicative monoid. A prominent example is the definition of the units of a ring. Every (multiplicative) monoid `M` has a predicate `IsUnit : M → Prop` asserting existence of a two-sided inverse, a type `Units M` of units with notation `Mˣ`, and a coercion to `M`. The type `Units M` bundles an invertible element with its inverse as well as properties than ensure that each is indeed the inverse of the other. This implementation detail is relevant mainly when defining computable functions. In most situations one can use `IsUnit.unit {x : M} : IsUnit x → Mˣ` to build a unit. In the commutative case, one also has `Units.mkOfMulEqOne (x y : M) : x * y = 1 → Mˣ` which builds `x` seen as unit.

```
example (x : ℤˣ) : x = 1 ∨ x = -1 := Int.units_eq_one_or x

example {M : Type*} [Monoid M] (x : Mˣ) : (x : M) * x⁻¹ = 1 := Units.mul_inv x

example {M : Type*} [Monoid M] : Group Mˣ := inferInstance

```

The type of ring morphisms between two (semi)-rings `R` and `S` is `RingHom R S`, with notation `R →+* S`.

```
example {R S : Type*} [Ring R] [Ring S] (f : R →+* S) (x y : R) :
    f (x + y) = f x + f y := f.map_add x y

example {R S : Type*} [Ring R] [Ring S] (f : R →+* S) : Rˣ →* Sˣ :=
  Units.map f

```

The isomorphism variant is `RingEquiv`, with notation `≃+*`.
As with submonoids and subgroups, there is a `Subring R` type for subrings of a ring `R`, but this type is a lot less useful than the type of subgroups since one cannot quotient a ring by a subring.

```
example {R : Type*} [Ring R] (S : Subring R) : Ring S := inferInstance

```

Also notice that `RingHom.range` produces a subring.
###  9.2.2. Ideals and quotients[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#ideals-and-quotients "Link to this heading")
For historical reasons, Mathlib only has a theory of ideals for commutative rings. (The ring library was originally developed to make quick progress toward the foundations of modern algebraic geometry.) So in this section we will work with commutative (semi)rings. Ideals of `R` are defined as submodules of `R` seen as `R`-modules. Modules will be covered later in a chapter on linear algebra, but this implementation detail can mostly be safely ignored since most (but not all) relevant lemmas are restated in the special context of ideals. But anonymous projection notation won’t always work as expected. For instance, one cannot replace `Ideal.Quotient.mk I` by `I.Quotient.mk` in the snippet below because there are two `.`s and so it will parse as `(Ideal.Quotient I).mk`; but `Ideal.Quotient` by itself doesn’t exist.

```
example {R : Type*} [CommRing R] (I : Ideal R) : R →+* R ⧸ I :=
  Ideal.Quotient.mk I

example {R : Type*} [CommRing R] {a : R} {I : Ideal R} :
    Ideal.Quotient.mk I a = 0 ↔ a ∈ I :=
  Ideal.Quotient.eq_zero_iff_mem

```

The universal property of quotient rings is `Ideal.Quotient.lift`.

```
example {R S : Type*} [CommRing R] [CommRing S] (I : Ideal R) (f : R →+* S)
    (H : I ≤ RingHom.ker f) : R ⧸ I →+* S :=
  Ideal.Quotient.lift I f H

```

In particular it leads to the first isomorphism theorem for rings.

```
example {R S : Type*} [CommRing R] [CommRing S](f : R →+* S) :
    R ⧸ RingHom.ker f ≃+* f.range :=
  RingHom.quotientKerEquivRange f

```

Ideals form a complete lattice structure with the inclusion relation, as well as a semiring structure. These two structures interact nicely.

```
variable {R : Type*} [CommRing R] {I J : Ideal R}

example : I + J = I ⊔ J := rfl

example {x : R} : x ∈ I + J ↔ ∃ a ∈ I, ∃ b ∈ J, a + b = x := by
  simp [Submodule.mem_sup]

example : I * J ≤ J := Ideal.mul_le_left

example : I * J ≤ I := Ideal.mul_le_right

example : I * J ≤ I ⊓ J := Ideal.mul_le_inf

```

One can use ring morphisms to push ideals forward and pull them back using `Ideal.map` and `Ideal.comap`, respectively. As usual, the latter is more convenient to use since it does not involve an existential quantifier. This explains why it is used to state the condition that allows us to build morphisms between quotient rings.

```
example {R S : Type*} [CommRing R] [CommRing S] (I : Ideal R) (J : Ideal S) (f : R →+* S)
    (H : I ≤ Ideal.comap f J) : R ⧸ I →+* S ⧸ J :=
  Ideal.quotientMap J f H

```

One subtle point is that the type `R ⧸ I` really depends on `I` (up to definitional equality), so having a proof that two ideals `I` and `J` are equal is not enough to make the corresponding quotients equal. However, the universal properties do provide an isomorphism in this case.

```
example {R : Type*} [CommRing R] {I J : Ideal R} (h : I = J) : R ⧸ I ≃+* R ⧸ J :=
  Ideal.quotEquivOfEq h

```

We can now present the Chinese remainder isomorphism as an example. Pay attention to the difference between the indexed infimum symbol `⨅` and the big product of types symbol `Π`. Depending on your font, those can be pretty hard to distinguish.

```
example {R : Type*} [CommRing R] {ι : Type*} [Fintype ι] (f : ι → Ideal R)
    (hf : ∀ i j, i ≠ j → IsCoprime (f i) (f j)) : (R ⧸ ⨅ i, f i) ≃+* Π i, R ⧸ f i :=
  Ideal.quotientInfRingEquivPiQuotient f hf

```

The elementary version of the Chinese remainder theorem, a statement about `ZMod`, can be easily deduced from the previous one:

```
open BigOperators PiNotation

example {ι : Type*} [Fintype ι] (a : ι → ℕ) (coprime : ∀ i j, i ≠ j → (a i).Coprime (a j)) :
    ZMod (∏ i, a i) ≃+* Π i, ZMod (a i) :=
  ZMod.prodEquivPi a coprime

```

As a series of exercises, we will reprove the Chinese remainder theorem in the general case.
We first need to define the map appearing in the theorem, as a ring morphism, using the universal property of quotient rings.

```
variable {ι R : Type*} [CommRing R]
open Ideal Quotient Function

#check Pi.ringHom
#check ker_Pi_Quotient_mk

/-- The homomorphism from ``R ⧸ ⨅ i, I i`` to ``Π i, R ⧸ I i`` featured in the Chinese
  Remainder Theorem. -/
def chineseMap (I : ι → Ideal R) : (R ⧸ ⨅ i, I i) →+* Π i, R ⧸ I i :=
  sorry

```

Make sure the following next two lemmas can be proven by `rfl`.

```
lemma chineseMap_mk (I : ι → Ideal R) (x : R) :
    chineseMap I (Quotient.mk _ x) = fun i : ι ↦ Ideal.Quotient.mk (I i) x :=
  sorry

lemma chineseMap_mk' (I : ι → Ideal R) (x : R) (i : ι) :
    chineseMap I (mk _ x) i = mk (I i) x :=
  sorry

```

The next lemma proves the easy half of the Chinese remainder theorem, without any assumption on the family of ideals. The proof is less than one line long.

```
#check injective_lift_iff

lemma chineseMap_inj (I : ι → Ideal R) : Injective (chineseMap I) := by
  sorry

```

We are now ready for the heart of the theorem, which will show the surjectivity of our `chineseMap`. First we need to know the different ways one can express the coprimality (also called co-maximality assumption). Only the first two will be needed below.

```
#check IsCoprime
#check isCoprime_iff_add
#check isCoprime_iff_exists
#check isCoprime_iff_sup_eq
#check isCoprime_iff_codisjoint

```

We take the opportunity to use induction on `Finset`. Relevant lemmas on `Finset` are given below. Remember that the `ring` tactic works for semirings and that the ideals of a ring form a semiring.

```
#check Finset.mem_insert_of_mem
#check Finset.mem_insert_self

theorem isCoprime_Inf {I : Ideal R} {J : ι → Ideal R} {s : Finset ι}
    (hf : ∀ j ∈ s, IsCoprime I (J j)) : IsCoprime I (⨅ j ∈ s, J j) := by
  classical
  simp_rw [isCoprime_iff_add] at *
  induction s using Finset.induction with
  | empty =>
      simp
  | @insert i s _ hs =>
      rw [Finset.iInf_insert, inf_comm, one_eq_top, eq_top_iff, ← one_eq_top]
      set K := ⨅ j ∈ s, J j
      calc
        1 = I + K                  := sorry
        _ = I + K * (I + J i)      := sorry
        _ = (1 + K) * I + K * J i  := sorry
        _ ≤ I + K ⊓ J i            := sorry

```

We can now prove surjectivity of the map appearing in the Chinese remainder theorem.

```
lemma chineseMap_surj [Fintype ι] {I : ι → Ideal R}
    (hI : ∀ i j, i ≠ j → IsCoprime (I i) (I j)) : Surjective (chineseMap I) := by
  classical
  intro g
  choose f hf using fun i ↦ Ideal.Quotient.mk_surjective (g i)
  have key : ∀ i, ∃ e : R, mk (I i) e = 1 ∧ ∀ j, j ≠ i → mk (I j) e = 0 := by
    intro i
    have hI' : ∀ j ∈ ({i} : Finset ι)ᶜ, IsCoprime (I i) (I j) := by
      sorry
    sorry
  choose e he using key
  use mk _ (∑ i, f i * e i)
  sorry

```

Now all the pieces come together in the following:

```
noncomputable def chineseIso [Fintype ι] (f : ι → Ideal R)
    (hf : ∀ i j, i ≠ j → IsCoprime (f i) (f j)) : (R ⧸ ⨅ i, f i) ≃+* Π i, R ⧸ f i :=
  { Equiv.ofBijective _ ⟨chineseMap_inj f, chineseMap_surj hf⟩,
    chineseMap f with }

```

###  9.2.3. Algebras and polynomials[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html#algebras-and-polynomials "Link to this heading")
Given a commutative (semi)ring `R`, an _algebra over_ `R` is a semiring `A` equipped with a ring morphism whose image commutes with every element of `A`. This is encoded as a type class `Algebra R A`. The morphism from `R` to `A` is called the structure map and is denoted `algebraMap R A : R →+* A` in Lean. Multiplication of `a : A` by `algebraMap R A r` for some `r : R` is called the scalar multiplication of `a` by `r` and denoted by `r • a`. Note that this notion of algebra is sometimes called an _associative unital algebra_ to emphasize the existence of more general notions of algebra.
The fact that `algebraMap R A` is ring morphism packages together a lot of properties of scalar multiplication, such as the following:

```
example {R A : Type*} [CommRing R] [Ring A] [Algebra R A] (r r' : R) (a : A) :
    (r + r') • a = r • a + r' • a :=
  add_smul r r' a

example {R A : Type*} [CommRing R] [Ring A] [Algebra R A] (r r' : R) (a : A) :
    (r * r') • a = r • r' • a :=
  mul_smul r r' a

```

The morphisms between two `R`-algebras `A` and `B` are ring morphisms which commute with scalar multiplication by elements of `R`. They are bundled morphisms with type `AlgHom R A B`, which is denoted by `A →ₐ[R] B`.
Important examples of non-commutative algebras include algebras of endomorphisms and algebras of square matrices, both of which will be covered in the chapter on linear algebra. In this chapter we will discuss one of the most important examples of a commutative algebra, namely, polynomial algebras.
The algebra of univariate polynomials with coefficients in `R` is called `Polynomial R`, which can be written as `R[X]` as soon as one opens the `Polynomial` namespace. The algebra structure map from `R` to `R[X]` is denoted by `C`, which stands for “constant” since the corresponding polynomial functions are always constant. The indeterminate is denoted by `X`.

```
open Polynomial

example {R : Type*} [CommRing R] : R[X] := X

example {R : Type*} [CommRing R] (r : R) := X - C r

```

In the first example above, it is crucial that we give Lean the expected type since it cannot be determined from the body of the definition. In the second example, the target polynomial algebra can be inferred from our use of `C r` since the type of `r` is known.
Because `C` is a ring morphism from `R` to `R[X]`, we can use all ring morphisms lemmas such as `map_zero`, `map_one`, `map_mul`, and `map_pow` before computing in the ring `R[X]`. For example:

```
example {R : Type*} [CommRing R] (r : R) : (X + C r) * (X - C r) = X ^ 2 - C (r ^ 2) := by
  rw [C.map_pow]
  ring

```

You can access coefficients using `Polynomial.coeff`

```
example {R : Type*} [CommRing R] (r:R) : (C r).coeff 0 = r := by simp

example {R : Type*} [CommRing R] : (X ^ 2 + 2 * X + C 3 : R[X]).coeff 1 = 2 := by simp

```

Defining the degree of a polynomial is always tricky because of the special case of the zero polynomial. Mathlib has two variants: `Polynomial.natDegree : R[X] → ℕ` assigns degree `0` to the zero polynomial, and `Polynomial.degree : R[X] → WithBot ℕ` assigns `⊥`. In the latter, `WithBot ℕ` can be seen as `ℕ ∪ {-∞}`, except that `-∞` is denoted `⊥`, the same symbol as the bottom element in a complete lattice. This special value is used as the degree of the zero polynomial, and it is absorbent for addition. (It is almost absorbent for multiplication, except that `⊥ * 0 = 0`.)
Morally speaking, the `degree` version is the correct one. For instance, it allows us to state the expected formula for the degree of a product (assuming the base ring has no zero divisor).

```
example {R : Type*} [Semiring R] [NoZeroDivisors R] {p q : R[X]} :
    degree (p * q) = degree p + degree q :=
  Polynomial.degree_mul

```

Whereas the version for `natDegree` needs to assume non-zero polynomials.

```
example {R : Type*} [Semiring R] [NoZeroDivisors R] {p q : R[X]} (hp : p ≠ 0) (hq : q ≠ 0) :
    natDegree (p * q) = natDegree p + natDegree q :=
  Polynomial.natDegree_mul hp hq

```

However, `ℕ` is much nicer to use than `WithBot ℕ`, so Mathlib makes both versions available and provides lemmas to convert between them. Also, `natDegree` is the more convenient definition to use when computing the degree of a composition. Composition of polynomial is `Polynomial.comp` and we have:

```
example {R : Type*} [Semiring R] [NoZeroDivisors R] {p q : R[X]} :
    natDegree (comp p q) = natDegree p * natDegree q :=
  Polynomial.natDegree_comp

```

Polynomials give rise to polynomial functions: any polynomial can be evaluated on `R` using `Polynomial.eval`.

```
example {R : Type*} [CommRing R] (P: R[X]) (x : R) := P.eval x

example {R : Type*} [CommRing R] (r : R) : (X - C r).eval r = 0 := by simp

```

In particular, there is a predicate, `IsRoot`, that holds for elements `r` in `R` where a polynomial vanishes.

```
example {R : Type*} [CommRing R] (P : R[X]) (r : R) : IsRoot P r ↔ P.eval r = 0 := Iff.rfl

```

We would like to say that, assuming `R` has no zero divisor, a polynomial has at most as many roots as its degree, where the roots are counted with multiplicities. But once again the case of the zero polynomial is painful. So Mathlib defines `Polynomial.roots` to send a polynomial `P` to a multiset, i.e. the finite set that is defined to be empty if `P` is zero and the roots of `P`, with multiplicities, otherwise. This is defined only when the underlying ring is a domain since otherwise the definition does not have good properties.

```
example {R : Type*} [CommRing R] [IsDomain R] (r : R) : (X - C r).roots = {r} :=
  roots_X_sub_C r

example {R : Type*} [CommRing R] [IsDomain R] (r : R) (n : ℕ):
    ((X - C r) ^ n).roots = n • {r} :=
  by simp

```

Both `Polynomial.eval` and `Polynomial.roots` consider only the coefficients ring. They do not allow us to say that `X ^ 2 - 2 : ℚ[X]` has a root in `ℝ` or that `X ^ 2 + 1 : ℝ[X]` has a root in `ℂ`. For this, we need `Polynomial.aeval`, which will evaluate `P : R[X]` in any `R`-algebra. More precisely, given a semiring `A` and an instance of `Algebra R A`, `Polynomial.aeval` sends every element of `a` along the `R`-algebra morphism of evaluation at `a`. Since `AlgHom` has a coercion to functions, one can apply it to a polynomial. But `aeval` does not have a polynomial as an argument, so one cannot use dot notation like in `P.eval` above.

```
example : aeval Complex.I (X ^ 2 + 1 : ℝ[X]) = 0 := by simp

```

The function corresponding to `roots` in this context is `aroots` which takes a polynomial and then an algebra and outputs a multiset (with the same caveat about the zero polynomial as for `roots`).

```
open Complex Polynomial

example : aroots (X ^ 2 + 1 : ℝ[X]) ℂ = {Complex.I, -I} := by
  suffices roots (X ^ 2 + 1 : ℂ[X]) = {I, -I} by simpa [aroots_def]
  have factored : (X ^ 2 + 1 : ℂ[X]) = (X - C I) * (X - C (-I)) := by
    have key : (C I * C I : ℂ[X]) = -1 := by simp [← C_mul]
    rw [C_neg]
    linear_combination key
  have p_ne_zero : (X - C I) * (X - C (-I)) ≠ 0 := by
    intro H
    apply_fun eval 0 at H
    simp [eval] at H
  simp only [factored, roots_mul p_ne_zero, roots_X_sub_C]
  rfl

-- Mathlib knows about D'Alembert-Gauss theorem: ``ℂ`` is algebraically closed.
example : IsAlgClosed ℂ := inferInstance

```

More generally, given an ring morphism `f : R →+* S` one can evaluate `P : R[X]` at a point in `S` using `Polynomial.eval₂`. This one produces an actual function from `R[X]` to `S` since it does not assume the existence of a `Algebra R S` instance, so dot notation works as you would expect.

```
#check (Complex.ofRealHom : ℝ →+* ℂ)

example : (X ^ 2 + 1 : ℝ[X]).eval₂ Complex.ofRealHom Complex.I = 0 := by simp

```

Let us end by mentioning multivariate polynomials briefly. Given a commutative semiring `R`, the `R`-algebra of polynomials with coefficients in `R` and indeterminates indexed by a type `σ` is `MVPolynomial σ R`. Given `i : σ`, the corresponding polynomial is `MvPolynomial.X i`. (As usual, one can open the `MVPolynomial` namespace to shorten this to `X i`.) For instance, if we want two indeterminates we can use `Fin 2` as `σ` and write the polynomial defining the unit circle in R2‘ as:

```
open MvPolynomial

def circleEquation : MvPolynomial (Fin 2) ℝ := X 0 ^ 2 + X 1 ^ 2 - 1

```

Recall that function application has a very high precedence so the expression above is read as `(X 0) ^ 2 + (X 1) ^ 2 - 1`. We can evaluate it to make sure the point with coordinates (1,0) is on the circle. Recall the `![...]` notation denotes elements of `Fin n → X` for some natural number `n` determined by the number of arguments and some type `X` determined by the type of arguments.

```
example : MvPolynomial.eval ![1, 0] circleEquation = 0 := by simp [circleEquation]

```

[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C08_Hierarchies.html "8. Hierarchies") [Next ](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C10_Linear_Algebra.html "10. Linear algebra")
* * *
© Copyright 2020-2025, Jeremy Avigad, Patrick Massot. Text licensed under CC BY 4.0.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 

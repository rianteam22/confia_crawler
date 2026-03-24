[ Mathematics in Lean ](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/index.html)
  * [1. Introduction](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C01_Introduction.html)
  * [2. Basics](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C02_Basics.html)
  * [3. Logic](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C03_Logic.html)
  * [4. Sets and Functions](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C04_Sets_and_Functions.html)
  * [5. Elementary Number Theory](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C05_Elementary_Number_Theory.html)
  * [6. Discrete Mathematics](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C06_Discrete_Mathematics.html)
  * [](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html)
    * [7.1. Defining structures](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#defining-structures)
    * [7.2. Algebraic Structures](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#algebraic-structures)
    * [7.3. Building the Gaussian Integers](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#building-the-gaussian-integers)
  * [8. Hierarchies](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C08_Hierarchies.html)
  * [9. Groups and Rings](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C09_Groups_and_Rings.html)
  * [10. Linear algebra](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C10_Linear_Algebra.html)
  * [11. Topology](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C11_Topology.html)
  * [12. Differential Calculus](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C12_Differential_Calculus.html)
  * [13. Integration and Measure Theory](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C13_Integration_and_Measure_Theory.html)


  * [Index](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/genindex.html)


[Mathematics in Lean](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/index.html)
  * [](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/index.html)
  * 7. Structures
  * [ View page source](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/_sources/C07_Structures.rst.txt)


* * *
#  7. Structures[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#structures "Link to this heading")
Modern mathematics makes essential use of algebraic structures, which encapsulate patterns that can be instantiated in multiple settings. The subject provides various ways of defining such structures and constructing particular instances.
Lean therefore provides corresponding ways of defining structures formally and working with them. You have already seen examples of algebraic structures in Lean, such as rings and lattices, which were discussed in [Chapter 2](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C02_Basics.html#basics). This chapter will explain the mysterious square bracket annotations that you saw there, `[Ring α]` and `[Lattice α]`. It will also show you how to define and use algebraic structures on your own.
For more technical detail, you can consult [Theorem Proving in Lean](https://leanprover.github.io/theorem_proving_in_lean/), and a paper by Anne Baanen, [Use and abuse of instance parameters in the Lean mathematical library](https://arxiv.org/abs/2202.01629).
##  7.1. Defining structures[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#defining-structures "Link to this heading")
In the broadest sense of the term, a _structure_ is a specification of a collection of data, possibly with constraints that the data is required to satisfy. An _instance_ of the structure is a particular bundle of data satisfying the constraints. For example, we can specify that a point is a tuple of three real numbers:

```
@[ext]
structure Point where
  x : ℝ
  y : ℝ
  z : ℝ

```

The `@[ext]` annotation tells Lean to automatically generate theorems that can be used to prove that two instances of a structure are equal when their components are equal, a property known as _extensionality_.

```
#check Point.ext

example (a b : Point) (hx : a.x = b.x) (hy : a.y = b.y) (hz : a.z = b.z) : a = b := by
  ext
  repeat' assumption

```

We can then define particular instances of the `Point` structure. Lean provides multiple ways of doing that.

```
def myPoint1 : Point where
  x := 2
  y := -1
  z := 4

def myPoint2 : Point :=
  ⟨2, -1, 4⟩

def myPoint3 :=
  Point.mk 2 (-1) 4

```

In the first example, the fields of the structure are named explicitly. The function `Point.mk` referred to in the definition of `myPoint3` is known as the _constructor_ for the `Point` structure, because it serves to construct elements. You can specify a different name if you want, like `build`.

```
structure Point' where build ::
  x : ℝ
  y : ℝ
  z : ℝ

#check Point'.build 2 (-1) 4

```

The next two examples show how to define functions on structures. Whereas the second example makes the `Point.mk` constructor explicit, the first example uses an anonymous constructor for brevity. Lean can infer the relevant constructor from the indicated type of `add`. It is conventional to put definitions and theorems associated with a structure like `Point` in a namespace with the same name. In the example below, because we have opened the `Point` namespace, the full name of `add` is `Point.add`. When the namespace is not open, we have to use the full name. But remember that it is often convenient to use anonymous projection notation, which allows us to write `a.add b` instead of `Point.add a b`. Lean interprets the former as the latter because `a` has type `Point`.

```
namespace Point

def add (a b : Point) : Point :=
  ⟨a.x + b.x, a.y + b.y, a.z + b.z⟩

def add' (a b : Point) : Point where
  x := a.x + b.x
  y := a.y + b.y
  z := a.z + b.z

#check add myPoint1 myPoint2
#check myPoint1.add myPoint2

end Point

#check Point.add myPoint1 myPoint2
#check myPoint1.add myPoint2

```

Below we will continue to put definitions in the relevant namespace, but we will leave the namespacing commands out of the quoted snippets. To prove properties of the addition function, we can use `rw` to expand the definition and `ext` to reduce an equation between two elements of the structure to equations between the components. Below we use the `protected` keyword so that the name of the theorem is `Point.add_comm`, even when the namespace is open. This is helpful when we want to avoid ambiguity with a generic theorem like `add_comm`.

```
protected theorem add_comm (a b : Point) : add a b = add b a := by
  rw [add, add]
  ext <;> dsimp
  repeat' apply add_comm

example (a b : Point) : add a b = add b a := by simp [add, add_comm]

```

Because Lean can unfold definitions and simplify projections internally, sometimes the equations we want hold definitionally.

```
theorem add_x (a b : Point) : (a.add b).x = a.x + b.x :=
  rfl

```

It is also possible to define functions on structures using pattern matching, in a manner similar to the way we defined recursive functions in [Section 5.2](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C05_Elementary_Number_Theory.html#section-induction-and-recursion). The definitions `addAlt` and `addAlt'` below are essentially the same; the only difference is that we use anonymous constructor notation in the second. Although it is sometimes convenient to define functions this way, and structural eta-reduction makes this alternative definitionally equivalent, it can make things less convenient in later proofs. In particular, `rw [addAlt]` leaves us with a messier goal view containing a `match` statement.

```
def addAlt : Point → Point → Point
  | Point.mk x₁ y₁ z₁, Point.mk x₂ y₂ z₂ => ⟨x₁ + x₂, y₁ + y₂, z₁ + z₂⟩

def addAlt' : Point → Point → Point
  | ⟨x₁, y₁, z₁⟩, ⟨x₂, y₂, z₂⟩ => ⟨x₁ + x₂, y₁ + y₂, z₁ + z₂⟩

theorem addAlt_x (a b : Point) : (a.addAlt b).x = a.x + b.x := by
  rfl

theorem addAlt_comm (a b : Point) : addAlt a b = addAlt b a := by
  rw [addAlt, addAlt]
  -- the same proof still works, but the goal view here is harder to read
  ext <;> dsimp
  repeat' apply add_comm

```

Mathematical constructions often involve taking apart bundled information and putting it together again in different ways. It therefore makes sense that Lean and Mathlib offer so many ways of doing this efficiently. As an exercise, try proving that `Point.add` is associative. Then define scalar multiplication for a point and show that it distributes over addition.

```
protected theorem add_assoc (a b c : Point) : (a.add b).add c = a.add (b.add c) := by
  sorry

def smul (r : ℝ) (a : Point) : Point :=
  sorry

theorem smul_distrib (r : ℝ) (a b : Point) :
    (smul r a).add (smul r b) = smul r (a.add b) := by
  sorry

```

Using structures is only the first step on the road to algebraic abstraction. We don’t yet have a way to link `Point.add` to the generic `+` symbol, or to connect `Point.add_comm` and `Point.add_assoc` to the generic `add_comm` and `add_assoc` theorems. These tasks belong to the _algebraic_ aspect of using structures, and we will explain how to carry them out in the next section. For now, just think of a structure as a way of bundling together objects and information.
It is especially useful that a structure can specify not only data types but also constraints that the data must satisfy. In Lean, the latter are represented as fields of type `Prop`. For example, the _standard 2-simplex_ is defined to be the set of points (x,y,z) satisfying x≥0, y≥0, z≥0, and x+y+z=1. If you are not familiar with the notion, you should draw a picture, and convince yourself that this set is the equilateral triangle in three-space with vertices (1,0,0), (0,1,0), and (0,0,1), together with its interior. We can represent it in Lean as follows:

```
structure StandardTwoSimplex where
  x : ℝ
  y : ℝ
  z : ℝ
  x_nonneg : 0 ≤ x
  y_nonneg : 0 ≤ y
  z_nonneg : 0 ≤ z
  sum_eq : x + y + z = 1

```

Notice that the last four fields refer to `x`, `y`, and `z`, that is, the first three fields. We can define a map from the two-simplex to itself that swaps `x` and `y`:

```
def swapXy (a : StandardTwoSimplex) : StandardTwoSimplex
    where
  x := a.y
  y := a.x
  z := a.z
  x_nonneg := a.y_nonneg
  y_nonneg := a.x_nonneg
  z_nonneg := a.z_nonneg
  sum_eq := by rw [add_comm a.y a.x, a.sum_eq]

```

More interestingly, we can compute the midpoint of two points on the simplex. We have added the phrase `noncomputable section` at the beginning of this file in order to use division on the real numbers.

```
noncomputable section

def midpoint (a b : StandardTwoSimplex) : StandardTwoSimplex
    where
  x := (a.x + b.x) / 2
  y := (a.y + b.y) / 2
  z := (a.z + b.z) / 2
  x_nonneg := div_nonneg (add_nonneg a.x_nonneg b.x_nonneg) (by norm_num)
  y_nonneg := div_nonneg (add_nonneg a.y_nonneg b.y_nonneg) (by norm_num)
  z_nonneg := div_nonneg (add_nonneg a.z_nonneg b.z_nonneg) (by norm_num)
  sum_eq := by field_simp; linarith [a.sum_eq, b.sum_eq]

```

Here we have established `x_nonneg`, `y_nonneg`, and `z_nonneg` with concise proof terms, but establish `sum_eq` in tactic mode, using `by`.
Given a parameter λ satisfying 0≤λ≤1, we can take the weighted average λa+(1−λ)b of two points a and b in the standard 2-simplex. We challenge you to define that function, in analogy to the `midpoint` function above.

```
def weightedAverage (lambda : Real) (lambda_nonneg : 0 ≤ lambda) (lambda_le : lambda ≤ 1)
    (a b : StandardTwoSimplex) : StandardTwoSimplex :=
  sorry

```

Structures can depend on parameters. For example, we can generalize the standard 2-simplex to the standard n-simplex for any n. At this stage, you don’t have to know anything about the type `Fin n` except that it has n elements, and that Lean knows how to sum over it.

```
open BigOperators

structure StandardSimplex (n : ℕ) where
  V : Fin n → ℝ
  NonNeg : ∀ i : Fin n, 0 ≤ V i
  sum_eq_one : (∑ i, V i) = 1

namespace StandardSimplex

def midpoint (n : ℕ) (a b : StandardSimplex n) : StandardSimplex n
    where
  V i := (a.V i + b.V i) / 2
  NonNeg := by
    intro i
    apply div_nonneg
    · linarith [a.NonNeg i, b.NonNeg i]
    norm_num
  sum_eq_one := by
    simp [div_eq_mul_inv, ← Finset.sum_mul, Finset.sum_add_distrib,
      a.sum_eq_one, b.sum_eq_one]
    field_simp

end StandardSimplex

```

As an exercise, see if you can define the weighted average of two points in the standard n-simplex. You can use `Finset.sum_add_distrib` and `Finset.mul_sum` to manipulate the relevant sums.
We have seen that structures can be used to bundle together data and properties. Interestingly, they can also be used to bundle together properties without the data. For example, the next structure, `IsLinear`, bundles together the two components of linearity.

```
structure IsLinear (f : ℝ → ℝ) where
  is_additive : ∀ x y, f (x + y) = f x + f y
  preserves_mul : ∀ x c, f (c * x) = c * f x

section
variable (f : ℝ → ℝ) (linf : IsLinear f)

#check linf.is_additive
#check linf.preserves_mul

end

```

It is worth pointing out that structures are not the only way to bundle together data. The `Point` data structure can be defined using the generic type product, and `IsLinear` can be defined with a simple `and`.

```
def Point'' :=
  ℝ × ℝ × ℝ

def IsLinear' (f : ℝ → ℝ) :=
  (∀ x y, f (x + y) = f x + f y) ∧ ∀ x c, f (c * x) = c * f x

```

Generic type constructions can even be used in place of structures with dependencies between their components. For example, the _subtype_ construction combines a piece of data with a property. You can think of the type `PReal` in the next example as being the type of positive real numbers. Any `x : PReal` has two components: the value, and the property of being positive. You can access these components as `x.val`, which has type `ℝ`, and `x.property`, which represents the fact `0 < x.val`.

```
def PReal :=
  { y : ℝ // 0 < y }

section
variable (x : PReal)

#check x.val
#check x.property
#check x.1
#check x.2

end

```

We could have used subtypes to define the standard 2-simplex, as well as the standard n-simplex for an arbitrary n.

```
def StandardTwoSimplex' :=
  { p : ℝ × ℝ × ℝ // 0 ≤ p.1 ∧ 0 ≤ p.2.1 ∧ 0 ≤ p.2.2 ∧ p.1 + p.2.1 + p.2.2 = 1 }

def StandardSimplex' (n : ℕ) :=
  { v : Fin n → ℝ // (∀ i : Fin n, 0 ≤ v i) ∧ (∑ i, v i) = 1 }

```

Similarly, _Sigma types_ are generalizations of ordered pairs, whereby the type of the second component depends on the type of the first.

```
def StdSimplex := Σ n : ℕ, StandardSimplex n

section
variable (s : StdSimplex)

#check s.fst
#check s.snd

#check s.1
#check s.2

end

```

Given `s : StdSimplex`, the first component `s.fst` is a natural number, and the second component is an element of the corresponding simplex `StandardSimplex s.fst`. The difference between a Sigma type and a subtype is that the second component of a Sigma type is data rather than a proposition.
But even though we can use products, subtypes, and Sigma types instead of structures, using structures has a number of advantages. Defining a structure abstracts away the underlying representation and provides custom names for the functions that access the components. This makes proofs more robust: proofs that rely only on the interface to a structure will generally continue to work when we change the definition, as long as we redefine the old accessors in terms of the new definition. Moreover, as we are about to see, Lean provides support for weaving structures together into a rich, interconnected hierarchy, and for managing the interactions between them.
##  7.2. Algebraic Structures[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#algebraic-structures "Link to this heading")
To clarify what we mean by the phrase _algebraic structure_ , it will help to consider some examples.
  1. A _partially ordered set_ consists of a set P and a binary relation ≤ on P that is transitive and reflexive.
  2. A _group_ consists of a set G with an associative binary operation, an identity element 1, and a function g↦g−1 that returns an inverse for each g in G. A group is _abelian_ or _commutative_ if the operation is commutative.
  3. A _lattice_ is a partially ordered set with meets and joins.
  4. A _ring_ consists of an (additively written) abelian group (R,+,0,x↦−x) together with an associative multiplication operation ⋅ and an identity 1, such that multiplication distributes over addition. A ring is _commutative_ if the multiplication is commutative.
  5. An _ordered ring_ (R,+,0,−,⋅,1,≤) consists of a ring together with a partial order on its elements, such that a≤b implies a+c≤b+c for every a, b, and c in R, and 0≤a and 0≤b implies 0≤ab for every a and b in R.
  6. A _metric space_ consists of a set X and a function d:X×X→R such that the following hold:
     * d(x,y)≥0 for every x and y in X.
     * d(x,y)=0 if and only if x=y.
     * d(x,y)=d(y,x) for every x and y in X.
     * d(x,z)≤d(x,y)+d(y,z) for every x, y, and z in X.
  7. A _topological space_ consists of a set X and a collection T of subsets of X, called the _open subsets of_ X, such that the following hold:
     * The empty set and X are open.
     * The intersection of two open sets is open.
     * An arbitrary union of open sets is open.


In each of these examples, the elements of the structure belong to a set, the _carrier set_ , that sometimes stands proxy for the entire structure. For example, when we say “let G be a group” and then “let g∈G,” we are using G to stand for both the structure and its carrier. Not every algebraic structure is associated with a single carrier set in this way. For example, a _bipartite graph_ involves a relation between two sets, as does a _Galois connection_ , A _category_ also involves two sets of interest, commonly called the _objects_ and the _morphisms_.
The examples indicate some of the things that a proof assistant has to do in order to support algebraic reasoning. First, it needs to recognize concrete instances of structures. The number systems Z, Q, and R are all ordered rings, and we should be able to apply a generic theorem about ordered rings in any of these instances. Sometimes a concrete set may be an instance of a structure in more than one way. For example, in addition to the usual topology on R, which forms the basis for real analysis, we can also consider the _discrete_ topology on R, in which every set is open.
Second, a proof assistant needs to support generic notation on structures. In Lean, the notation `*` is used for multiplication in all the usual number systems, as well as for multiplication in generic groups and rings. When we use an expression like `f x * y`, Lean has to use information about the types of `f`, `x`, and `y` to determine which multiplication we have in mind.
Third, it needs to deal with the fact that structures can inherit definitions, theorems, and notation from other structures in various ways. Some structures extend others by adding more axioms. A commutative ring is still a ring, so any definition that makes sense in a ring also makes sense in a commutative ring, and any theorem that holds in a ring also holds in a commutative ring. Some structures extend others by adding more data. For example, the additive part of any ring is an additive group. The ring structure adds a multiplication and an identity, as well as axioms that govern them and relate them to the additive part. Sometimes we can define one structure in terms of another. Any metric space has a canonical topology associated with it, the _metric space topology_ , and there are various topologies that can be associated with any linear ordering.
Finally, it is important to keep in mind that mathematics allows us to use functions and operations to define structures in the same way we use functions and operations to define numbers. Products and powers of groups are again groups. For every n, the integers modulo n form a ring, and for every k>0, the k×k matrices of polynomials with coefficients in that ring again form a ring. Thus we can calculate with structures just as easily as we can calculate with their elements. This means that algebraic structures lead dual lives in mathematics, as containers for collections of objects and as objects in their own right. A proof assistant has to accommodate this dual role.
When dealing with elements of a type that has an algebraic structure associated with it, a proof assistant needs to recognize the structure and find the relevant definitions, theorems, and notation. All this should sound like a lot of work, and it is. But Lean uses a small collection of fundamental mechanisms to carry out these tasks. The goal of this section is to explain these mechanisms and show you how to use them.
The first ingredient is almost too obvious to mention: formally speaking, algebraic structures are structures in the sense of [Section 7.1](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#section-structures). An algebraic structure is a specification of a bundle of data satisfying some axiomatic hypotheses, and we saw in [Section 7.1](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#section-structures) that this is exactly what the `structure` command is designed to accommodate. It’s a marriage made in heaven!
Given a data type `α`, we can define the group structure on `α` as follows.

```
structure Group₁ (α : Type*) where
  mul : α → α → α
  one : α
  inv : α → α
  mul_assoc : ∀ x y z : α, mul (mul x y) z = mul x (mul y z)
  mul_one : ∀ x : α, mul x one = x
  one_mul : ∀ x : α, mul one x = x
  inv_mul_cancel : ∀ x : α, mul (inv x) x = one

```

Notice that the type `α` is a _parameter_ in the definition of `Group₁`. So you should think of an object `struc : Group₁ α` as being a group structure on `α`. We saw in [Section 2.2](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C02_Basics.html#proving-identities-in-algebraic-structures) that the counterpart `mul_inv_cancel` to `inv_mul_cancel` follows from the other group axioms, so there is no need to add it to the definition.
This definition of a group is similar to the definition of `Group` in Mathlib, and we have chosen the name `Group₁` to distinguish our version. If you write `#check Group` and ctrl-click on the definition, you will see that the Mathlib version of `Group` is defined to extend another structure; we will explain how to do that later. If you type `#print Group` you will also see that the Mathlib version of `Group` has a number of extra fields. For reasons we will explain later, sometimes it is useful to add redundant information to a structure, so that there are additional fields for objects and functions that can be defined from the core data. Don’t worry about that for now. Rest assured that our simplified version `Group₁` is morally the same as the definition of a group that Mathlib uses.
It is sometimes useful to bundle the type together with the structure, and Mathlib also contains a definition of a `Grp` structure that is equivalent to the following:

```
structure Grp₁ where
  α : Type*
  str : Group₁ α

```

The Mathlib version is found in `Mathlib.Algebra.Category.Grp.Basic`, and you can `#check` it if you add this to the imports at the beginning of the examples file.
For reasons that will become clearer below, it is more often useful to keep the type `α` separate from the structure `Group α`. We refer to the two objects together as a _partially bundled structure_ , since the representation combines most, but not all, of the components into one structure. It is common in Mathlib to use capital roman letters like `G` for a type when it is used as the carrier type for a group.
Let’s construct a group, which is to say, an element of the `Group₁` type. For any pair of types `α` and `β`, Mathlib defines the type `Equiv α β` of _equivalences_ between `α` and `β`. Mathlib also defines the suggestive notation `α ≃ β` for this type. An element `f : α ≃ β` is a bijection between `α` and `β` represented by four components: a function `f.toFun` from `α` to `β`, the inverse function `f.invFun` from `β` to `α`, and two properties that specify these functions are indeed inverse to one another.

```
variable (α β γ : Type*)
variable (f : α ≃ β) (g : β ≃ γ)

#check Equiv α β
#check (f.toFun : α → β)
#check (f.invFun : β → α)
#check (f.right_inv : ∀ x : β, f (f.invFun x) = x)
#check (f.left_inv : ∀ x : α, f.invFun (f x) = x)
#check (Equiv.refl α : α ≃ α)
#check (f.symm : β ≃ α)
#check (f.trans g : α ≃ γ)

```

Notice the creative naming of the last three constructions. We think of the identity function `Equiv.refl`, the inverse operation `Equiv.symm`, and the composition operation `Equiv.trans` as explicit evidence that the property of being in bijective correspondence is an equivalence relation.
Notice also that `f.trans g` requires composing the forward functions in reverse order. Mathlib has declared a _coercion_ from `Equiv α β` to the function type `α → β`, so we can omit writing `.toFun` and have Lean insert it for us.

```
example (x : α) : (f.trans g).toFun x = g.toFun (f.toFun x) :=
  rfl

example (x : α) : (f.trans g) x = g (f x) :=
  rfl

example : (f.trans g : α → γ) = g ∘ f :=
  rfl

```

Mathlib also defines the type `perm α` of equivalences between `α` and itself.

```
example (α : Type*) : Equiv.Perm α = (α ≃ α) :=
  rfl

```

It should be clear that `Equiv.Perm α` forms a group under composition of equivalences. We orient things so that `mul f g` is equal to `g.trans f`, whose forward function is `f ∘ g`. In other words, multiplication is what we ordinarily think of as composition of the bijections. Here we define this group:

```
def permGroup {α : Type*} : Group₁ (Equiv.Perm α)
    where
  mul f g := Equiv.trans g f
  one := Equiv.refl α
  inv := Equiv.symm
  mul_assoc f g h := (Equiv.trans_assoc _ _ _).symm
  one_mul := Equiv.trans_refl
  mul_one := Equiv.refl_trans
  inv_mul_cancel := Equiv.self_trans_symm

```

In fact, Mathlib defines exactly this `Group` structure on `Equiv.Perm α` in the file `Algebra.Group.End`. As always, you can hover over the theorems used in the definition of `permGroup` to see their statements, and you can jump to their definitions in the original file to learn more about how they are implemented.
In ordinary mathematics, we generally think of notation as independent of structure. For example, we can consider groups (G1,⋅,1,⋅−1), (G2,∘,e,i(⋅)), and (G3,+,0,−). In the first case, we write the binary operation as ⋅, the identity as 1, and the inverse function as x↦x−1. In the second and third cases, we use the notational alternatives shown. When we formalize the notion of a group in Lean, however, the notation is more tightly linked to the structure. In Lean, the components of any `Group` are named `mul`, `one`, and `inv`, and in a moment we will see how multiplicative notation is set up to refer to them. If we want to use additive notation, we instead use an isomorphic structure `AddGroup` (the structure underlying additive groups). Its components are named `add`, `zero`, and `neg`, and the associated notation is what you would expect it to be.
Recall the type `Point` that we defined in [Section 7.1](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#section-structures), and the addition function that we defined there. These definitions are reproduced in the examples file that accompanies this section. As an exercise, define an `AddGroup₁` structure that is similar to the `Group₁` structure we defined above, except that it uses the additive naming scheme just described. Define negation and a zero on the `Point` data type, and define the `AddGroup₁` structure on `Point`.

```
structure AddGroup₁ (α : Type*) where
  (add : α → α → α)
  -- fill in the rest
@[ext]
structure Point where
  x : ℝ
  y : ℝ
  z : ℝ

namespace Point

def add (a b : Point) : Point :=
  ⟨a.x + b.x, a.y + b.y, a.z + b.z⟩

def neg (a : Point) : Point := sorry

def zero : Point := sorry

def addGroupPoint : AddGroup₁ Point := sorry

end Point

```

We are making progress. Now we know how to define algebraic structures in Lean, and we know how to define instances of those structures. But we also want to associate notation with structures so that we can use it with each instance. Moreover, we want to arrange it so that we can define an operation on a structure and use it with any particular instance, and we want to arrange it so that we can prove a theorem about a structure and use it with any instance.
In fact, Mathlib is already set up to use generic group notation, definitions, and theorems for `Equiv.Perm α`.

```
variable {α : Type*} (f g : Equiv.Perm α) (n : ℕ)

#check f * g
#check mul_assoc f g g⁻¹

-- group power, defined for any group
#check g ^ n

example : f * g * g⁻¹ = f := by rw [mul_assoc, mul_inv_cancel, mul_one]

example : f * g * g⁻¹ = f :=
  mul_inv_cancel_right f g

example {α : Type*} (f g : Equiv.Perm α) : g.symm.trans (g.trans f) = f :=
  mul_inv_cancel_right f g

```

You can check that this is not the case for the additive group structure on `Point` that we asked you to define above. Our task now is to understand that magic that goes on under the hood in order to make the examples for `Equiv.Perm α` work the way they do.
The issue is that Lean needs to be able to _find_ the relevant notation and the implicit group structure, using the information that is found in the expressions that we type. Similarly, when we write `x + y` with expressions `x` and `y` that have type `ℝ`, Lean needs to interpret the `+` symbol as the relevant addition function on the reals. It also has to recognize the type `ℝ` as an instance of a commutative ring, so that all the definitions and theorems for a commutative ring are available. For another example, continuity is defined in Lean relative to any two topological spaces. When we have `f : ℝ → ℂ` and we write `Continuous f`, Lean has to find the relevant topologies on `ℝ` and `ℂ`.
The magic is achieved with a combination of three things.
  1. _Logic._ A definition that should be interpreted in any group takes, as arguments, the type of the group and the group structure as arguments. Similarly, a theorem about the elements of an arbitrary group begins with universal quantifiers over the type of the group and the group structure.
  2. _Implicit arguments._ The arguments for the type and the structure are generally left implicit, so that we do not have to write them or see them in the Lean information window. Lean fills the information in for us silently.
  3. _Type class inference._ Also known as _class inference_ , this is a simple but powerful mechanism that enables us to register information for Lean to use later on. When Lean is called on to fill in implicit arguments to a definition, theorem, or piece of notation, it can make use of information that has been registered.


Whereas an annotation `(grp : Group G)` tells Lean that it should expect to be given that argument explicitly and the annotation `{grp : Group G}` tells Lean that it should try to figure it out from contextual cues in the expression, the annotation `[grp : Group G]` tells Lean that the corresponding argument should be synthesized using type class inference. Since the whole point to the use of such arguments is that we generally do not need to refer to them explicitly, Lean allows us to write `[Group G]` and leave the name anonymous. You have probably already noticed that Lean chooses names like `_inst_1` automatically. When we use the anonymous square-bracket annotation with the `variables` command, then as long as the variables are still in scope, Lean automatically adds the argument `[Group G]` to any definition or theorem that mentions `G`.
How do we register the information that Lean needs to use to carry out the search? Returning to our group example, we need only make two changes. First, instead of using the `structure` command to define the group structure, we use the keyword `class` to indicate that it is a candidate for class inference. Second, instead of defining particular instances with `def`, we use the keyword `instance` to register the particular instance with Lean. As with the names of class variables, we are allowed to leave the name of an instance definition anonymous, since in general we intend Lean to find it and put it to use without troubling us with the details.

```
class Group₂ (α : Type*) where
  mul : α → α → α
  one : α
  inv : α → α
  mul_assoc : ∀ x y z : α, mul (mul x y) z = mul x (mul y z)
  mul_one : ∀ x : α, mul x one = x
  one_mul : ∀ x : α, mul one x = x
  inv_mul_cancel : ∀ x : α, mul (inv x) x = one

instance {α : Type*} : Group₂ (Equiv.Perm α) where
  mul f g := Equiv.trans g f
  one := Equiv.refl α
  inv := Equiv.symm
  mul_assoc f g h := (Equiv.trans_assoc _ _ _).symm
  one_mul := Equiv.trans_refl
  mul_one := Equiv.refl_trans
  inv_mul_cancel := Equiv.self_trans_symm

```

The following illustrates their use.

```
#check Group₂.mul

def mySquare {α : Type*} [Group₂ α] (x : α) :=
  Group₂.mul x x

#check mySquare

section
variable {β : Type*} (f g : Equiv.Perm β)

example : Group₂.mul f g = g.trans f :=
  rfl

example : mySquare f = f.trans f :=
  rfl

end

```

The `#check` command shows that `Group₂.mul` has an implicit argument `[Group₂ α]` that we expect to be found by class inference, where `α` is the type of the arguments to `Group₂.mul`. In other words, `{α : Type*}` is the implicit argument for the type of the group elements and `[Group₂ α]` is the implicit argument for the group structure on `α`. Similarly, when we define a generic squaring function `my_square` for `Group₂`, we use an implicit argument `{α : Type*}` for the type of the elements and an implicit argument `[Group₂ α]` for the `Group₂` structure.
In the first example, when we write `Group₂.mul f g`, the type of `f` and `g` tells Lean that in the argument `α` to `Group₂.mul` has to be instantiated to `Equiv.Perm β`. That means that Lean has to find an element of `Group₂ (Equiv.Perm β)`. The previous `instance` declaration tells Lean exactly how to do that. Problem solved!
This simple mechanism for registering information so that Lean can find it when it needs it is remarkably useful. Here is one way it comes up. In Lean’s foundation, a data type `α` may be empty. In a number of applications, however, it is useful to know that a type has at least one element. For example, the function `List.headI`, which returns the first element of a list, can return the default value when the list is empty. To make that work, the Lean library defines a class `Inhabited α`, which does nothing more than store a default value. We can show that the `Point` type is an instance:

```
instance : Inhabited Point where default := ⟨0, 0, 0⟩

#check (default : Point)

example : ([] : List Point).headI = default :=
  rfl

```

The class inference mechanism is also used for generic notation. The expression `x + y` is an abbreviation for `Add.add x y` where—you guessed it—`Add α` is a class that stores a binary function on `α`. Writing `x + y` tells Lean to find a registered instance of `[Add.add α]` and use the corresponding function. Below, we register the addition function for `Point`.

```
instance : Add Point where add := Point.add

section
variable (x y : Point)

#check x + y

example : x + y = Point.add x y :=
  rfl

end

```

In this way, we can assign the notation `+` to binary operations on other types as well.
But we can do even better. We have seen that `*` can be used in any group, `+` can be used in any additive group, and both can be used in any ring. When we define a new instance of a ring in Lean, we don’t have to define `+` and `*` for that instance, because Lean knows that these are defined for every ring. We can use this method to specify notation for our `Group₂` class:

```
instance {α : Type*} [Group₂ α] : Mul α :=
  ⟨Group₂.mul⟩

instance {α : Type*} [Group₂ α] : One α :=
  ⟨Group₂.one⟩

instance {α : Type*} [Group₂ α] : Inv α :=
  ⟨Group₂.inv⟩

section
variable {α : Type*} (f g : Equiv.Perm α)

#check f * 1 * g⁻¹

def foo : f * 1 * g⁻¹ = g.symm.trans ((Equiv.refl α).trans f) :=
  rfl

end

```

What makes this approach work is that Lean carries out a recursive search. According to the instances we have declared, Lean can find an instance of `Mul (Equiv.Perm α)` by finding an instance of `Group₂ (Equiv.Perm α)`, and it can find an instance of `Group₂ (Equiv.Perm α)` because we have provided one. Lean is capable of finding these two facts and chaining them together.
The example we have just given is dangerous, because Lean’s library also has an instance of `Group (Equiv.Perm α)`, and multiplication is defined on any group. So it is ambiguous as to which instance is found. In fact, Lean favors more recent declarations unless you explicitly specify a different priority. Also, there is another way to tell Lean that one structure is an instance of another, using the `extends` keyword. This is how Mathlib specifies that, for example, every commutative ring is a ring. You can find more information in [Section 8](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C08_Hierarchies.html#hierarchies) and in a [section on class inference](https://leanprover.github.io/theorem_proving_in_lean4/type_classes.html#managing-type-class-inference) in _Theorem Proving in Lean_.
In general, it is a bad idea to specify a value of `*` for an instance of an algebraic structure that already has the notation defined. Redefining the notion of `Group` in Lean is an artificial example. In this case, however, both interpretations of the group notation unfold to `Equiv.trans`, `Equiv.refl`, and `Equiv.symm`, in the same way.
As a similarly artificial exercise, define a class `AddGroup₂` in analogy to `Group₂`. Define the usual notation for addition, negation, and zero on any `AddGroup₂` using the classes `Add`, `Neg`, and `Zero`. Then show `Point` is an instance of `AddGroup₂`. Try it out and make sure that the additive group notation works for elements of `Point`.

```
class AddGroup₂ (α : Type*) where
  add : α → α → α
  -- fill in the rest

```

It is not a big problem that we have already declared instances `Add`, `Neg`, and `Zero` for `Point` above. Once again, the two ways of synthesizing the notation should come up with the same answer.
Class inference is subtle, and you have to be careful when using it, because it configures automation that invisibly governs the interpretation of the expressions we type. When used wisely, however, class inference is a powerful tool. It is what makes algebraic reasoning possible in Lean.
##  7.3. Building the Gaussian Integers[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#building-the-gaussian-integers "Link to this heading")
We will now illustrate the use of the algebraic hierarchy in Lean by building an important mathematical object, the _Gaussian integers_ , and showing that it is a Euclidean domain. In other words, according to the terminology we have been using, we will define the Gaussian integers and show that they are an instance of the Euclidean domain structure.
In ordinary mathematical terms, the set of Gaussian integers Z[i] is the set of complex numbers {a+bi∣a,b∈Z}. But rather than define them as a subset of the complex numbers, our goal here is to define them as a data type in their own right. We do this by representing a Gaussian integer as a pair of integers, which we think of as the _real_ and _imaginary_ parts.

```
@[ext]
structure GaussInt where
  re : ℤ
  im : ℤ

```

We first show that the Gaussian integers have the structure of a ring, with `0` defined to be `⟨0, 0⟩`, `1` defined to be `⟨1, 0⟩`, and addition defined pointwise. To work out the definition of multiplication, remember that we want the element i, represented by `⟨0, 1⟩`, to be a square root of −1. Thus we want
(a+bi)(c+di)=ac+bci+adi+bdi2=(ac−bd)+(bc+ad)i.
This explains the definition of `Mul` below.

```
instance : Zero GaussInt :=
  ⟨⟨0, 0⟩⟩

instance : One GaussInt :=
  ⟨⟨1, 0⟩⟩

instance : Add GaussInt :=
  ⟨fun x y ↦ ⟨x.re + y.re, x.im + y.im⟩⟩

instance : Neg GaussInt :=
  ⟨fun x ↦ ⟨-x.re, -x.im⟩⟩

instance : Mul GaussInt :=
  ⟨fun x y ↦ ⟨x.re * y.re - x.im * y.im, x.re * y.im + x.im * y.re⟩⟩

```

As noted in [Section 7.1](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C07_Structures.html#section-structures), it is a good idea to put all the definitions related to a data type in a namespace with the same name. Thus in the Lean files associated with this chapter, these definitions are made in the `GaussInt` namespace.
Notice that here we are defining the interpretations of the notation `0`, `1`, `+`, `-`, and `*` directly, rather than naming them `GaussInt.zero` and the like and assigning the notation to those. It is often useful to have an explicit name for the definitions, for example, to use with `simp` and `rw`.

```
theorem zero_def : (0 : GaussInt) = ⟨0, 0⟩ :=
  rfl

theorem one_def : (1 : GaussInt) = ⟨1, 0⟩ :=
  rfl

theorem add_def (x y : GaussInt) : x + y = ⟨x.re + y.re, x.im + y.im⟩ :=
  rfl

theorem neg_def (x : GaussInt) : -x = ⟨-x.re, -x.im⟩ :=
  rfl

theorem mul_def (x y : GaussInt) :
    x * y = ⟨x.re * y.re - x.im * y.im, x.re * y.im + x.im * y.re⟩ :=
  rfl

```

It is also useful to name the rules that compute the real and imaginary parts, and to declare them to the simplifier.

```
@[simp]
theorem zero_re : (0 : GaussInt).re = 0 :=
  rfl

@[simp]
theorem zero_im : (0 : GaussInt).im = 0 :=
  rfl

@[simp]
theorem one_re : (1 : GaussInt).re = 1 :=
  rfl

@[simp]
theorem one_im : (1 : GaussInt).im = 0 :=
  rfl

@[simp]
theorem add_re (x y : GaussInt) : (x + y).re = x.re + y.re :=
  rfl

@[simp]
theorem add_im (x y : GaussInt) : (x + y).im = x.im + y.im :=
  rfl

@[simp]
theorem neg_re (x : GaussInt) : (-x).re = -x.re :=
  rfl

@[simp]
theorem neg_im (x : GaussInt) : (-x).im = -x.im :=
  rfl

@[simp]
theorem mul_re (x y : GaussInt) : (x * y).re = x.re * y.re - x.im * y.im :=
  rfl

@[simp]
theorem mul_im (x y : GaussInt) : (x * y).im = x.re * y.im + x.im * y.re :=
  rfl

```

It is now surprisingly easy to show that the Gaussian integers are an instance of a commutative ring. We are putting the structure concept to good use. Each particular Gaussian integer is an instance of the `GaussInt` structure, whereas the type `GaussInt` itself, together with the relevant operations, is an instance of the `CommRing` structure. The `CommRing` structure, in turn, extends the notational structures `Zero`, `One`, `Add`, `Neg`, and `Mul`.
If you type `instance : CommRing GaussInt := _`, click on the light bulb that appears in VS Code, and then ask Lean to fill in a skeleton for the structure definition, you will see a scary number of entries. Jumping to the definition of the structure, however, shows that many of the fields have default definitions that Lean will fill in for you automatically. The essential ones appear in the definition below. A special case are `nsmul` and `zsmul` which should be ignored for now and will be explained in the next chapter. In each case, the relevant identity is proved by unfolding definitions, using the `ext` tactic to reduce the identities to their real and imaginary components, simplifying, and, if necessary, carrying out the relevant ring calculation in the integers. Note that we could easily avoid repeating all this code, but this is not the topic of the current discussion.

```
instance instCommRing : CommRing GaussInt where
  zero := 0
  one := 1
  add := (· + ·)
  neg x := -x
  mul := (· * ·)
  nsmul := nsmulRec
  zsmul := zsmulRec
  add_assoc := by
    intros
    ext <;> simp <;> ring
  zero_add := by
    intro
    ext <;> simp
  add_zero := by
    intro
    ext <;> simp
  neg_add_cancel := by
    intro
    ext <;> simp
  add_comm := by
    intros
    ext <;> simp <;> ring
  mul_assoc := by
    intros
    ext <;> simp <;> ring
  one_mul := by
    intro
    ext <;> simp
  mul_one := by
    intro
    ext <;> simp
  left_distrib := by
    intros
    ext <;> simp <;> ring
  right_distrib := by
    intros
    ext <;> simp <;> ring
  mul_comm := by
    intros
    ext <;> simp <;> ring
  zero_mul := by
    intros
    ext <;> simp
  mul_zero := by
    intros
    ext <;> simp

```

Lean’s library defines the class of _nontrivial_ types to be types with at least two distinct elements. In the context of a ring, this is equivalent to saying that the zero is not equal to the one. Since some common theorems depend on that fact, we may as well establish it now.

```
instance : Nontrivial GaussInt := by
  use 0, 1
  rw [Ne, GaussInt.ext_iff]
  simp

```

We will now show that the Gaussian integers have an important additional property. A _Euclidean domain_ is a ring R equipped with a _norm_ function N:R→N with the following two properties:
  * For every a and b≠0 in R, there are q and r in R such that a=bq+r and either r=0 or N(r)<N(b).
  * For every a and b≠0, N(a)≤N(ab).


The ring of integers Z with N(a)=|a| is an archetypal example of a Euclidean domain. In that case, we can take q to be the result of integer division of a by b and r to be the remainder. These functions are defined in Lean so that the satisfy the following:

```
example (a b : ℤ) : a = b * (a / b) + a % b :=
  Eq.symm (Int.ediv_add_emod a b)

example (a b : ℤ) : b ≠ 0 → 0 ≤ a % b :=
  Int.emod_nonneg a

example (a b : ℤ) : b ≠ 0 → a % b < |b| :=
  Int.emod_lt_abs a

```

In an arbitrary ring, an element a is said to be a _unit_ if it divides 1. A nonzero element a is said to be _irreducible_ if it cannot be written in the form a=bc where neither b nor c is a unit. In the integers, every irreducible element a is _prime_ , which is to say, whenever a divides a product bc, it divides either b or c. But in other rings this property can fail. In the ring Z[−5], we have
6=2⋅3=(1+−5)(1−−5),
and the elements 2, 3, 1+−5, and 1−−5 are all irreducible, but they are not prime. For example, 2 divides the product (1+−5)(1−−5), but it does not divide either factor. In particular, we no longer have unique factorization: the number 6 can be factored into irreducible elements in more than one way.
In contrast, every Euclidean domain is a unique factorization domain, which implies that every irreducible element is prime. The axioms for a Euclidean domain imply that one can write any nonzero element as a finite product of irreducible elements. They also imply that one can use the Euclidean algorithm to find a greatest common divisor of any two nonzero elements `a` and `b`, i.e. an element that is divisible by any other common divisor. This, in turn, implies that factorization into irreducible elements is unique up to multiplication by units.
We now show that the Gaussian integers are a Euclidean domain with the norm defined by N(a+bi)=(a+bi)(a−bi)=a2+b2. The Gaussian integer a−bi is called the _conjugate_ of a+bi. It is not hard to check that for any complex numbers x and y, we have N(xy)=N(x)N(y).
To see that this definition of the norm makes the Gaussian integers a Euclidean domain, only the first property is challenging. Suppose we want to write a+bi=(c+di)q+r for suitable q and r. Treating a+bi and c+di as complex numbers, carry out the division
a+bic+di=(a+bi)(c−di)(c+di)(c−di)=ac+bdc2+d2+bc−adc2+d2i.
The real and imaginary parts might not be integers, but we can round them to the nearest integers u and v. We can then express the right-hand side as (u+vi)+(u′+v′i), where u′+v′i is the part left over. Note that we have |u′|≤1/2 and |v′|≤1/2, and hence
N(u′+v′i)=(u′)2+(v′)2≤1/4+1/4≤1/2.
Multiplying through by c+di, we have
a+bi=(c+di)(u+vi)+(c+di)(u′+v′i).
Setting q=u+vi and r=(c+di)(u′+v′i), we have a+bi=(c+di)q+r, and we only need to bound N(r):
N(r)=N(c+di)N(u′+v′i)≤N(c+di)⋅1/2<N(c+di).
The argument we just carried out requires viewing the Gaussian integers as a subset of the complex numbers. One option for formalizing it in Lean is therefore to embed the Gaussian integers in the complex numbers, embed the integers in the Gaussian integers, define the rounding function from the real numbers to the integers, and take great care to pass back and forth between these number systems appropriately. In fact, this is exactly the approach that is followed in Mathlib, where the Gaussian integers themselves are constructed as a special case of a ring of _quadratic integers_. See the file [GaussianInt.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/NumberTheory/Zsqrtd/GaussianInt.lean).
Here we will instead carry out an argument that stays in the integers. This illustrates a choice one commonly faces when formalizing mathematics. Given an argument that requires concepts or machinery that is not already in the library, one has two choices: either formalize the concepts and machinery needed, or adapt the argument to make use of concepts and machinery you already have. The first choice is generally a good investment of time when the results can be used in other contexts. Pragmatically speaking, however, sometimes seeking a more elementary proof is more efficient.
The usual quotient-remainder theorem for the integers says that for every a and nonzero b, there are q and r such that a=bq+r and 0≤r<b. Here we will make use of the following variation, which says that there are q′ and r′ such that a=bq′+r′ and |r′|≤b/2. You can check that if the value of r in the first statement satisfies r≤b/2, we can take q′=q and r′=r, and otherwise we can take q′=q+1 and r′=r−b. We are grateful to Heather Macbeth for suggesting the following more elegant approach, which avoids definition by cases. We simply add `b / 2` to `a` before dividing and then subtract it from the remainder.

```
def div' (a b : ℤ) :=
  (a + b / 2) / b

def mod' (a b : ℤ) :=
  (a + b / 2) % b - b / 2

theorem div'_add_mod' (a b : ℤ) : b * div' a b + mod' a b = a := by
  rw [div', mod']
  linarith [Int.ediv_add_emod (a + b / 2) b]

theorem abs_mod'_le (a b : ℤ) (h : 0 < b) : |mod' a b| ≤ b / 2 := by
  rw [mod', abs_le]
  constructor
  · linarith [Int.emod_nonneg (a + b / 2) h.ne']
  have := Int.emod_lt_of_pos (a + b / 2) h
  have := Int.ediv_add_emod b 2
  have := Int.emod_lt_of_pos b zero_lt_two
  linarith

```

Note the use of our old friend, `linarith`. We will also need to express `mod'` in terms of `div'`.

```
theorem mod'_eq (a b : ℤ) : mod' a b = a - b * div' a b := by linarith [div'_add_mod' a b]

```

We will use the fact that x2+y2 is equal to zero if and only if x and y are both zero. As an exercise, we ask you to prove that this holds in any ordered ring.

```
theorem sq_add_sq_eq_zero {α : Type*} [Ring α] [LinearOrder α] [IsStrictOrderedRing α]
    (x y : α) : x ^ 2 + y ^ 2 = 0 ↔ x = 0 ∧ y = 0 := by
  sorry

```

We will put all the remaining definitions and theorems in this section in the `GaussInt` namespace. First, we define the `norm` function and ask you to establish some of its properties. The proofs are all short.

```
def norm (x : GaussInt) :=
  x.re ^ 2 + x.im ^ 2

@[simp]
theorem norm_nonneg (x : GaussInt) : 0 ≤ norm x := by
  sorry
theorem norm_eq_zero (x : GaussInt) : norm x = 0 ↔ x = 0 := by
  sorry
theorem norm_pos (x : GaussInt) : 0 < norm x ↔ x ≠ 0 := by
  sorry
theorem norm_mul (x y : GaussInt) : norm (x * y) = norm x * norm y := by
  sorry

```

Next we define the conjugate function:

```
def conj (x : GaussInt) : GaussInt :=
  ⟨x.re, -x.im⟩

@[simp]
theorem conj_re (x : GaussInt) : (conj x).re = x.re :=
  rfl

@[simp]
theorem conj_im (x : GaussInt) : (conj x).im = -x.im :=
  rfl

theorem norm_conj (x : GaussInt) : norm (conj x) = norm x := by simp [norm]

```

Finally, we define division for the Gaussian integers with the notation `x / y`, that rounds the complex quotient to the nearest Gaussian integer. We use our bespoke `Int.div'` for that purpose. As we calculated above, if `x` is a+bi and `y` is c+di, then the real and imaginary parts of `x / y` are the nearest integers to
ac+bdc2+d2andbc−adc2+d2,
respectively. Here the numerators are the real and imaginary parts of (a+bi)(c−di), and the denominators are both equal to the norm of c+di.

```
instance : Div GaussInt :=
  ⟨fun x y ↦ ⟨Int.div' (x * conj y).re (norm y), Int.div' (x * conj y).im (norm y)⟩⟩

```

Having defined `x / y`, We define `x % y` to be the remainder, `x - (x / y) * y`. As above, we record the definitions in the theorems `div_def` and `mod_def` so that we can use them with `simp` and `rw`.

```
instance : Mod GaussInt :=
  ⟨fun x y ↦ x - y * (x / y)⟩

theorem div_def (x y : GaussInt) :
    x / y = ⟨Int.div' (x * conj y).re (norm y), Int.div' (x * conj y).im (norm y)⟩ :=
  rfl

theorem mod_def (x y : GaussInt) : x % y = x - y * (x / y) :=
  rfl

```

These definitions immediately yield `x = y * (x / y) + x % y` for every `x` and `y`, so all we need to do is show that the norm of `x % y` is less than the norm of `y` when `y` is not zero.
We just defined the real and imaginary parts of `x / y` to be `div' (x * conj y).re (norm y)` and `div' (x * conj y).im (norm y)`, respectively. Calculating, we have
> `(x % y) * conj y = (x - x / y * y) * conj y = x * conj y - x / y * (y * conj y)`
The real and imaginary parts of the right-hand side are exactly `mod' (x * conj y).re (norm y)` and `mod' (x * conj y).im (norm y)`. By the properties of `div'` and `mod'`, these are guaranteed to be less than or equal to `norm y / 2`. So we have
> `norm ((x % y) * conj y) ≤ (norm y / 2)^2 + (norm y / 2)^2 ≤ (norm y / 2) * norm y`.
On the other hand, we have
> `norm ((x % y) * conj y) = norm (x % y) * norm (conj y) = norm (x % y) * norm y`.
Dividing through by `norm y` we have `norm (x % y) ≤ (norm y) / 2 < norm y`, as required.
This messy calculation is carried out in the next proof. We encourage you to step through the details and see if you can find a nicer argument.

```
theorem norm_mod_lt (x : GaussInt) {y : GaussInt} (hy : y ≠ 0) :
    (x % y).norm < y.norm := by
  have norm_y_pos : 0 < norm y := by rwa [norm_pos]
  have H1 : x % y * conj y = ⟨Int.mod' (x * conj y).re (norm y), Int.mod' (x * conj y).im (norm y)⟩
  · ext <;> simp [Int.mod'_eq, mod_def, div_def, norm] <;> ring
  have H2 : norm (x % y) * norm y ≤ norm y / 2 * norm y
  · calc
      norm (x % y) * norm y = norm (x % y * conj y) := by simp only [norm_mul, norm_conj]
      _ = |Int.mod' (x.re * y.re + x.im * y.im) (norm y)| ^ 2
          + |Int.mod' (-(x.re * y.im) + x.im * y.re) (norm y)| ^ 2 := by simp [H1, norm, sq_abs]
      _ ≤ (y.norm / 2) ^ 2 + (y.norm / 2) ^ 2 := by gcongr <;> apply Int.abs_mod'_le _ _ norm_y_pos
      _ = norm y / 2 * (norm y / 2 * 2) := by ring
      _ ≤ norm y / 2 * norm y := by gcongr; apply Int.ediv_mul_le; norm_num
  calc norm (x % y) ≤ norm y / 2 := le_of_mul_le_mul_right H2 norm_y_pos
    _ < norm y := by
        apply Int.ediv_lt_of_lt_mul
        · norm_num
        · linarith

```

We are in the home stretch. Our `norm` function maps Gaussian integers to nonnegative integers. We need a function that maps Gaussian integers to natural numbers, and we obtain that by composing `norm` with the function `Int.natAbs`, which maps integers to the natural numbers. The first of the next two lemmas establishes that mapping the norm to the natural numbers and back to the integers does not change the value. The second one re-expresses the fact that the norm is decreasing.

```
theorem coe_natAbs_norm (x : GaussInt) : (x.norm.natAbs : ℤ) = x.norm :=
  Int.natAbs_of_nonneg (norm_nonneg _)

theorem natAbs_norm_mod_lt (x y : GaussInt) (hy : y ≠ 0) :
    (x % y).norm.natAbs < y.norm.natAbs := by
  apply Int.ofNat_lt.1
  simp only [Int.natCast_natAbs, abs_of_nonneg, norm_nonneg]
  exact norm_mod_lt x hy

```

We also need to establish the second key property of the norm function on a Euclidean domain.

```
theorem not_norm_mul_left_lt_norm (x : GaussInt) {y : GaussInt} (hy : y ≠ 0) :
    ¬(norm (x * y)).natAbs < (norm x).natAbs := by
  apply not_lt_of_ge
  rw [norm_mul, Int.natAbs_mul]
  apply le_mul_of_one_le_right (Nat.zero_le _)
  apply Int.ofNat_le.1
  rw [coe_natAbs_norm]
  exact Int.add_one_le_of_lt ((norm_pos _).mpr hy)

```

We can now put it together to show that the Gaussian integers are an instance of a Euclidean domain. We use the quotient and remainder function we have defined. The Mathlib definition of a Euclidean domain is more general than the one above in that it allows us to show that remainder decreases with respect to any well-founded measure. Comparing the values of a norm function that returns natural numbers is just one instance of such a measure, and in that case, the required properties are the theorems `natAbs_norm_mod_lt` and `not_norm_mul_left_lt_norm`.

```
instance : EuclideanDomain GaussInt :=
  { GaussInt.instCommRing with
    quotient := (· / ·)
    remainder := (· % ·)
    quotient_mul_add_remainder_eq :=
      fun x y ↦ by rw [mod_def, add_comm] ; ring
    quotient_zero := fun x ↦ by
      simp [div_def, norm, Int.div']
      rfl
    r := (measure (Int.natAbs ∘ norm)).1
    r_wellFounded := (measure (Int.natAbs ∘ norm)).2
    remainder_lt := natAbs_norm_mod_lt
    mul_left_not_lt := not_norm_mul_left_lt_norm }

```

An immediate payoff is that we now know that, in the Gaussian integers, the notions of being prime and being irreducible coincide.

```
example (x : GaussInt) : Irreducible x ↔ Prime x :=
  irreducible_iff_prime

```

[](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C06_Discrete_Mathematics.html "6. Discrete Mathematics") [Next ](file:///home/rian-macedo/Projects/confia_crawler/output/01_raw_html/math_in_lean/C08_Hierarchies.html "8. Hierarchies")
* * *
© Copyright 2020-2025, Jeremy Avigad, Patrick Massot. Text licensed under CC BY 4.0.
Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 

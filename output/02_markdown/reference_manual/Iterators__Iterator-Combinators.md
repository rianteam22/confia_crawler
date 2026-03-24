[←22.3. Consuming Iterators](Iterators/Consuming-Iterators/#The-Lean-Language-Reference--Iterators--Consuming-Iterators "22.3. Consuming Iterators")[22.5. Reasoning About Iterators→](Iterators/Reasoning-About-Iterators/#The-Lean-Language-Reference--Iterators--Reasoning-About-Iterators "22.5. Reasoning About Iterators")
#  22.4. Iterator Combinators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Iterator-Combinators "Permalink")
The documentation for iterator combinators often includes _marble diagrams_ that show the relationship between the elements returned by the underlying iterators and the elements returned by the combinator's iterator. Marble diagrams provide examples, not full specifications. These diagrams consist of a number of rows. Each row shows an example of an iterator's output, where `-` indicates a `[skip](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___skip "Documentation for Std.PlausibleIterStep.skip")`, a term indicates a value returned with `[yield](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___yield "Documentation for Std.PlausibleIterStep.yield")`, and `⊥` indicates the end of iteration. Spaces indicate that iteration did not occur. Unbound identifiers in the marble diagram stand for arbitrary values of the iterator's element type.
Vertical alignment in the marble diagram indicates a causal relationship: when two elements are aligned, it means that consuming the iterator in the lower row results in the upper rows being consumed. In particular, consuming up to the `nnn`th column of the lower iterator results in the consumption of the first `nnn` columns from the upper iterator.
A marble diagram for an identity iterator combinator that returns each element from the underlying iterator looks like this:

```
it    ---a-----b---c----d⊥
it.id ---a-----b---c----d⊥

```

A marble diagram for an iterator combinator that duplicates each element of the underlying iterator looks like this:

```
it           ---a  ---b  ---c  ---d⊥
it.double    ---a-a---b-b---c-c---d-d⊥

```

The marble diagram for `[Iter.filter](Iterators/Iterator-Combinators/#Std___Iter___filter "Documentation for Std.Iter.filter")` shows how some elements of the underlying iterator do not occur in the filtered iterator, but also that stepping the filtered iterator results in a `[skip](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___skip "Documentation for Std.PlausibleIterStep.skip")` when the underlying iterator returns a value that doesn't satisfy the predicate:

```
it            ---a--b--c--d-e--⊥
it.filter     ---a-----c-------⊥

```

The diagram requires an explanatory note:
> (given that `f a = f c = true` and `f b = f d = d e = false`)
The diagram for `[Iter.zip](Iterators/Iterator-Combinators/#Std___Iter___zip "Documentation for Std.Iter.zip")` shows how consuming the combined iterator consumes the underlying iterators:

```
left               --a        ---b        --c
right                 --x         --y        --⊥
left.zip right     -----(a, x)------(b, y)-----⊥

```

The zipped iterator emits `[skip](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___skip "Documentation for Std.PlausibleIterStep.skip")`s so long as `left` does. When `left` emits `a`, the zipped iterator emits one more `[skip](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___skip "Documentation for Std.PlausibleIterStep.skip")`. After this, the zipped iterator switches to consuming `right`, and it emits `[skip](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___skip "Documentation for Std.PlausibleIterStep.skip")`s so long as `right` does. When `right` emits `x`, the zipped iterator emits the pair `(a, x)`. This interleaving of `left` and `right` continues until one of them stops, at which point the zipped iterator stops. Blank spaces in the upper rows of the marble diagram indicate that the iterator is not being consumed at that step.
##  22.4.1. Pure Combinators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Iterator-Combinators--Pure-Combinators "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.mk "Permalink")constructor of Std.IterM
```


Std.IterM.mk.{w, w'} {α : Type w} {m : Type w → Type w'} {β : Type w}
  (internalState : α) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.mk.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  (internalState : α) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

Wraps the state of an iterator into an `[Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter")` object.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.toIterM "Permalink")def
```


Std.Iter.toIterM.{w} {α β : Type w} (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β


Std.Iter.toIterM.{w} {α β : Type w}
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β


```

Converts a pure iterator (`[Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β`) into a monadic iterator (`[IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β`) in the identity monad `[Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.take "Permalink")def
```


Std.Iter.take.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.Iter.take.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

Given an iterator `it` and a natural number `n`, `it.[take](Iterators/Iterator-Combinators/#Std___Iter___take "Documentation for Std.Iter.take") n` is an iterator that outputs up to the first `n` of `it`'s values in order and then terminates.
**Marble diagram:**
`it          ---a----b---c--d-e--⊥ it.take 3   ---a----b---c⊥  it          ---a--⊥ it.take 3   ---a--⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is productive
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


**Performance:**
This combinator incurs an additional O(1) cost with each output of `it`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.takeWhile "Permalink")def
```


Std.Iter.takeWhile.{w} {α β : Type w} (P : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.Iter.takeWhile.{w} {α β : Type w}
  (P : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

Given an iterator `it` and a predicate `P`, `it.[takeWhile](Iterators/Iterator-Combinators/#Std___Iter___takeWhile "Documentation for Std.Iter.takeWhile") P` is an iterator that outputs the values emitted by `it` until one of those values is rejected by `P`. If some emitted value is rejected by `P`, the value is dropped and the iterator terminates.
**Marble diagram:**
Assuming that the predicate `P` accepts `a` and `b` but rejects `c`:
`it               ---a----b---c--d-e--⊥ it.takeWhile P   ---a----b---⊥  it               ---a----⊥ it.takeWhile P   ---a----⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


Depending on `P`, it is possible that `it.[takeWhile](Iterators/Iterator-Combinators/#Std___Iter___takeWhile "Documentation for Std.Iter.takeWhile") P` is finite (or productive) although `it` is not. In this case, the `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance needs to be proved manually.
**Performance:**
This combinator calls `P` on each output of `it` until the predicate evaluates to false. Then it terminates.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.toTake "Permalink")def
```


Std.Iter.toTake.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.Iter.toTake.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

This combinator is only useful for advanced use cases.
Given a finite iterator `it`, returns an iterator that behaves exactly like `it` but is of the same type as `it.[take](Iterators/Iterator-Combinators/#Std___Iter___take "Documentation for Std.Iter.take") n`.
**Marble diagram:**
`it          ---a----b---c--d-e--⊥ it.toTake   ---a----b---c--d-e--⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: always
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: always


**Performance:**
This combinator incurs an additional O(1) cost with each output of `it`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.drop "Permalink")def
```


Std.Iter.drop.{w} {α β : Type w} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.Iter.drop.{w} {α β : Type w} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

Given an iterator `it` and a natural number `n`, `it.[drop](Iterators/Iterator-Combinators/#Std___Iter___drop "Documentation for Std.Iter.drop") n` is an iterator that forwards all of `it`'s output values except for the first `n`.
**Marble diagram:**
`it          ---a----b---c--d-e--⊥ it.drop 3   ---------------d-e--⊥  it          ---a--⊥ it.drop 3   ------⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


**Performance:**
Currently, this combinator incurs an additional O(1) cost with each output of `it`, even when the iterator does not drop any elements anymore.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.dropWhile "Permalink")def
```


Std.Iter.dropWhile.{w} {α β : Type w} (P : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.Iter.dropWhile.{w} {α β : Type w}
  (P : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

Given an iterator `it` and a predicate `P`, `it.[dropWhile](Iterators/Iterator-Combinators/#Std___Iter___dropWhile "Documentation for Std.Iter.dropWhile") P` is an iterator that emits the values emitted by `it` starting from the first value that is rejected by `P`. The elements before are dropped.
In situations where `P` is monadic, use `dropWhileM` instead.
**Marble diagram:**
Assuming that the predicate `P` accepts `a` and `b` but rejects `c`:
`it               ---a----b---c--d-e--⊥ it.dropWhile P   ------------c--d-e--⊥  it               ---a----⊥ it.dropWhile P   --------⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite


Depending on `P`, it is possible that `it.dropWhileM P` is productive although `it` is not. In this case, the `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance needs to be proved manually.
**Performance:**
This combinator calls `P` on each output of `it` until the predicate evaluates to false. After that, the combinator incurs an additional O(1) cost for each value emitted by `it`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.stepSize "Permalink")def
```


Std.Iter.stepSize.{u_1} {α β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.Iter.stepSize.{u_1} {α β : Type u_1}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

Produces an iterator that emits one value of `it`, then drops `n - 1` elements, then emits another value, and so on. In other words, it emits every `n`-th value of `it`, starting with the first one.
If `n = 0`, the iterator behaves like for `n = 1`: It emits all values of `it`.
**Marble diagram:**
`it               ---1----2----3---4----5 it.stepSize 2    ---1---------3--------5`
**Availability:**
This operation is currently only available for iterators implementing `[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess")`, such as `PRange.iter` range iterators.
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if the base iterator `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.map "Permalink")def
```


Std.Iter.map.{w} {α β γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (f : β → γ)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ


Std.Iter.map.{w} {α β γ : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (f : β → γ)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ


```

If `it` is an iterator, then `it.[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") f` is another iterator that applies a function `f` to all values emitted by `it` and emits the result.
In situations where `f` is monadic, use `mapM` instead.
**Marble diagram:**
`it         ---a --b --c --d -e ----⊥ it.map     ---a'--b'--c'--d'-e'----⊥`
(given that `f a = a'`, `f b = b'` etc.)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.mapM "Permalink")def
```


Std.Iter.mapM.{w, w'} {α β γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m] (f : β → m γ)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.Iter.mapM.{w, w'} {α β γ : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m] (f : β → m γ)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

If `it` is an iterator, then `it.[mapM](Iterators/Iterator-Combinators/#Std___Iter___mapM "Documentation for Std.Iter.mapM") f` is another iterator that applies a monadic function `f` to all values emitted by `it` and emits the result.
The base iterator `it` being monadic in `m`, `f` can return values in any monad `n` for which a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n` instance is available.
If `f` is pure, then the simpler variant `it.[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map")` can be used instead.
**Marble diagram (without monadic effects):**
`it          ---a --b --c --d -e ----⊥ it.mapM     ---a'--b'--c'--d'-e'----⊥`
(given that `f a = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") a'`, `f b = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") b'` etc.)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.mapM` will be finite even if `it` isn't. In such cases, the termination proof needs to be done manually.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.mapWithPostcondition "Permalink")def
```


Std.Iter.mapWithPostcondition.{w, w'} {α β γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m γ)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.Iter.mapWithPostcondition.{w, w'}
  {α β γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m γ)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

_Note: This is a very general combinator that requires an advanced understanding of monads, dependent types and termination proofs. The variants`map` and `mapM` are easier to use and sufficient for most use cases._
If `it` is an iterator, then `it.[mapWithPostcondition](Iterators/Iterator-Combinators/#Std___Iter___mapWithPostcondition "Documentation for Std.Iter.mapWithPostcondition") f` is another iterator that applies a monadic function `f` to all values emitted by `it` and emits the result.
`f` is expected to return `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n _`, where `n` is an arbitrary monad. The `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT")` transformer allows the caller to intrinsically prove properties about `f`'s return value in the monad `n`, enabling termination proofs depending on the specific behavior of `f`.
**Marble diagram (without monadic effects):**
`it                          ---a --b --c --d -e ----⊥ it.mapWithPostcondition     ---a'--b'--c'--d'-e'----⊥`
(given that `f a = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") a'`, `f b = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") b'` etc.)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.mapWithPostcondition` will be finite even if `it` isn't.
In such situations, the missing instances can be proved manually if the postcondition bundled in the `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n` monad is strong enough. In the given example, a suitable postcondition might be `fun _ => [False](Basic-Propositions/Truth/#False "Documentation for False")`.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.uLift "Permalink")def
```


Std.Iter.uLift.{v, u} {α β : Type u} (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") β)


Std.Iter.uLift.{v, u} {α β : Type u}
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") β)


```

Transforms an iterator with values in `β` into one with values in `[ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") β`.
Most other combinators like `map` cannot switch between universe levels. This combinators makes it possible to transition to a higher universe.
**Marble diagram:**
`it            ---a    ----b    ---c    --d    ---⊥ it.uLift n    ---.up a----.up b---.up c--.up d---⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")`: only if the original iterator is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`: only if the original iterator is productive


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.flatMap "Permalink")def
```


Std.Iter.flatMap.{w} {α β α₂ γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") γ] (f : β → [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ


Std.Iter.flatMap.{w} {α β α₂ γ : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") γ]
  (f : β → [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ


```

Let `it` be an iterator and `f` a function mapping `it`'s outputs to iterators. Then `it.[flatMap](Iterators/Iterator-Combinators/#Std___Iter___flatMap "Documentation for Std.Iter.flatMap") f` is an iterator that goes over `it` and for each output, it applies `f` and iterates over the resulting iterator. `it.[flatMap](Iterators/Iterator-Combinators/#Std___Iter___flatMap "Documentation for Std.Iter.flatMap") f` emits all values obtained from the inner iterators -- first, all of the first inner iterator, then all of the second one, and so on.
**Marble diagram:**

```
it                 ---a      --b      c    --d -⊥
f a                    a1-a2⊥
f b                             b1-b2⊥
f c                                    c1-c2⊥
f d                                           ⊥
it.flatMap         ----a1-a2----b1-b2--c1-c2----⊥

```

**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` and the inner iterators are finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite and the inner iterators are productive


For certain functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided out of the box. For example, if the outer iterator is productive and the inner iterators are productive _and provably never empty_ , then the resulting iterator is also productive.
**Performance:**
This combinator incurs an additional O(1) cost with each output of `it` or an internal iterator.
For each value emitted by the outer iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.flatMapM "Permalink")def
```


Std.Iter.flatMapM.{w, w'} {α β α₂ γ : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ]
  (f : β → m ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.Iter.flatMapM.{w, w'}
  {α β α₂ γ : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [MonadAttach m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ]
  (f : β → m ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

Let `it` be an iterator and `f` a monadic function mapping `it`'s outputs to iterators. Then `it.[flatMapM](Iterators/Iterator-Combinators/#Std___Iter___flatMapM "Documentation for Std.Iter.flatMapM") f` is an iterator that goes over `it` and for each output, it applies `f` and iterates over the resulting iterator. `it.[flatMapM](Iterators/Iterator-Combinators/#Std___Iter___flatMapM "Documentation for Std.Iter.flatMapM") f` emits all values obtained from the inner iterators -- first, all of the first inner iterator, then all of the second one, and so on.
**Marble diagram (without monadic effects):**

```
it                 ---a      --b      c    --d -⊥
f a                    a1-a2⊥
f b                             b1-b2⊥
f c                                    c1-c2⊥
f d                                           ⊥
it.flatMapM        ----a1-a2----b1-b2--c1-c2----⊥

```

**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` and the inner iterators are finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite and the inner iterators are productive


For certain functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided out of the box. For example, if the outer iterator is productive and the inner iterators are productive _and provably never empty_ , then the resulting iterator is also productive.
**Performance:**
This combinator incurs an additional O(1) cost with each output of `it` or an internal iterator.
For each value emitted by the outer iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.flatMapAfter "Permalink")def
```


Std.Iter.flatMapAfter.{w} {α β α₂ γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") γ] (f : β → [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ) (it₁ : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β)
  (it₂ : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ)) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ


Std.Iter.flatMapAfter.{w}
  {α β α₂ γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") γ] (f : β → [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ)
  (it₁ : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) (it₂ : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ)) :
  [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ


```

Let `it₁` and `it₂` be iterators and `f` a function mapping `it₁`'s outputs to iterators of the same type as `it₂`. Then `it₁.[flatMapAfter](Iterators/Iterator-Combinators/#Std___Iter___flatMapAfter "Documentation for Std.Iter.flatMapAfter") f it₂` first goes over `it₂` and then over `it₁.[flatMap](Iterators/Iterator-Combinators/#Std___Iter___flatMap "Documentation for Std.Iter.flatMap") f it₂`, emitting all their values.
The main purpose of this combinator is to represent the intermediate state of a `flatMap` iterator that is currently iterating over one of the inner iterators.
**Marble diagram:**

```
it₁                            --b      c    --d -⊥
it₂                      a1-a2⊥
f b                               b1-b2⊥
f c                                      c1-c2⊥
f d                                             ⊥
it.flatMapAfter  f it₂   a1-a2----b1-b2--c1-c2----⊥

```

**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it₁`, `it₂` and the inner iterators are finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it₁` is finite and `it₂` and the inner iterators are productive


For certain functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided out of the box. For example, if the outer iterator is productive and the inner iterators are productive _and provably never empty_ , then the resulting iterator is also productive.
**Performance:**
This combinator incurs an additional O(1) cost with each output of `it₁`, `it₂` or an internal iterator.
For each value emitted by the outer iterator `it₁`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.flatMapAfterM "Permalink")def
```


Std.Iter.flatMapAfterM.{w, w'} {α β α₂ γ : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ] (f : β → m ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) (it₁ : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β)
  (it₂ : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.Iter.flatMapAfterM.{w, w'}
  {α β α₂ γ : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [MonadAttach m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ]
  (f : β → m ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) (it₁ : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β)
  (it₂ : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

Let `it₁` and `it₂` be iterators and `f` a monadic function mapping `it₁`'s outputs to iterators of the same type as `it₂`. Then `it₁.[flatMapAfterM](Iterators/Iterator-Combinators/#Std___Iter___flatMapAfterM "Documentation for Std.Iter.flatMapAfterM") f it₂` first goes over `it₂` and then over `it₁.flatMap f it₂`, emitting all their values.
The main purpose of this combinator is to represent the intermediate state of a `flatMap` iterator that is currently iterating over one of the inner iterators.
**Marble diagram (without monadic effects):**

```
it₁                            --b      c    --d -⊥
it₂                      a1-a2⊥
f b                               b1-b2⊥
f c                                      c1-c2⊥
f d                                             ⊥
it.flatMapAfterM f it₂   a1-a2----b1-b2--c1-c2----⊥

```

**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it₁`, `it₂` and the inner iterators are finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it₁` is finite and `it₂` and the inner iterators are productive


For certain functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided out of the box. For example, if the outer iterator is productive and the inner iterators are productive _and provably never empty_ , then the resulting iterator is also productive.
**Performance:**
This combinator incurs an additional O(1) cost with each output of `it₁`, `it₂` or an internal iterator.
For each value emitted by the outer iterator `it₁`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.filter "Permalink")def
```


Std.Iter.filter.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (f : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.Iter.filter.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (f : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

If `it` is an iterator, then `it.[filter](Iterators/Iterator-Combinators/#Std___Iter___filter "Documentation for Std.Iter.filter") f` is another iterator that applies a predicate `f` to all values emitted by `it` and emits them only if they are accepted by `f`.
In situations where `f` is monadic, use `filterM` instead.
**Marble diagram (without monadic effects):**
`it            ---a--b--c--d-e--⊥ it.filter     ---a-----c-------⊥`
(given that `f a = f c = true` and `f b = f d = d e = false`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite`


For certain mapping functions `f`, the resulting iterator will be productive even though no `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance is provided. For example, if `f` always returns `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`, the resulting iterator will be productive as long as `it` is. In such situations, the missing instance needs to be proved manually.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f` and matches on the returned value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.filterM "Permalink")def
```


Std.Iter.filterM.{w, w'} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m]
  (f : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.Iter.filterM.{w, w'} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m]
  (f : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

If `it` is an iterator, then `it.[filterM](Iterators/Iterator-Combinators/#Std___Iter___filterM "Documentation for Std.Iter.filterM") f` is another iterator that applies a monadic predicate `f` to all values emitted by `it` and emits them only if they are accepted by `f`.
If `f` is pure, then the simpler variant `it.[filter](Iterators/Iterator-Combinators/#Std___Iter___filter "Documentation for Std.Iter.filter")` can be used instead.
**Marble diagram (without monadic effects):**
`it             ---a--b--c--d-e--⊥ it.filterM     ---a-----c-------⊥`
(given that `f a = f c = pure true` and `f b = f d = d e = pure false`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite`


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.filterWithPostcondition` will be finite -- and productive -- even if `it` isn't. In such cases, the termination proof needs to be done manually.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.filterWithPostcondition "Permalink")def
```


Std.Iter.filterWithPostcondition.{w, w'} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.Iter.filterWithPostcondition.{w, w'}
  {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

_Note: This is a very general combinator that requires an advanced understanding of monads, dependent types and termination proofs. The variants`filter` and `filterM` are easier to use and sufficient for most use cases._
If `it` is an iterator, then `it.[filterWithPostcondition](Iterators/Iterator-Combinators/#Std___Iter___filterWithPostcondition "Documentation for Std.Iter.filterWithPostcondition") f` is another iterator that applies a monadic predicate `f` to all values emitted by `it` and emits them only if they are accepted by `f`.
`f` is expected to return `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))`, where `n` is an arbitrary monad. The `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT")` transformer allows the caller to intrinsically prove properties about `f`'s return value in the monad `n`, enabling termination proofs depending on the specific behavior of `f`.
**Marble diagram (without monadic effects):**
`it                             ---a--b--c--d-e--⊥ it.filterWithPostcondition     ---a-----c-------⊥`
(given that `f a = f c = pure true` and `f b = f d = d e = pure false`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite`


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.filterWithPostcondition` will be finite -- and productive -- even if `it` isn't.
In such situations, the missing instances can be proved manually if the postcondition bundled in the `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n` monad is strong enough. In the given example, a suitable postcondition might be `fun _ => [False](Basic-Propositions/Truth/#False "Documentation for False")`.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.filterMap "Permalink")def
```


Std.Iter.filterMap.{w} {α β γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  (f : β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ


Std.Iter.filterMap.{w} {α β γ : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (f : β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") γ


```

If `it` is an iterator, then `it.[filterMap](Iterators/Iterator-Combinators/#Std___Iter___filterMap "Documentation for Std.Iter.filterMap") f` is another iterator that applies a function `f` to all values emitted by `it`. `f` is expected to return an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`. If it returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then nothing is emitted; if it returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x`, then `x` is emitted.
In situations where `f` is monadic, use `filterMapM` instead.
**Marble diagram:**
`it               ---a --b--c --d-e--⊥ it.filterMap     ---a'-----c'-------⊥`
(given that `f a = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a'`, `f c = c'` and `f b = f d = d e = none`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite`


For certain mapping functions `f`, the resulting iterator will be productive even though no `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance is provided. For example, if `f` never returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then this combinator will preserve productiveness. In such situations, the missing instance needs to be proved manually.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f` and matches on the returned `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.filterMapM "Permalink")def
```


Std.Iter.filterMapM.{w, w'} {α β γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m]
  (f : β → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.Iter.filterMapM.{w, w'}
  {α β γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [MonadAttach m] (f : β → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

If `it` is an iterator, then `it.[filterMapM](Iterators/Iterator-Combinators/#Std___Iter___filterMapM "Documentation for Std.Iter.filterMapM") f` is another iterator that applies a monadic function `f` to all values emitted by `it`. `f` is expected to return an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` inside the monad. If `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then nothing is emitted; if it returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x`, then `x` is emitted.
If `f` is pure, then the simpler variant `it.[filterMap](Iterators/Iterator-Combinators/#Std___Iter___filterMap "Documentation for Std.Iter.filterMap")` can be used instead.
**Marble diagram (without monadic effects):**
`it                ---a --b--c --d-e--⊥ it.filterMapM     ---a'-----c'-------⊥`
(given that `f a = pure (some a)'`, `f c = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") c')` and `f b = f d = d e = pure none`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite`


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` never returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then this combinator will preserve productiveness. If `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.filterMapM` will be finite even if `it` isn't. In such cases, the termination proof needs to be done manually.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f` and matches on the returned `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.filterMapWithPostcondition "Permalink")def
```


Std.Iter.filterMapWithPostcondition.{w, w'} {α β γ : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.Iter.filterMapWithPostcondition.{w,
    w'}
  {α β γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

_Note: This is a very general combinator that requires an advanced understanding of monads, dependent types and termination proofs. The variants`filterMap` and `filterMapM` are easier to use and sufficient for most use cases._
If `it` is an iterator, then `it.[filterMapWithPostcondition](Iterators/Iterator-Combinators/#Std___Iter___filterMapWithPostcondition "Documentation for Std.Iter.filterMapWithPostcondition") f` is another iterator that applies a monadic function `f` to all values emitted by `it`. `f` is expected to return an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` inside the monad. If `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then nothing is emitted; if it returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x`, then `x` is emitted.
`f` is expected to return `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") _)`, where `n` is an arbitrary monad. The `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT")` transformer allows the caller to intrinsically prove properties about `f`'s return value in the monad `n`, enabling termination proofs depending on the specific behavior of `f`.
**Marble diagram (without monadic effects):**
`it                                ---a --b--c --d-e--⊥ it.filterMapWithPostcondition     ---a'-----c'-------⊥`
(given that `f a = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a')`, `f c = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") c')` and `f b = f d = d e = pure none`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` never returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then this combinator will preserve productiveness. If `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.filterMapWithPostcondition` will be finite even if `it` isn't. In the first case, consider using the `map`/`mapM`/`mapWithPostcondition` combinators instead, which provide more instances out of the box.
In such situations, the missing instances can be proved manually if the postcondition bundled in the `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n` monad is strong enough. If `f` always returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") _`, a suitable postcondition is `fun x => x.isSome`; if `f` always fails, a suitable postcondition might be `fun _ => [False](Basic-Propositions/Truth/#False "Documentation for False")`.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f` and matches on the returned `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.zip "Permalink")def
```


Std.Iter.zip.{w} {α₁ β₁ α₂ β₂ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₁ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β₁]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β₂] (left : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β₁) (right : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β₂) :
  [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")β₁ [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β₂[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.Iter.zip.{w} {α₁ β₁ α₂ β₂ : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₁ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β₁] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β₂]
  (left : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β₁) (right : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β₂) :
  [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")β₁ [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β₂[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Given two iterators `left` and `right`, `left.[zip](Iterators/Iterator-Combinators/#Std___Iter___zip "Documentation for Std.Iter.zip") right` is an iterator that yields pairs of outputs of `left` and `right`. When one of them terminates, the `zip` iterator will also terminate.
**Marble diagram:**
`left               --a        ---b        --c right                 --x         --y        --⊥ left.zip right     -----(a, x)------(b, y)-----⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if either `left` or `right` is finite and the other is productive
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `left` and `right` are productive


There are situations where `left.[zip](Iterators/Iterator-Combinators/#Std___Iter___zip "Documentation for Std.Iter.zip") right` is finite (or productive) but none of the instances above applies. For example, if `left` immediately terminates but `right` always skips, then `left.[zip](Iterators/Iterator-Combinators/#Std___Iter___zip "Documentation for Std.Iter.zip").right` is finite even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or even `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is available. Such instances need to be proved manually.
**Performance:**
This combinator incurs an additional O(1) cost with each step taken by `left` or `right`.
Right now, the compiler does not unbox the internal state, leading to worse performance than theoretically possible.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.attachWith "Permalink")def
```


Std.Iter.attachWith.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β)
  (P : β → Prop)
  (h : ∀ (out : β), it.[IsPlausibleIndirectOutput](Iterators/Reasoning-About-Iterators/#Std___Iter___IsPlausibleIndirectOutput___direct "Documentation for Std.Iter.IsPlausibleIndirectOutput") out → P out) :
  [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") out [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P out [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


Std.Iter.attachWith.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β)
  (P : β → Prop)
  (h :
    ∀ (out : β),
      it.[IsPlausibleIndirectOutput](Iterators/Reasoning-About-Iterators/#Std___Iter___IsPlausibleIndirectOutput___direct "Documentation for Std.Iter.IsPlausibleIndirectOutput") out →
        P out) :
  [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") out [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P out [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


```

“Attaches” individual proofs to an iterator of values that satisfy a predicate `P`, returning an iterator with values in the corresponding subtype `{ x // P x }`.
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if the base iterator is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if the base iterator is productive


##  22.4.2. Monadic Combinators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Iterator-Combinators--Monadic-Combinators "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.toIter "Permalink")def
```


Std.IterM.toIter.{w} {α β : Type w} (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.IterM.toIter.{w} {α β : Type w}
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β) : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

Converts a monadic iterator (`[IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β`) over `[Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")` into a pure iterator (`[Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.take "Permalink")def
```


Std.IterM.take.{w, w'} {α : Type w} {m : Type w → Type w'} {β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.take.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

Given an iterator `it` and a natural number `n`, `it.[take](Iterators/Iterator-Combinators/#Std___IterM___take "Documentation for Std.IterM.take") n` is an iterator that outputs up to the first `n` of `it`'s values in order and then terminates.
**Marble diagram:**
`it          ---a----b---c--d-e--⊥ it.take 3   ---a----b---c⊥  it          ---a--⊥ it.take 3   ---a--⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is productive
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


**Performance:**
This combinator incurs an additional O(1) cost with each output of `it`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.takeWhile "Permalink")def
```


Std.IterM.takeWhile.{w, w'} {α : Type w} {m : Type w → Type w'}
  {β : Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (P : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.takeWhile.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (P : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

Given an iterator `it` and a predicate `P`, `it.[takeWhile](Iterators/Iterator-Combinators/#Std___IterM___takeWhile "Documentation for Std.IterM.takeWhile") P` is an iterator that outputs the values emitted by `it` until one of those values is rejected by `P`. If some emitted value is rejected by `P`, the value is dropped and the iterator terminates.
In situations where `P` is monadic, use `takeWhileM` instead.
**Marble diagram (ignoring monadic effects):**
Assuming that the predicate `P` accepts `a` and `b` but rejects `c`:
`it               ---a----b---c--d-e--⊥ it.takeWhile P   ---a----b---⊥  it               ---a----⊥ it.takeWhile P   ---a----⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


Depending on `P`, it is possible that `it.[takeWhile](Iterators/Iterator-Combinators/#Std___IterM___takeWhile "Documentation for Std.IterM.takeWhile") P` is finite (or productive) although `it` is not. In this case, the `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance needs to be proved manually.
**Performance:**
This combinator calls `P` on each output of `it` until the predicate evaluates to false. Then it terminates.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.takeWhileM "Permalink")def
```


Std.IterM.takeWhileM.{w, w'} {α : Type w} {m : Type w → Type w'}
  {β : Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m] (P : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.takeWhileM.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m]
  (P : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

Given an iterator `it` and a monadic predicate `P`, `it.[takeWhileM](Iterators/Iterator-Combinators/#Std___IterM___takeWhileM "Documentation for Std.IterM.takeWhileM") P` is an iterator that outputs the values emitted by `it` until one of those values is rejected by `P`. If some emitted value is rejected by `P`, the value is dropped and the iterator terminates.
If `P` is pure, then the simpler variant `takeWhile` can be used instead.
**Marble diagram (ignoring monadic effects):**
Assuming that the predicate `P` accepts `a` and `b` but rejects `c`:
`it                ---a----b---c--d-e--⊥ it.takeWhileM P   ---a----b---⊥  it                ---a----⊥ it.takeWhileM P   ---a----⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


Depending on `P`, it is possible that `it.[takeWhileM](Iterators/Iterator-Combinators/#Std___IterM___takeWhileM "Documentation for Std.IterM.takeWhileM") P` is finite (or productive) although `it` is not. In this case, the `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance needs to be proved manually.
**Performance:**
This combinator calls `P` on each output of `it` until the predicate evaluates to false. Then it terminates.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.takeWhileWithPostcondition "Permalink")def
```


Std.IterM.takeWhileWithPostcondition.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  (P : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.takeWhileWithPostcondition.{w,
    w'}
  {α : Type w} {m : Type w → Type w'}
  {β : Type w}
  (P : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

_Note: This is a very general combinator that requires an advanced understanding of monads, dependent types and termination proofs. The variants`takeWhile` and `takeWhileM` are easier to use and sufficient for most use cases._
Given an iterator `it` and a monadic predicate `P`, `it.[takeWhileWithPostcondition](Iterators/Iterator-Combinators/#Std___IterM___takeWhileWithPostcondition "Documentation for Std.IterM.takeWhileWithPostcondition") P` is an iterator that emits the values emitted by `it` until one of those values is rejected by `P`. If some emitted value is rejected by `P`, the value is dropped and the iterator terminates.
`P` is expected to return `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))`. The `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT")` transformer allows the caller to intrinsically prove properties about `P`'s return value in the monad `m`, enabling termination proofs depending on the specific behavior of `P`.
**Marble diagram (ignoring monadic effects):**
Assuming that the predicate `P` accepts `a` and `b` but rejects `c`:
`it                                ---a----b---c--d-e--⊥ it.takeWhileWithPostcondition P   ---a----b---⊥  it                                ---a----⊥ it.takeWhileWithPostcondition P   ---a----⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


Depending on `P`, it is possible that `it.[takeWhileWithPostcondition](Iterators/Iterator-Combinators/#Std___IterM___takeWhileWithPostcondition "Documentation for Std.IterM.takeWhileWithPostcondition") P` is finite (or productive) although `it` is not. In this case, the `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance needs to be proved manually.
**Performance:**
This combinator calls `P` on each output of `it` until the predicate evaluates to false. Then it terminates.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.toTake "Permalink")def
```


Std.IterM.toTake.{w, w'} {α : Type w} {m : Type w → Type w'}
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.toTake.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α m]
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

This combinator is only useful for advanced use cases.
Given a finite iterator `it`, returns an iterator that behaves exactly like `it` but is of the same type as `it.[take](Iterators/Iterator-Combinators/#Std___IterM___take "Documentation for Std.IterM.take") n`.
**Marble diagram:**
`it          ---a----b---c--d-e--⊥ it.toTake   ---a----b---c--d-e--⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: always
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: always


**Performance:**
This combinator incurs an additional O(1) cost with each output of `it`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.drop "Permalink")def
```


Std.IterM.drop.{w, w'} {α : Type w} {m : Type w → Type w'} {β : Type w}
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.drop.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

Given an iterator `it` and a natural number `n`, `it.[drop](Iterators/Iterator-Combinators/#Std___IterM___drop "Documentation for Std.IterM.drop") n` is an iterator that forwards all of `it`'s output values except for the first `n`.
**Marble diagram:**
`it          ---a----b---c--d-e--⊥ it.drop 3   ---------------d-e--⊥  it          ---a--⊥ it.drop 3   ------⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


**Performance:**
Currently, this combinator incurs an additional O(1) cost with each output of `it`, even when the iterator does not drop any elements anymore.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.dropWhile "Permalink")def
```


Std.IterM.dropWhile.{w, w'} {α : Type w} {m : Type w → Type w'}
  {β : Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (P : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.dropWhile.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (P : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

Given an iterator `it` and a predicate `P`, `it.[dropWhile](Iterators/Iterator-Combinators/#Std___IterM___dropWhile "Documentation for Std.IterM.dropWhile") P` is an iterator that emits the values emitted by `it` starting from the first value that is rejected by `P`. The elements before are dropped.
In situations where `P` is monadic, use `dropWhileM` instead.
**Marble diagram (ignoring monadic effects):**
Assuming that the predicate `P` accepts `a` and `b` but rejects `c`:
`it               ---a----b---c--d-e--⊥ it.dropWhile P   ------------c--d-e--⊥  it               ---a----⊥ it.dropWhile P   --------⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite


**Performance:**
This combinator calls `P` on each output of `it` until the predicate evaluates to false. After that, the combinator incurs an addictional O(1) cost for each value emitted by `it`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.dropWhileM "Permalink")def
```


Std.IterM.dropWhileM.{w, w'} {α : Type w} {m : Type w → Type w'}
  {β : Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m] (P : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.dropWhileM.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m]
  (P : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

Given an iterator `it` and a monadic predicate `P`, `it.[dropWhileM](Iterators/Iterator-Combinators/#Std___IterM___dropWhileM "Documentation for Std.IterM.dropWhileM") P` is an iterator that emits the values emitted by `it` starting from the first value that is rejected by `P`. The elements before are dropped.
If `P` is pure, then the simpler variant `dropWhile` can be used instead.
**Marble diagram (ignoring monadic effects):**
Assuming that the predicate `P` accepts `a` and `b` but rejects `c`:
`it                ---a----b---c--d-e--⊥ it.dropWhileM P   ------------c--d-e--⊥  it                ---a----⊥ it.dropWhileM P   --------⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite


Depending on `P`, it is possible that `it.[dropWhileM](Iterators/Iterator-Combinators/#Std___IterM___dropWhileM "Documentation for Std.IterM.dropWhileM") P` is finite (or productive) although `it` is not. In this case, the `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance needs to be proved manually.
**Performance:**
This combinator calls `P` on each output of `it` until the predicate evaluates to false. After that, the combinator incurs an addictional O(1) cost for each value emitted by `it`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.dropWhileWithPostcondition "Permalink")def
```


Std.IterM.dropWhileWithPostcondition.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  (P : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.dropWhileWithPostcondition.{w,
    w'}
  {α : Type w} {m : Type w → Type w'}
  {β : Type w}
  (P : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

_Note: This is a very general combinator that requires an advanced understanding of monads, dependent types and termination proofs. The variants`dropWhile` and `dropWhileM` are easier to use and sufficient for most use cases._
Given an iterator `it` and a monadic predicate `P`, `it.[dropWhileWithPostcondition](Iterators/Iterator-Combinators/#Std___IterM___dropWhileWithPostcondition "Documentation for Std.IterM.dropWhileWithPostcondition") P` is an iterator that emits the values emitted by `it` starting from the first value that is rejected by `P`. The elements before are dropped.
`P` is expected to return `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))`. The `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT")` transformer allows the caller to intrinsically prove properties about `P`'s return value in the monad `m`, enabling termination proofs depending on the specific behavior of `P`.
**Marble diagram (ignoring monadic effects):**
Assuming that the predicate `P` accepts `a` and `b` but rejects `c`:
`it                                ---a----b---c--d-e--⊥ it.dropWhileWithPostcondition P   ------------c--d-e--⊥  it                                ---a----⊥ it.dropWhileWithPostcondition P   --------⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite


Depending on `P`, it is possible that `it.[dropWhileWithPostcondition](Iterators/Iterator-Combinators/#Std___IterM___dropWhileWithPostcondition "Documentation for Std.IterM.dropWhileWithPostcondition") P` is finite (or productive) although `it` is not. In this case, the `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance needs to be proved manually.
**Performance:**
This combinator calls `P` on each output of `it` until the predicate evaluates to false. After that, the combinator incurs an additional O(1) cost for each value emitted by `it`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.stepSize "Permalink")def
```


Std.IterM.stepSize.{u_1, u_2} {α : Type u_1} {m : Type u_1 → Type u_2}
  {β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess") α m] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.stepSize.{u_1, u_2}
  {α : Type u_1} {m : Type u_1 → Type u_2}
  {β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess") α m] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

Produces an iterator that emits one value of `it`, then drops `n - 1` elements, then emits another value, and so on. In other words, it emits every `n`-th value of `it`, starting with the first one.
If `n = 0`, the iterator behaves like for `n = 1`: It emits all values of `it`.
**Marble diagram:**
`it               ---1----2----3---4----5 it.stepSize 2    ---1---------3--------5`
**Availability:**
This operation is currently only available for iterators implementing `[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess")`, such as `PRange.iter` range iterators.
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if the base iterator `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.map "Permalink")def
```


Std.IterM.map.{w, w'} {α β γ : Type w} {m : Type w → Type w'}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : β → γ) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.IterM.map.{w, w'} {α β γ : Type w}
  {m : Type w → Type w'} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : β → γ) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

If `it` is an iterator, then `it.[map](Iterators/Iterator-Combinators/#Std___IterM___map "Documentation for Std.IterM.map") f` is another iterator that applies a function `f` to all values emitted by `it` and emits the result.
In situations where `f` is monadic, use `mapM` instead.
**Marble diagram:**
`it         ---a --b --c --d -e ----⊥ it.map     ---a'--b'--c'--d'-e'----⊥`
(given that `f a = a'`, `f b = b'` etc.)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.mapM "Permalink")def
```


Std.IterM.mapM.{w, w', w''} {α β γ : Type w} {m : Type w → Type w'}
  {n : Type w → Type w''} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n] [MonadAttach n]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] (f : β → n γ) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n γ


Std.IterM.mapM.{w, w', w''}
  {α β γ : Type w} {m : Type w → Type w'}
  {n : Type w → Type w''} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n] [MonadAttach n]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] (f : β → n γ)
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n γ


```

If `it` is an iterator, then `it.[mapM](Iterators/Iterator-Combinators/#Std___IterM___mapM "Documentation for Std.IterM.mapM") f` is another iterator that applies a monadic function `f` to all values emitted by `it` and emits the result.
The base iterator `it` being monadic in `m`, `f` can return values in any monad `n` for which a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n` instance is available.
If `f` is pure, then the simpler variant `it.[map](Iterators/Iterator-Combinators/#Std___IterM___map "Documentation for Std.IterM.map")` can be used instead.
**Marble diagram (without monadic effects):**
`it          ---a --b --c --d -e ----⊥ it.mapM     ---a'--b'--c'--d'-e'----⊥`
(given that `f a = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") a'`, `f b = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") b'` etc.)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.mapM` will be finite even if `it` isn't. In such cases, the termination proof needs to be done manually.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.mapWithPostcondition "Permalink")def
```


Std.IterM.mapWithPostcondition.{w, w', w''} {α β γ : Type w}
  {m : Type w → Type w'} {n : Type w → Type w''} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n γ)
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n γ


Std.IterM.mapWithPostcondition.{w, w',
    w''}
  {α β γ : Type w} {m : Type w → Type w'}
  {n : Type w → Type w''} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n γ)
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n γ


```

_Note: This is a very general combinator that requires an advanced understanding of monads, dependent types and termination proofs. The variants`map` and `mapM` are easier to use and sufficient for most use cases._
If `it` is an iterator, then `it.[mapWithPostcondition](Iterators/Iterator-Combinators/#Std___IterM___mapWithPostcondition "Documentation for Std.IterM.mapWithPostcondition") f` is another iterator that applies a monadic function `f` to all values emitted by `it` and emits the result.
`f` is expected to return `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n _`. The base iterator `it` being monadic in `m`, `n` can be different from `m`, but `it.[mapWithPostcondition](Iterators/Iterator-Combinators/#Std___IterM___mapWithPostcondition "Documentation for Std.IterM.mapWithPostcondition") f` expects a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n` instance. The `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT")` transformer allows the caller to intrinsically prove properties about `f`'s return value in the monad `n`, enabling termination proofs depending on the specific behavior of `f`.
**Marble diagram (without monadic effects):**
`it                          ---a --b --c --d -e ----⊥ it.mapWithPostcondition     ---a'--b'--c'--d'-e'----⊥`
(given that `f a = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") a'`, `f b = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") b'` etc.)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is productive


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.mapWithPostcondition` will be finite even if `it` isn't.
In such situations, the missing instances can be proved manually if the postcondition bundled in the `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n` monad is strong enough. In the given example, a suitable postcondition might be `fun _ => [False](Basic-Propositions/Truth/#False "Documentation for False")`.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.uLift "Permalink")def
```


Std.IterM.uLift.{v, u, v', u'} {α β : Type u} {m : Type u → Type u'}
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) (n : Type (max u v) → Type v')
  [lift : [MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m (ULiftT n)] : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") β)


Std.IterM.uLift.{v, u, v', u'}
  {α β : Type u} {m : Type u → Type u'}
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β)
  (n : Type (max u v) → Type v')
  [lift : [MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m (ULiftT n)] :
  [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") β)


```

Transforms an `m`-monadic iterator with values in `β` into an `n`-monadic iterator with values in `[ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") β`. Requires a `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift") m (ULiftT n)` instance.
**Marble diagram:**
`it            ---a    ----b    ---c    --d    ---⊥ it.uLift n    ---.up a----.up b---.up c--.up d---⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")`: only if the original iterator is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`: only if the original iterator is productive


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.flatMap "Permalink")def
```


Std.IterM.flatMap.{w, w'} {α β α₂ γ : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ] (f : β → [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.IterM.flatMap.{w, w'}
  {α β α₂ γ : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ]
  (f : β → [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

Let `it` be an iterator and `f` a function mapping `it`'s outputs to iterators. Then `it.[flatMap](Iterators/Iterator-Combinators/#Std___IterM___flatMap "Documentation for Std.IterM.flatMap") f` is an iterator that goes over `it` and for each output, it applies `f` and iterates over the resulting iterator. `it.[flatMap](Iterators/Iterator-Combinators/#Std___IterM___flatMap "Documentation for Std.IterM.flatMap") f` emits all values obtained from the inner iterators -- first, all of the first inner iterator, then all of the second one, and so on.
**Marble diagram:**

```
it                 ---a      --b      c    --d -⊥
f a                    a1-a2⊥
f b                             b1-b2⊥
f c                                    c1-c2⊥
f d                                           ⊥
it.flatMap         ----a1-a2----b1-b2--c1-c2----⊥

```

**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` and the inner iterators are finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite and the inner iterators are productive


For certain functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided out of the box. For example, if the outer iterator is productive and the inner iterators are productive _and provably never empty_ , then the resulting iterator is also productive.
**Performance:**
This combinator incurs an additional O(1) cost with each output of `it` or an internal iterator.
For each value emitted by the outer iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.flatMapM "Permalink")def
```


Std.IterM.flatMapM.{w, w'} {α β α₂ γ : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ]
  (f : β → m ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.IterM.flatMapM.{w, w'}
  {α β α₂ γ : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [MonadAttach m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ]
  (f : β → m ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

Let `it` be an iterator and `f` a monadic function mapping `it`'s outputs to iterators. Then `it.[flatMapM](Iterators/Iterator-Combinators/#Std___IterM___flatMapM "Documentation for Std.IterM.flatMapM") f` is an iterator that goes over `it` and for each output, it applies `f` and iterates over the resulting iterator. `it.[flatMapM](Iterators/Iterator-Combinators/#Std___IterM___flatMapM "Documentation for Std.IterM.flatMapM") f` emits all values obtained from the inner iterators -- first, all of the first inner iterator, then all of the second one, and so on.
**Marble diagram (without monadic effects):**

```
it                 ---a      --b      c    --d -⊥
f a                    a1-a2⊥
f b                             b1-b2⊥
f c                                    c1-c2⊥
f d                                           ⊥
it.flatMapM        ----a1-a2----b1-b2--c1-c2----⊥

```

**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` and the inner iterators are finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite and the inner iterators are productive


For certain functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided out of the box. For example, if the outer iterator is productive and the inner iterators are productive _and provably never empty_ , then the resulting iterator is also productive.
**Performance:**
This combinator incurs an additional O(1) cost with each output of `it` or an internal iterator.
For each value emitted by the outer iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.flatMapAfter "Permalink")def
```


Std.IterM.flatMapAfter.{w, w'} {α β α₂ γ : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ]
  (f : β → [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ) (it₁ : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) (it₂ : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) :
  [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.IterM.flatMapAfter.{w, w'}
  {α β α₂ γ : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ]
  (f : β → [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ) (it₁ : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β)
  (it₂ : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

Let `it₁` and `it₂` be iterators and `f` a function mapping `it₁`'s outputs to iterators of the same type as `it₂`. Then `it₁.[flatMapAfter](Iterators/Iterator-Combinators/#Std___IterM___flatMapAfter "Documentation for Std.IterM.flatMapAfter") f it₂` first goes over `it₂` and then over `it₁.[flatMap](Iterators/Iterator-Combinators/#Std___IterM___flatMap "Documentation for Std.IterM.flatMap") f it₂`, emitting all their values.
The main purpose of this combinator is to represent the intermediate state of a `flatMap` iterator that is currently iterating over one of the inner iterators.
**Marble diagram:**

```
it₁                            --b      c    --d -⊥
it₂                      a1-a2⊥
f b                               b1-b2⊥
f c                                      c1-c2⊥
f d                                             ⊥
it.flatMapAfter  f it₂   a1-a2----b1-b2--c1-c2----⊥

```

**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it₁`, `it₂` and the inner iterators are finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it₁` is finite and `it₂` and the inner iterators are productive


For certain functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided out of the box. For example, if the outer iterator is productive and the inner iterators are productive _and provably never empty_ , then the resulting iterator is also productive.
**Performance:**
This combinator incurs an additional O(1) cost with each output of `it₁`, `it₂` or an internal iterator.
For each value emitted by the outer iterator `it₁`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.flatMapAfterM "Permalink")def
```


Std.IterM.flatMapAfterM.{w, w'} {α β α₂ γ : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadAttach m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ] (f : β → m ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) (it₁ : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β)
  (it₂ : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.IterM.flatMapAfterM.{w, w'}
  {α β α₂ γ : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [MonadAttach m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m γ]
  (f : β → m ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ))
  (it₁ : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β)
  (it₂ : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ)) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

Let `it₁` and `it₂` be iterators and `f` a monadic function mapping `it₁`'s outputs to iterators of the same type as `it₂`. Then `it₁.[flatMapAfterM](Iterators/Iterator-Combinators/#Std___IterM___flatMapAfterM "Documentation for Std.IterM.flatMapAfterM") f it₂` first goes over `it₂` and then over `it₁.flatMap f it₂`, emitting all their values.
The main purpose of this combinator is to represent the intermediate state of a `flatMap` iterator that is currently iterating over one of the inner iterators.
**Marble diagram (without monadic effects):**

```
it₁                            --b      c    --d -⊥
it₂                      a1-a2⊥
f b                               b1-b2⊥
f c                                      c1-c2⊥
f d                                             ⊥
it.flatMapAfterM f it₂   a1-a2----b1-b2--c1-c2----⊥

```

**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it₁`, `it₂` and the inner iterators are finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it₁` is finite and `it₂` and the inner iterators are productive


For certain functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided out of the box. For example, if the outer iterator is productive and the inner iterators are productive _and provably never empty_ , then the resulting iterator is also productive.
**Performance:**
This combinator incurs an additional O(1) cost with each output of `it₁`, `it₂` or an internal iterator.
For each value emitted by the outer iterator `it₁`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.filter "Permalink")def
```


Std.IterM.filter.{w, w'} {α β : Type w} {m : Type w → Type w'}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


Std.IterM.filter.{w, w'} {α β : Type w}
  {m : Type w → Type w'} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β


```

If `it` is an iterator, then `it.[filter](Iterators/Iterator-Combinators/#Std___IterM___filter "Documentation for Std.IterM.filter") f` is another iterator that applies a predicate `f` to all values emitted by `it` and emits them only if they are accepted by `f`.
In situations where `f` is monadic, use `filterM` instead.
**Marble diagram (without monadic effects):**
`it            ---a--b--c--d-e--⊥ it.filter     ---a-----c-------⊥`
(given that `f a = f c = true` and `f b = f d = d e = false`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite`


For certain mapping functions `f`, the resulting iterator will be productive even though no `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance is provided. For example, if `f` always returns `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`, the resulting iterator will be productive as long as `it` is. In such situations, the missing instance needs to be proved manually.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f` and matches on the returned value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.filterM "Permalink")def
```


Std.IterM.filterM.{w, w', w''} {α β : Type w} {m : Type w → Type w'}
  {n : Type w → Type w''} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n] [MonadAttach n]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] (f : β → n ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n β


Std.IterM.filterM.{w, w', w''}
  {α β : Type w} {m : Type w → Type w'}
  {n : Type w → Type w''} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n] [MonadAttach n]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n]
  (f : β → n ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n β


```

If `it` is an iterator, then `it.[filterM](Iterators/Iterator-Combinators/#Std___IterM___filterM "Documentation for Std.IterM.filterM") f` is another iterator that applies a monadic predicate `f` to all values emitted by `it` and emits them only if they are accepted by `f`.
The base iterator `it` being monadic in `m`, `f` can return values in any monad `n` for which a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n` instance is available.
If `f` is pure, then the simpler variant `it.[filter](Iterators/Iterator-Combinators/#Std___IterM___filter "Documentation for Std.IterM.filter")` can be used instead.
**Marble diagram (without monadic effects):**
`it             ---a--b--c--d-e--⊥ it.filterM     ---a-----c-------⊥`
(given that `f a = f c = pure true` and `f b = f d = d e = pure false`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite`


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.filterWithPostcondition` will be finite -- and productive -- even if `it` isn't. In such cases, the termination proof needs to be done manually.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.filterWithPostcondition "Permalink")def
```


Std.IterM.filterWithPostcondition.{w, w', w''} {α β : Type w}
  {m : Type w → Type w'} {n : Type w → Type w''} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n β


Std.IterM.filterWithPostcondition.{w, w',
    w''}
  {α β : Type w} {m : Type w → Type w'}
  {n : Type w → Type w''} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n β


```

_Note: This is a very general combinator that requires an advanced understanding of monads, dependent types and termination proofs. The variants`filter` and `filterM` are easier to use and sufficient for most use cases._
If `it` is an iterator, then `it.[filterWithPostcondition](Iterators/Iterator-Combinators/#Std___IterM___filterWithPostcondition "Documentation for Std.IterM.filterWithPostcondition") f` is another iterator that applies a monadic predicate `f` to all values emitted by `it` and emits them only if they are accepted by `f`.
`f` is expected to return `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))`. The base iterator `it` being monadic in `m`, `n` can be different from `m`, but `it.[filterWithPostcondition](Iterators/Iterator-Combinators/#Std___IterM___filterWithPostcondition "Documentation for Std.IterM.filterWithPostcondition") f` expects a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n` instance. The `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT")` transformer allows the caller to intrinsically prove properties about `f`'s return value in the monad `n`, enabling termination proofs depending on the specific behavior of `f`.
**Marble diagram (without monadic effects):**
`it                             ---a--b--c--d-e--⊥ it.filterWithPostcondition     ---a-----c-------⊥`
(given that `f a = f c = pure true` and `f b = f d = d e = pure false`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite`


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.filterWithPostcondition` will be finite -- and productive -- even if `it` isn't.
In such situations, the missing instances can be proved manually if the postcondition bundled in the `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n` monad is strong enough. In the given example, a suitable postcondition might be `fun _ => [False](Basic-Propositions/Truth/#False "Documentation for False")`.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.filterMap "Permalink")def
```


Std.IterM.filterMap.{w, w'} {α β γ : Type w} {m : Type w → Type w'}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


Std.IterM.filterMap.{w, w'}
  {α β γ : Type w} {m : Type w → Type w'}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m γ


```

If `it` is an iterator, then `it.[filterMap](Iterators/Iterator-Combinators/#Std___IterM___filterMap "Documentation for Std.IterM.filterMap") f` is another iterator that applies a function `f` to all values emitted by `it`. `f` is expected to return an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`. If it returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then nothing is emitted; if it returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x`, then `x` is emitted.
In situations where `f` is monadic, use `filterMapM` instead.
**Marble diagram:**
`it               ---a --b--c --d-e--⊥ it.filterMap     ---a'-----c'-------⊥`
(given that `f a = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a'`, `f c = c'` and `f b = f d = d e = none`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite`


For certain mapping functions `f`, the resulting iterator will be productive even though no `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance is provided. For example, if `f` never returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then this combinator will preserve productiveness. In such situations, the missing instance needs to be proved manually.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f` and matches on the returned `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.filterMapM "Permalink")def
```


Std.IterM.filterMapM.{w, w', w''} {α β γ : Type w}
  {m : Type w → Type w'} {n : Type w → Type w''} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n] [MonadAttach n] [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] (f : β → n ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n γ


Std.IterM.filterMapM.{w, w', w''}
  {α β γ : Type w} {m : Type w → Type w'}
  {n : Type w → Type w''} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n] [MonadAttach n]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] (f : β → n ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n γ


```

If `it` is an iterator, then `it.[filterMapM](Iterators/Iterator-Combinators/#Std___IterM___filterMapM "Documentation for Std.IterM.filterMapM") f` is another iterator that applies a monadic function `f` to all values emitted by `it`. `f` is expected to return an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` inside the monad. If `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then nothing is emitted; if it returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x`, then `x` is emitted.
The base iterator `it` being monadic in `m`, `f` can return values in any monad `n` for which a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n` instance is available.
If `f` is pure, then the simpler variant `it.[filterMap](Iterators/Iterator-Combinators/#Std___IterM___filterMap "Documentation for Std.IterM.filterMap")` can be used instead.
**Marble diagram (without monadic effects):**
`it                ---a --b--c --d-e--⊥ it.filterMapM     ---a'-----c'-------⊥`
(given that `f a = pure (some a)'`, `f c = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") c')` and `f b = f d = d e = pure none`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite`


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` never returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then this combinator will preserve productiveness. If `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.filterMapM` will be finite even if `it` isn't. In such cases, the termination proof needs to be done manually.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f` and matches on the returned `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.filterMapWithPostcondition "Permalink")def
```


Std.IterM.filterMapWithPostcondition.{w, w', w''} {α β γ : Type w}
  {m : Type w → Type w'} {n : Type w → Type w''} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n γ


Std.IterM.filterMapWithPostcondition.{w,
    w', w''}
  {α β γ : Type w} {m : Type w → Type w'}
  {n : Type w → Type w''} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  (f : β → [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") n γ


```

_Note: This is a very general combinator that requires an advanced understanding of monads, dependent types and termination proofs. The variants`filterMap` and `filterMapM` are easier to use and sufficient for most use cases._
If `it` is an iterator, then `it.[filterMapWithPostcondition](Iterators/Iterator-Combinators/#Std___IterM___filterMapWithPostcondition "Documentation for Std.IterM.filterMapWithPostcondition") f` is another iterator that applies a monadic function `f` to all values emitted by `it`. `f` is expected to return an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` inside the monad. If `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then nothing is emitted; if it returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x`, then `x` is emitted.
`f` is expected to return `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") _)`. The base iterator `it` being monadic in `m`, `n` can be different from `m`, but `it.[filterMapWithPostcondition](Iterators/Iterator-Combinators/#Std___IterM___filterMapWithPostcondition "Documentation for Std.IterM.filterMapWithPostcondition") f` expects a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n` instance. The `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT")` transformer allows the caller to intrinsically prove properties about `f`'s return value in the monad `n`, enabling termination proofs depending on the specific behavior of `f`.
**Marble diagram (without monadic effects):**
`it                                ---a --b--c --d-e--⊥ it.filterMapWithPostcondition     ---a'-----c'-------⊥`
(given that `f a = pure (some a)'`, `f c = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") c')` and `f b = f d = d e = pure none`)
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if `it` is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `it` is finite


For certain mapping functions `f`, the resulting iterator will be finite (or productive) even though no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance is provided. For example, if `f` never returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then this combinator will preserve productiveness. If `f` is an `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` monad and will always fail, then `it.filterMapWithPostcondition` will be finite even if `it` isn't. In the first case, consider using the `map`/`mapM`/`mapWithPostcondition` combinators instead, which provide more instances out of the box.
In such situations, the missing instances can be proved manually if the postcondition bundled in the `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") n` monad is strong enough. If `f` always returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") _`, a suitable postcondition is `fun x => x.isSome`; if `f` always fails, a suitable postcondition might be `fun _ => [False](Basic-Propositions/Truth/#False "Documentation for False")`.
**Performance:**
For each value emitted by the base iterator `it`, this combinator calls `f` and matches on the returned `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.zip "Permalink")def
```


Std.IterM.zip.{w, w'} {m : Type w → Type w'} {α₁ β₁ : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₁ m β₁] {α₂ β₂ : Type w} (left : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β₁)
  (right : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β₂) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")β₁ [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β₂[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.IterM.zip.{w, w'}
  {m : Type w → Type w'} {α₁ β₁ : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₁ m β₁] {α₂ β₂ : Type w}
  (left : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β₁)
  (right : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β₂) : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")β₁ [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β₂[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Given two iterators `left` and `right`, `left.[zip](Iterators/Iterator-Combinators/#Std___IterM___zip "Documentation for Std.IterM.zip") right` is an iterator that yields pairs of outputs of `left` and `right`. When one of them terminates, the `zip` iterator will also terminate.
**Marble diagram:**
`left               --a        ---b        --c right                 --x         --y        --⊥ left.zip right     -----(a, x)------(b, y)-----⊥`
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if either `left` or `right` is finite and the other is productive
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if `left` and `right` are productive


There are situations where `left.[zip](Iterators/Iterator-Combinators/#Std___IterM___zip "Documentation for Std.IterM.zip") right` is finite (or productive) but none of the instances above applies. For example, if the computation happens in an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except")` monad and `left` immediately fails when calling `step`, then `left.[zip](Iterators/Iterator-Combinators/#Std___IterM___zip "Documentation for Std.IterM.zip") right` will also do so. In such a case, the `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` (or `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`) instance needs to be proved manually.
**Performance:**
This combinator incurs an additional O(1) cost with each step taken by `left` or `right`.
Right now, the compiler does not unbox the internal state, leading to worse performance than possible.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.attachWith "Permalink")def
```


Std.IterM.attachWith.{w, w'} {α β : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) (P : β → Prop)
  (h : ∀ (out : β), it.IsPlausibleIndirectOutput out → P out) :
  [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") out [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P out [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


Std.IterM.attachWith.{w, w'}
  {α β : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) (P : β → Prop)
  (h :
    ∀ (out : β),
      it.IsPlausibleIndirectOutput out →
        P out) :
  [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") out [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P out [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


```

“Attaches” individual proofs to an iterator of values that satisfy a predicate `P`, returning an iterator with values in the corresponding subtype `{ x // P x }`.
**Termination properties:**
  * `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance: only if the base iterator is finite
  * `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")` instance: only if the base iterator is productive


[←22.3. Consuming Iterators](Iterators/Consuming-Iterators/#The-Lean-Language-Reference--Iterators--Consuming-Iterators "22.3. Consuming Iterators")[22.5. Reasoning About Iterators→](Iterators/Reasoning-About-Iterators/#The-Lean-Language-Reference--Iterators--Reasoning-About-Iterators "22.5. Reasoning About Iterators")

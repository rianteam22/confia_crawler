[←20.20. Subtypes](Basic-Types/Subtypes/#Subtype "20.20. Subtypes")[21. IO→](IO/#io "21. IO")
#  20.21. Lazy Computations[🔗](find/?domain=Verso.Genre.Manual.section&name=Thunk "Permalink")
A _thunk_ delays the computation of a value. In particular, the `[Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk")` type is used to delay the computation of a value in compiled code until it is explicitly requested—this request is called _forcing_ the thunk. The computed value is saved, so subsequent requests do not result in recomputation. Computing values at most once, when explicitly requested, is called _lazy evaluation_. This caching is invisible to Lean's logic, in which `[Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk")` is equivalent to a function from `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`.
##  20.21.1. Logical Model[🔗](find/?domain=Verso.Genre.Manual.section&name=Thunk-model "Permalink")
Thunks are modeled as a single-field structure that contains a function from `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`. The structure's field is private, so the function itself cannot be directly accessed. Instead, `[Thunk.get](Basic-Types/Lazy-Computations/#Thunk___get "Documentation for Thunk.get")` should be used. From the perspective of the logic, they are equivalent; `[Thunk.get](Basic-Types/Lazy-Computations/#Thunk___get "Documentation for Thunk.get")` exists to be overridden in the compiler by the platform primitive that implements lazy evaluation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Thunk.mk "Permalink")structure
```


Thunk.{u} (α : Type u) : Type u


Thunk.{u} (α : Type u) : Type u


```

Delays evaluation. The delayed code is evaluated at most once.
A thunk is code that constructs a value when it is requested via `[Thunk.get](Basic-Types/Lazy-Computations/#Thunk___get "Documentation for Thunk.get")`, `[Thunk.map](Basic-Types/Lazy-Computations/#Thunk___map "Documentation for Thunk.map")`, or `[Thunk.bind](Basic-Types/Lazy-Computations/#Thunk___bind "Documentation for Thunk.bind")`. The resulting value is cached, so the code is executed at most once. This is also known as lazy or call-by-need evaluation.
The Lean runtime has special support for the `[Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk")` type in order to implement the caching behavior.
#  Constructor

```
[Thunk.mk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk.mk").{u}
```

Constructs a new thunk from a function `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → α` that will be called when the thunk is first forced.
The result is cached. It is re-used when the thunk is forced again.
#  Fields

```
fn : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → α
```

Extract the getter function out of a thunk. Use `[Thunk.get](Basic-Types/Lazy-Computations/#Thunk___get "Documentation for Thunk.get")` instead.
##  20.21.2. Runtime Representation[🔗](find/?domain=Verso.Genre.Manual.section&name=Thunk-runtime "Permalink")
Memory layout of thunks
Thunks are one of the primitive object types supported by the Lean runtime. The object header contains a specific tag that indicates that an object is a thunk.
Thunks have two fields:
  * `m_value` is a pointer to a saved value, which is a null pointer if the value has not yet been computed.
  * `m_closure` is a closure which is to be called when the value should be computed.


The runtime system maintains the invariant that either the closure or the saved value is a null pointer. If both are null pointers, then the thunk is being forced on another thread.
When a thunk is [forced](Basic-Types/Lazy-Computations/#--tech-term-forcing), the runtime system first checks whether the saved value has already been computed, returning it if so. Otherwise, it attempts to acquire a lock on the closure by atomically swapping it with a null pointer. If the lock is acquired, it is invoked to compute the value; the computed value is stored in the saved value field and the reference to the closure is dropped. If not, then another thread is already computing the value; the system waits until it is computed.
##  20.21.3. Coercions[🔗](find/?domain=Verso.Genre.Manual.section&name=Thunk-coercions "Permalink")
There is a coercion from any type `α` to `[Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") α` that converts a term `e` into `[Thunk.mk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk.mk") fun () => e`. Because the elaborator [unfolds coercions](Coercions/Coercion-Insertion/#coercion-insertion), evaluation of the original term `e` is delayed; the coercion is not equivalent to `[Thunk.pure](Basic-Types/Lazy-Computations/#Thunk___pure "Documentation for Thunk.pure")`.
Lazy Lists
Lazy lists are lists that may contain thunks. The `[delayed](Basic-Types/Lazy-Computations/#LazyList___delayed-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example")` constructor causes part of the list to be computed on demand.
`inductive LazyList (α : Type u) where   | nil   | cons : α → [LazyList](Basic-Types/Lazy-Computations/#LazyList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") α → [LazyList](Basic-Types/Lazy-Computations/#LazyList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") α   | delayed : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") ([LazyList](Basic-Types/Lazy-Computations/#LazyList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") α) → [LazyList](Basic-Types/Lazy-Computations/#LazyList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") α deriving [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") `
Lazy lists can be converted to ordinary lists by forcing all the embedded thunks.
`def LazyList.toList : [LazyList](Basic-Types/Lazy-Computations/#LazyList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α   | [.nil](Basic-Types/Lazy-Computations/#LazyList___nil-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") => []   | [.cons](Basic-Types/Lazy-Computations/#LazyList___cons-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") x xs => x :: xs.[toList](Basic-Types/Lazy-Computations/#LazyList___toList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example")   | [.delayed](Basic-Types/Lazy-Computations/#LazyList___delayed-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") xs => xs.[get](Basic-Types/Lazy-Computations/#Thunk___get "Documentation for Thunk.get").[toList](Basic-Types/Lazy-Computations/#LazyList___toList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") `
Many operations on lazy lists can be implemented without forcing the embedded thunks, instead building up further thunks. The body of `[delayed](Basic-Types/Lazy-Computations/#LazyList___delayed-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example")` does not need to be an explicit call to `[Thunk.mk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk.mk")` because of the coercion.
`def LazyList.take : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [LazyList](Basic-Types/Lazy-Computations/#LazyList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") α → [LazyList](Basic-Types/Lazy-Computations/#LazyList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") α   | 0, _ => .nil   | _, [.nil](Basic-Types/Lazy-Computations/#LazyList___nil-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") => .nil   | n + 1, [.cons](Basic-Types/Lazy-Computations/#LazyList___cons-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") x xs => [.cons](Basic-Types/Lazy-Computations/#LazyList___cons-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") x <| [.delayed](Basic-Types/Lazy-Computations/#LazyList___delayed-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") <| [take](Basic-Types/Lazy-Computations/#LazyList___take-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") n xs   | n + 1, [.delayed](Basic-Types/Lazy-Computations/#LazyList___delayed-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") xs => [.delayed](Basic-Types/Lazy-Computations/#LazyList___delayed-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") <| [take](Basic-Types/Lazy-Computations/#LazyList___take-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") (n + 1) xs.[get](Basic-Types/Lazy-Computations/#Thunk___get "Documentation for Thunk.get")  def LazyList.ofFn (f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → α) : [LazyList](Basic-Types/Lazy-Computations/#LazyList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") α :=   [Fin.foldr](Basic-Types/Finite-Natural-Numbers/#Fin___foldr "Documentation for Fin.foldr") n (init := [.nil](Basic-Types/Lazy-Computations/#LazyList___nil-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example")) fun i xs =>     [.delayed](Basic-Types/Lazy-Computations/#LazyList___delayed-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") <| [LazyList.cons](Basic-Types/Lazy-Computations/#LazyList___cons-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") (f i) xs  def LazyList.append (xs ys : [LazyList](Basic-Types/Lazy-Computations/#LazyList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") α) : [LazyList](Basic-Types/Lazy-Computations/#LazyList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") α :=   [.delayed](Basic-Types/Lazy-Computations/#LazyList___delayed-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") <|     [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") xs [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")     | [.nil](Basic-Types/Lazy-Computations/#LazyList___nil-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") => ys     | [.cons](Basic-Types/Lazy-Computations/#LazyList___cons-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") x xs' => [LazyList.cons](Basic-Types/Lazy-Computations/#LazyList___cons-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") x ([append](Basic-Types/Lazy-Computations/#LazyList___append-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") xs' ys)     | [.delayed](Basic-Types/Lazy-Computations/#LazyList___delayed-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") xs' => [append](Basic-Types/Lazy-Computations/#LazyList___append-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") xs'.[get](Basic-Types/Lazy-Computations/#Thunk___get "Documentation for Thunk.get") ys `
Laziness is ordinarily invisible to Lean programs: there is no way to check whether a thunk has been forced. However, ``Lean.Parser.Term.dbgTrace : term`
``dbg_trace` can be used to gain insight into thunk evaluation.
`def observe (tag : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   dbg_trace "{tag}: {i.[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")}"   i.[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val") `
The lazy lists `[xs](Basic-Types/Lazy-Computations/#xs-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example")` and `[ys](Basic-Types/Lazy-Computations/#ys-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example")` emit traces when evaluated.
`def xs := [LazyList.ofFn](Basic-Types/Lazy-Computations/#LazyList___ofFn-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") (n := 3) ([observe](Basic-Types/Lazy-Computations/#observe-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") "xs") def ys := [LazyList.ofFn](Basic-Types/Lazy-Computations/#LazyList___ofFn-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") (n := 3) ([observe](Basic-Types/Lazy-Computations/#observe-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") "ys") `
Converting `[xs](Basic-Types/Lazy-Computations/#xs-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example")` to an ordinary list forces all of the embedded thunks:
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")``xs: 0 xs: 1 xs: 2 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [xs](Basic-Types/Lazy-Computations/#xs-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example").[toList](Basic-Types/Lazy-Computations/#LazyList___toList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") `
```
xs: 0
xs: 1
xs: 2

```

```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

Likewise, converting `[xs](Basic-Types/Lazy-Computations/#xs-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example").[append](Basic-Types/Lazy-Computations/#LazyList___append-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") [ys](Basic-Types/Lazy-Computations/#ys-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example")` to an ordinary list forces the embedded thunks:
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")``xs: 0 xs: 1 xs: 2 ys: 0 ys: 1 ys: 2 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [xs](Basic-Types/Lazy-Computations/#xs-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example").[append](Basic-Types/Lazy-Computations/#LazyList___append-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") [ys](Basic-Types/Lazy-Computations/#ys-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") |>.[toList](Basic-Types/Lazy-Computations/#LazyList___toList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") `
```
xs: 0
xs: 1
xs: 2
ys: 0
ys: 1
ys: 2

```

```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

Appending `[xs](Basic-Types/Lazy-Computations/#xs-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example")` to itself before forcing the thunks results in a single set of traces, because each thunk's code is evaluated just once:
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")``xs: 0 xs: 1 xs: 2 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [xs](Basic-Types/Lazy-Computations/#xs-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example").[append](Basic-Types/Lazy-Computations/#LazyList___append-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") [xs](Basic-Types/Lazy-Computations/#xs-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") |>.[toList](Basic-Types/Lazy-Computations/#LazyList___toList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") `
```
xs: 0
xs: 1
xs: 2

```

```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

Finally, taking a prefix of `[xs](Basic-Types/Lazy-Computations/#xs-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example").[append](Basic-Types/Lazy-Computations/#LazyList___append-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") [ys](Basic-Types/Lazy-Computations/#ys-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example")` results in only some of the thunks in `[ys](Basic-Types/Lazy-Computations/#ys-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example")` being evaluated:
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")``xs: 0 xs: 1 xs: 2 ys: 0 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [xs](Basic-Types/Lazy-Computations/#xs-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example").[append](Basic-Types/Lazy-Computations/#LazyList___append-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") [ys](Basic-Types/Lazy-Computations/#ys-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") |>.[take](Basic-Types/Lazy-Computations/#LazyList___take-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") 4 |>.[toList](Basic-Types/Lazy-Computations/#LazyList___toList-_LPAR_in-Lazy-Lists_RPAR_ "Definition of example") `
```
xs: 0
xs: 1
xs: 2
ys: 0

```

```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAGQIYC8CergGcZkAKQRuBkAuZAFWwAcUIBKZAdwAtEAnRAKGWQAfZCGAAbfkORQA9iHyVk5QEmEaLLgJEVanHkJLJwsIjHpsiMIursIIANYkMuzUpaqnG/aV7GuCUADmyACSIOzoAEbAMBa8PogAZjqeMAB0MDJ6RFQeWUrI7i7eAsKpomLIALwAfMgA2gC6hsipsvLIAB6dCjWdlFQd+OmZms2pxqbmloNVtYOpAYhpGVlxxkm5munodihUAHLoRO7qedqbXs0ADAA0yAD6sy3lzfd3ZeJPHxIlIsgA1MgAIzvNoKLozXqtOTg5AAHlKEzMFnhwhgOxQIG6zSxgJBLSRU26X0JKIRyHRuxIuOBLHmixga0SySyqRkCQAYljiEkqBzQH9VKQWDlTkVKJVJPyQKkEjIxGAuH9iKBohLnuIWAlbMhgMSapIBOMTMjLOSLmkwSQksA6fgmRsxYRUug6AxwCQZtgFKLnF4RSzxRRJUbSWbBIbkABbI5QdjE1jRdiR0rlJ7elMtK0Q/AAcieFuh7S6xFd7umeeQ3qYmeNkxRg3zvTLiA9jYWSyr9viSRkEXw3CQJHRQSoAGUYH4QAEWCrFNKRAHDtkQ8gwBEAvdJ+goCgAEQAbxHAF8qAfgKl4OgxMe95IL1eJD3icHA872VzqeqAMyzvsDrghz3QY9xrdYu3VQsP25LFX1/Eh/0HfdvVAuIAGJEEfbphlWXgMKw+YWw9b0hGqHDRjwzDr2woiK1I8jCHQqiKkIt1W0sEjBDIykUAAFnolZNCAA"\))
##  20.21.4. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=Thunk-api "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Thunk.get "Permalink")def
```


Thunk.get.{u_1} {α : Type u_1} (x : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") α) : α


Thunk.get.{u_1} {α : Type u_1}
  (x : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") α) : α


```

Gets the thunk's value. If the value is cached, it is returned in constant time; if not, it is computed.
Computed values are cached, so the value is not recomputed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Thunk.map "Permalink")def
```


Thunk.map.{u_1, u_2} {α : Type u_1} {β : Type u_2} (f : α → β)
  (x : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") α) : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") β


Thunk.map.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (f : α → β)
  (x : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") α) : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") β


```

Constructs a new thunk that forces `x` and then applies `x` to the result. Upon forcing, the result of `f` is cached and the reference to the thunk `x` is dropped.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Thunk.pure "Permalink")def
```


Thunk.pure.{u_1} {α : Type u_1} (a : α) : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") α


Thunk.pure.{u_1} {α : Type u_1} (a : α) :
  [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") α


```

Stores an already-computed value in a thunk.
Because the value has already been computed, there is no laziness.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Thunk.bind "Permalink")def
```


Thunk.bind.{u_1, u_2} {α : Type u_1} {β : Type u_2} (x : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") α)
  (f : α → [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") β) : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") β


Thunk.bind.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (x : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") α)
  (f : α → [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") β) : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") β


```

Constructs a new thunk that applies `f` to the result of `x` when forced.
[←20.20. Subtypes](Basic-Types/Subtypes/#Subtype "20.20. Subtypes")[21. IO→](IO/#io "21. IO")

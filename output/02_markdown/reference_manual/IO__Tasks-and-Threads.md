[←21.10. Random Numbers](IO/Random-Numbers/#The-Lean-Language-Reference--IO--Random-Numbers "21.10. Random Numbers")[22. Iterators→](Iterators/#iterators "22. Iterators")
#  21.11. Tasks and Threads[🔗](find/?domain=Verso.Genre.Manual.section&name=concurrency "Permalink")
_Tasks_ are the fundamental primitive for writing multi-threaded code. A `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α` represents a computation that, at some point, will [_resolve_](IO/Tasks-and-Threads/#--tech-term-resolving-next) to a value of type `α`; it may be computed on a separate thread. When a task has resolved, its value can be read; attempting to get the value of a task before it resolves causes the current thread to block until the task has resolved. Tasks are similar to promises in JavaScript, `JoinHandle` in Rust, and `Future` in Scala.
Tasks may either carry out pure computations or `[IO](IO/Logical-Model/#IO "Documentation for IO")` actions. The API of pure tasks resembles that of [thunks](Basic-Types/Lazy-Computations/#--tech-term-thunk): `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")` creates a `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α` from a function in `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → α`, and `[Task.get](IO/Tasks-and-Threads/#Task___get "Documentation for Task.get")` waits until the function's value has been computed and then returns it. The value is cached, so subsequent requests do not need to recompute it. The key difference lies in when the computation occurs: while the values of thunks are not computed until they are forced, tasks execute opportunistically in a separate thread.
Tasks in `[IO](IO/Logical-Model/#IO "Documentation for IO")` are created using `[IO.asTask](IO/Tasks-and-Threads/#IO___asTask "Documentation for IO.asTask")`. Similarly, `[BaseIO.asTask](IO/Tasks-and-Threads/#BaseIO___asTask "Documentation for BaseIO.asTask")` and `[EIO.asTask](IO/Tasks-and-Threads/#EIO___asTask "Documentation for EIO.asTask")` create tasks in other `[IO](IO/Logical-Model/#IO "Documentation for IO")` monads. These tasks may have side effects, and can communicate with other tasks.
When the last reference to a task is dropped it is _cancelled_. Pure tasks created with `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")` are terminated upon cancellation. Tasks spawned with `[IO.asTask](IO/Tasks-and-Threads/#IO___asTask "Documentation for IO.asTask")`, `[EIO.asTask](IO/Tasks-and-Threads/#EIO___asTask "Documentation for EIO.asTask")`, or `[BaseIO.asTask](IO/Tasks-and-Threads/#BaseIO___asTask "Documentation for BaseIO.asTask")` continue executing and must explicitly check for cancellation using `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")`. Tasks may be explicitly cancelled using `[IO.cancel](IO/Tasks-and-Threads/#IO___cancel "Documentation for IO.cancel")`.
The Lean runtime maintains a thread pool for running tasks. The size of the thread pool is determined by the environment variable `LEAN_NUM_THREADS` if it is set, or by the number of logical processors on the current machine otherwise. The size of the thread pool is not a hard limit; in certain situations it may be exceeded to avoid deadlocks. By default, these threads are used to run tasks; each task has a _priority_ (`[Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority")`), and higher-priority tasks take precedence over lower-priority tasks. Tasks may also be assigned to dedicated threads by spawning them with a sufficiently high priority.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Task "Permalink")type
```


Task.{u} (α : Type u) : Type u


Task.{u} (α : Type u) : Type u


```

`[Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α` is a primitive for asynchronous computation. It represents a computation that will resolve to a value of type `α`, possibly being computed on another thread. This is similar to `Future` in Scala, `Promise` in Javascript, and `JoinHandle` in Rust.
The tasks have an overridden representation in the runtime.
##  21.11.1. Creating Tasks[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Creating-Tasks "Permalink")
Pure tasks should typically be created with `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, as `[Task.pure](IO/Tasks-and-Threads/#Task___pure "Documentation for Task.pure")` is a task that's already been resolved with the provided value. Impure tasks are created by one of the `[asTask](IO/Tasks-and-Threads/#BaseIO___asTask "Documentation for BaseIO.asTask")` actions.
###  21.11.1.1. Pure Tasks[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Creating-Tasks--Pure-Tasks "Permalink")
Pure tasks may be created outside the `[IO](IO/Logical-Model/#IO "Documentation for IO")` family of monads. They are terminated when the last reference to them is dropped.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Task.spawn "Permalink")def
```


Task.spawn.{u} {α : Type u} (fn : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default")) : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α


Task.spawn.{u} {α : Type u}
  (fn : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default")) :
  [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α


```

`spawn fn : Task α` constructs and immediately launches a new task for evaluating the function `fn () : α` asynchronously.
`prio`, if provided, is the priority of the task.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Task.pure "Permalink")constructor of Task
```


Task.pure.{u} {α : Type u} (get : α) : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α


Task.pure.{u} {α : Type u} (get : α) :
  [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α


```

`[Task.pure](IO/Tasks-and-Threads/#Task___pure "Documentation for Task.pure") (a : α)` constructs a task that is already resolved with value `a`.
###  21.11.1.2. Impure Tasks[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Creating-Tasks--Impure-Tasks "Permalink")
When spawning a task with side effects using one of the `[asTask](IO/Tasks-and-Threads/#IO___asTask "Documentation for IO.asTask")` functions, it's important to actually execute the resulting `[IO](IO/Logical-Model/#IO "Documentation for IO")` action. A task is spawned each time the resulting action is executed, not when `[asTask](IO/Tasks-and-Threads/#IO___asTask "Documentation for IO.asTask")` is called. Impure tasks continue running even when there are no references to them, though this does result in cancellation being requested. Cancellation may also be explicitly requested using `[IO.cancel](IO/Tasks-and-Threads/#IO___cancel "Documentation for IO.cancel")`. The impure task must check for cancellation using `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BaseIO.asTask "Permalink")opaque
```


BaseIO.asTask {α : Type} (act : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)


BaseIO.asTask {α : Type} (act : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)


```

Runs `act` in a separate `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task")`, with priority `prio`.
Running the resulting `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action causes the task to be started eagerly. Pure accesses to the `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task")` do not influence the impure `act`.
Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EIO.asTask "Permalink")def
```


EIO.asTask {ε α : Type} (act : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α))


EIO.asTask {ε α : Type} (act : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α))


```

Runs `act` in a separate `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task")`, with priority `prio`. Because `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε` actions may throw an exception of type `ε`, the result of the task is an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α`.
Running the resulting `[IO](IO/Logical-Model/#IO "Documentation for IO")` action causes the task to be started eagerly. Pure accesses to the `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task")` do not influence the impure `act`.
Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.asTask "Permalink")def
```


IO.asTask {α : Type} (act : [IO](IO/Logical-Model/#IO "Documentation for IO") α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") α))


IO.asTask {α : Type} (act : [IO](IO/Logical-Model/#IO "Documentation for IO") α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") α))


```

Runs `act` in a separate `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task")`, with priority `prio`. Because `[IO](IO/Logical-Model/#IO "Documentation for IO")` actions may throw an exception of type `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")`, the result of the task is an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") α`.
Running the resulting `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action causes the task to be started eagerly. Pure accesses to the `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task")` do not influence the impure `act`. Because `[IO](IO/Logical-Model/#IO "Documentation for IO")` actions may throw an exception of type `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")`, the result of the task is an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") α`.
Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped.
###  21.11.1.3. Priorities[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Creating-Tasks--Priorities "Permalink")
Task priorities are used by the thread scheduler to assign tasks to threads. Within the priority range `[default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default")`–`[max](IO/Tasks-and-Threads/#Task___Priority___max "Documentation for Task.Priority.max")`, higher-priority tasks always take precedence over lower-priority tasks. Tasks spawned with priority `[dedicated](IO/Tasks-and-Threads/#Task___Priority___dedicated "Documentation for Task.Priority.dedicated")` are assigned their own dedicated threads and do not contend with other tasks for the threads in the thread pool.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Task.Priority "Permalink")def
```


Task.Priority : Type


Task.Priority : Type


```

Task priority.
Tasks with higher priority will always be scheduled before tasks with lower priority. Tasks with a priority greater than `[Task.Priority.max](IO/Tasks-and-Threads/#Task___Priority___max "Documentation for Task.Priority.max")` are scheduled on dedicated threads.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Task.Priority.default "Permalink")def
```


Task.Priority.default : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority")


Task.Priority.default : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority")


```

The default priority for spawned tasks, also the lowest priority: `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Task.Priority.max "Permalink")def
```


Task.Priority.max : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority")


Task.Priority.max : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority")


```

The highest regular priority for spawned tasks: `8`.
Spawning a task with a priority higher than `[Task.Priority.max](IO/Tasks-and-Threads/#Task___Priority___max "Documentation for Task.Priority.max")` is not an error but will spawn a dedicated worker for the task. This is indicated using `[Task.Priority.dedicated](IO/Tasks-and-Threads/#Task___Priority___dedicated "Documentation for Task.Priority.dedicated")`. Regular priority tasks are placed in a thread pool and worked on according to their priority order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Task.Priority.dedicated "Permalink")def
```


Task.Priority.dedicated : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority")


Task.Priority.dedicated : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority")


```

Indicates that a task should be scheduled on a dedicated thread.
Any priority higher than `[Task.Priority.max](IO/Tasks-and-Threads/#Task___Priority___max "Documentation for Task.Priority.max")` will result in the task being scheduled immediately on a dedicated thread. This is particularly useful for long-running and/or I/O-bound tasks since Lean will, by default, allocate no more non-dedicated workers than the number of cores to reduce context switches.
##  21.11.2. Task Results[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Task-Results "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Task.get "Permalink")def
```


Task.get.{u} {α : Type u} (self : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) : α


Task.get.{u} {α : Type u}
  (self : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) : α


```

Blocks the current thread until the given task has finished execution, and then returns the result of the task. If the current thread is itself executing a (non-dedicated) task, the maximum threadpool size is temporarily increased by one while waiting so as to ensure the process cannot be deadlocked by threadpool starvation. Note that when the current thread is unblocked, more tasks than the configured threadpool size may temporarily be running at the same time until sufficiently many tasks have finished.
`[Task.map](IO/Tasks-and-Threads/#Task___map "Documentation for Task.map")` and `[Task.bind](IO/Tasks-and-Threads/#Task___bind "Documentation for Task.bind")` should be preferred over `[Task.get](IO/Tasks-and-Threads/#Task___get "Documentation for Task.get")` for setting up task dependencies where possible as they do not require temporarily growing the threadpool in this way. In particular, calling `[Task.get](IO/Tasks-and-Threads/#Task___get "Documentation for Task.get")` in a task continuation with `(sync := true)` will panic as the continuation is decidedly not "cheap" in this case and deadlocks may otherwise occur. The waited-upon task should instead be returned and unwrapped using `Task.bind/IO.bindTask`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.wait "Permalink")opaque
```


IO.wait {α : Type} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α


IO.wait {α : Type} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α


```

Waits for the task to finish, then returns its result.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.waitAny "Permalink")opaque
```


IO.waitAny {α : Type} (tasks : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α))
  (h : tasks.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") > 0 := by exact Nat.zero_lt_succ _) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α


IO.waitAny {α : Type}
  (tasks : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α))
  (h : tasks.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") > 0 := by
    exact Nat.zero_lt_succ _) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α


```

Waits until any of the tasks in the list has finished, then returns its result.
##  21.11.3. Sequencing Tasks[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Sequencing-Tasks "Permalink")
These operators create new tasks from old ones. When possible, it's good to use `[Task.map](IO/Tasks-and-Threads/#Task___map "Documentation for Task.map")` or `[Task.bind](IO/Tasks-and-Threads/#Task___bind "Documentation for Task.bind")` instead of manually calling `[Task.get](IO/Tasks-and-Threads/#Task___get "Documentation for Task.get")` in a new task because they don't temporarily increase the size of the thread pool.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Task.map "Permalink")def
```


Task.map.{u_1, u_2} {α : Type u_1} {β : Type u_2} (f : α → β)
  (x : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β


Task.map.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (f : α → β) (x : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β


```

`map f x` maps function `f` over the task `x`: that is, it constructs (and immediately launches) a new task which will wait for the value of `x` to be available and then calls `f` on the result.
`prio`, if provided, is the priority of the task. If `sync` is set to true, `f` is executed on the current thread if `x` has already finished and otherwise on the thread that `x` finished on. `prio` is ignored in this case. This should only be done when executing `f` is cheap and non-blocking.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Task.bind "Permalink")def
```


Task.bind.{u_1, u_2} {α : Type u_1} {β : Type u_2} (x : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (f : α → [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β) (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β


Task.bind.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (x : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (f : α → [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β


```

`bind x f` does a monad "bind" operation on the task `x` with function `f`: that is, it constructs (and immediately launches) a new task which will wait for the value of `x` to be available and then calls `f` on the result, resulting in a new task which is then run for a result.
`prio`, if provided, is the priority of the task. If `sync` is set to true, `f` is executed on the current thread if `x` has already finished and otherwise on the thread that `x` finished on. `prio` is ignored in this case. This should only be done when executing `f` is cheap and non-blocking.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Task.mapList "Permalink")def
```


Task.mapList.{u_1, u_2} {α : Type u_1} {β : Type u_2} (f : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → β)
  (tasks : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β


Task.mapList.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (f : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → β)
  (tasks : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β


```

Creates a task that, when all `tasks` have finished, computes the result of `f` applied to their results.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BaseIO.mapTask "Permalink")opaque
```


BaseIO.mapTask.{u_1} {α : Type u_1} {β : Type} (f : α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") β)
  (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β)


BaseIO.mapTask.{u_1} {α : Type u_1}
  {β : Type} (f : α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") β)
  (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β)


```

Creates a new task that waits for `t` to complete and then runs the `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action `f` on its result. This new task has priority `prio`.
Running the resulting `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action causes the task to be started eagerly. Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EIO.mapTask "Permalink")def
```


EIO.mapTask.{u_1} {α : Type u_1} {ε β : Type} (f : α → [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε β)
  (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β))


EIO.mapTask.{u_1} {α : Type u_1}
  {ε β : Type} (f : α → [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε β)
  (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β))


```

Creates a new task that waits for `t` to complete and then runs the `[IO](IO/Logical-Model/#IO "Documentation for IO")` action `f` on its result. This new task has priority `prio`.
Running the resulting `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action causes the task to be started eagerly. Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped. Because `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε` actions may throw an exception of type `ε`, the result of the task is an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.mapTask "Permalink")def
```


IO.mapTask.{u_1} {α : Type u_1} {β : Type} (f : α → [IO](IO/Logical-Model/#IO "Documentation for IO") β) (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") β))


IO.mapTask.{u_1} {α : Type u_1} {β : Type}
  (f : α → [IO](IO/Logical-Model/#IO "Documentation for IO") β) (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") β))


```

Creates a new task that waits for `t` to complete and then runs the `[IO](IO/Logical-Model/#IO "Documentation for IO")` action `f` on its result. This new task has priority `prio`.
Running the resulting `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action causes the task to be started eagerly. Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped. Because `[IO](IO/Logical-Model/#IO "Documentation for IO")` actions may throw an exception of type `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")`, the result of the task is an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") α`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BaseIO.mapTasks "Permalink")def
```


BaseIO.mapTasks.{u_1} {α : Type u_1} {β : Type} (f : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") β)
  (tasks : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β)


BaseIO.mapTasks.{u_1} {α : Type u_1}
  {β : Type} (f : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") β)
  (tasks : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β)


```

Creates a new task that waits for all the tasks in the list `tasks` to complete, and then runs the `[IO](IO/Logical-Model/#IO "Documentation for IO")` action `f` on their results. This new task has priority `prio`.
Running the resulting `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action causes the task to be started eagerly. Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EIO.mapTasks "Permalink")def
```


EIO.mapTasks.{u_1} {α : Type u_1} {ε β : Type} (f : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε β)
  (tasks : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β))


EIO.mapTasks.{u_1} {α : Type u_1}
  {ε β : Type} (f : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε β)
  (tasks : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β))


```

Creates a new task that waits for all the tasks in the list `tasks` to complete, and then runs the `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε` action `f` on their results. This new task has priority `prio`.
Running the resulting `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action causes the task to be started eagerly. Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.mapTasks "Permalink")def
```


IO.mapTasks.{u_1} {α : Type u_1} {β : Type} (f : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [IO](IO/Logical-Model/#IO "Documentation for IO") β)
  (tasks : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") β))


IO.mapTasks.{u_1} {α : Type u_1}
  {β : Type} (f : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [IO](IO/Logical-Model/#IO "Documentation for IO") β)
  (tasks : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") β))


```

`[IO](IO/Logical-Model/#IO "Documentation for IO")` specialization of `[EIO.mapTasks](IO/Tasks-and-Threads/#EIO___mapTasks "Documentation for EIO.mapTasks")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BaseIO.bindTask "Permalink")opaque
```


BaseIO.bindTask.{u_1} {α : Type u_1} {β : Type} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (f : α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β)


BaseIO.bindTask.{u_1} {α : Type u_1}
  {β : Type} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (f : α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") β)


```

Creates a new task that waits for `t` to complete, runs the `[IO](IO/Logical-Model/#IO "Documentation for IO")` action `f` on its result, and then continues as the resulting task. This new task has priority `prio`.
Running the resulting `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action causes this new task to be started eagerly. Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EIO.bindTask "Permalink")def
```


EIO.bindTask.{u_1} {α : Type u_1} {ε β : Type} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (f : α → [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β)))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β))


EIO.bindTask.{u_1} {α : Type u_1}
  {ε β : Type} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (f : α → [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β)))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β))


```

Creates a new task that waits for `t` to complete, runs the `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε` action `f` on its result, and then continues as the resulting task. This new task has priority `prio`.
Running the resulting `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action causes this new task to be started eagerly. Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped. Because `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε` actions may throw an exception of type `ε`, the result of the task is an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.bindTask "Permalink")def
```


IO.bindTask.{u_1} {α : Type u_1} {β : Type} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (f : α → [IO](IO/Logical-Model/#IO "Documentation for IO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") β)))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") β))


IO.bindTask.{u_1} {α : Type u_1}
  {β : Type} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (f : α → [IO](IO/Logical-Model/#IO "Documentation for IO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") β)))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") β))


```

Creates a new task that waits for `t` to complete, runs the `[IO](IO/Logical-Model/#IO "Documentation for IO")` action `f` on its result, and then continues as the resulting task. This new task has priority `prio`.
Running the resulting `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action causes this new task to be started eagerly. Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped. Because `[IO](IO/Logical-Model/#IO "Documentation for IO")` actions may throw an exception of type `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")`, the result of the task is an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") α`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BaseIO.chainTask "Permalink")def
```


BaseIO.chainTask.{u_1} {α : Type u_1} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) (f : α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


BaseIO.chainTask.{u_1} {α : Type u_1}
  (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) (f : α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Creates a new task that waits for `t` to complete and then runs the `[IO](IO/Logical-Model/#IO "Documentation for IO")` action `f` on its result. This new task has priority `prio`.
This is a version of `[BaseIO.mapTask](IO/Tasks-and-Threads/#BaseIO___mapTask "Documentation for BaseIO.mapTask")` that ignores the result value.
Running the resulting `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action causes the task to be started eagerly. Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EIO.chainTask "Permalink")def
```


EIO.chainTask.{u_1} {α : Type u_1} {ε : Type} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (f : α → [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


EIO.chainTask.{u_1} {α : Type u_1}
  {ε : Type} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)
  (f : α → [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Creates a new task that waits for `t` to complete and then runs the `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε` action `f` on its result. This new task has priority `prio`.
This is a version of `[EIO.mapTask](IO/Tasks-and-Threads/#EIO___mapTask "Documentation for EIO.mapTask")` that ignores the result value.
Running the resulting `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε` action causes the task to be started eagerly. Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The `act` should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.chainTask "Permalink")def
```


IO.chainTask.{u_1} {α : Type u_1} (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) (f : α → [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.chainTask.{u_1} {α : Type u_1}
  (t : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) (f : α → [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default"))
  (sync : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Creates a new task that waits for `t` to complete and then runs the `[IO](IO/Logical-Model/#IO "Documentation for IO")` action `f` on its result. This new task has priority `prio`.
This is a version of `[IO.mapTask](IO/Tasks-and-Threads/#IO___mapTask "Documentation for IO.mapTask")` that ignores the result value.
Running the resulting `[IO](IO/Logical-Model/#IO "Documentation for IO")` action causes the task to be started eagerly. Unlike pure tasks created by `[Task.spawn](IO/Tasks-and-Threads/#Task___spawn "Documentation for Task.spawn")`, tasks created by this function will run even if the last reference to the task is dropped. The act should explicitly check for cancellation via `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` if it should be terminated or otherwise react to the last reference being dropped.
##  21.11.4. Cancellation and Status[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Cancellation-and-Status "Permalink")
Impure tasks should use `IO.checkCanceled` to react to cancellation, which occurs either as a result of `IO.cancel` or when the last reference to the task is dropped. Pure tasks are terminated automatically upon cancellation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.cancel "Permalink")opaque
```


IO.cancel.{u_1} {α : Type u_1} : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.cancel.{u_1} {α : Type u_1} :
  [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Requests cooperative cancellation of the task. The task must explicitly call `[IO.checkCanceled](IO/Tasks-and-Threads/#IO___checkCanceled "Documentation for IO.checkCanceled")` to react to the cancellation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.checkCanceled "Permalink")opaque
```


IO.checkCanceled : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


IO.checkCanceled : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the current task's cancellation flag has been set by calling `[IO.cancel](IO/Tasks-and-Threads/#IO___cancel "Documentation for IO.cancel")` or by dropping the last reference to the task.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.hasFinished "Permalink")def
```


IO.hasFinished.{u_1} {α : Type u_1} (task : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


IO.hasFinished.{u_1} {α : Type u_1}
  (task : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the task has finished execution, at which point calling `[Task.get](IO/Tasks-and-Threads/#Task___get "Documentation for Task.get")` will return immediately.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.getTaskState "Permalink")opaque
```


IO.getTaskState.{u_1} {α : Type u_1} : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.TaskState](IO/Tasks-and-Threads/#IO___TaskState___waiting "Documentation for IO.TaskState")


IO.getTaskState.{u_1} {α : Type u_1} :
  [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.TaskState](IO/Tasks-and-Threads/#IO___TaskState___waiting "Documentation for IO.TaskState")


```

Returns the current state of a task in the Lean runtime's task manager.
For tasks derived from `Promise`s, the states `waiting` and `running` should be considered equivalent.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.TaskState.finished "Permalink")inductive type
```


IO.TaskState : Type


IO.TaskState : Type


```

The current state of a `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task")` in the Lean runtime's task manager.
#  Constructors

```
waiting : [IO.TaskState](IO/Tasks-and-Threads/#IO___TaskState___waiting "Documentation for IO.TaskState")
```

The `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task")` is waiting to be run.
It can be waiting for dependencies to complete or sitting in the task manager queue waiting for a thread to run on.

```
running : [IO.TaskState](IO/Tasks-and-Threads/#IO___TaskState___waiting "Documentation for IO.TaskState")
```

The `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task")` is actively running on a thread or, in the case of a `[Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise")`, waiting for a call to `[IO.Promise.resolve](IO/Tasks-and-Threads/#IO___Promise___resolve "Documentation for IO.Promise.resolve")`.

```
finished : [IO.TaskState](IO/Tasks-and-Threads/#IO___TaskState___waiting "Documentation for IO.TaskState")
```

The `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task")` has finished running and its result is available. Calling `[Task.get](IO/Tasks-and-Threads/#Task___get "Documentation for Task.get")` or `[IO.wait](IO/Tasks-and-Threads/#IO___wait "Documentation for IO.wait")` on the task will not block.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.getTID "Permalink")opaque
```


IO.getTID : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


IO.getTID : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Returns the thread ID of the calling thread.
##  21.11.5. Promises[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Promises "Permalink")
Promises represent a value that will be supplied in the future. Supplying the value is called _resolving_ the promise. Once created, a promise can be stored in a data structure or passed around like any other value, and attempts to read from it will block until it is resolved.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Promise "Permalink")structure
```


IO.Promise (α : Type) : Type


IO.Promise (α : Type) : Type


```

`Promise α` allows you to create a `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α` whose value is provided later by calling `resolve`.
Typical usage is as follows:
  1. `let promise ← Promise.new` creates a promise
  2. `promise.result? : Task (Option α)` can now be passed around
  3. `promise.result?.get` blocks until the promise is resolved
  4. `promise.resolve a` resolves the promise
  5. `promise.result?.get` now returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a`


If the promise is dropped without ever being resolved, `promise.result?.get` will return `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. See `Promise.result!/resultD` for other ways to handle this case.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Promise.new "Permalink")opaque
```


IO.Promise.new {α : Type} [[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α] : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α)


IO.Promise.new {α : Type} [[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α] :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α)


```

Creates a new `Promise`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Promise.isResolved "Permalink")def
```


IO.Promise.isResolved {α : Type} (promise : [IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


IO.Promise.isResolved {α : Type}
  (promise : [IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the promise has already been resolved, i.e. whether access to `result*` will return immediately.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Promise.result? "Permalink")opaque
```


IO.Promise.result? {α : Type} (promise : [IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α) : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


IO.Promise.result? {α : Type}
  (promise : [IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α) :
  [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


```

Like `Promise.result`, but resolves to `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the promise is dropped without ever being resolved.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Promise.result! "Permalink")def
```


IO.Promise.result! {α : Type} (promise : [IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α) : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α


IO.Promise.result! {α : Type}
  (promise : [IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α) : [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α


```

The result task of a `Promise`.
The task blocks until `Promise.resolve` is called. If the promise is dropped without ever being resolved, evaluating the task will panic and, when not using fatal panics, block forever. As `Promise.result!` is a pure value and thus the point of evaluation may not be known precisely, this means that any promise on which `Promise.result!` _may_ be evaluated _must_ be resolved eventually. When in doubt, always prefer `Promise.result?` to handle dropped promises explicitly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Promise.resultD "Permalink")def
```


IO.Promise.resultD {α : Type} (promise : [IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α) (dflt : α) :
  [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α


IO.Promise.resultD {α : Type}
  (promise : [IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α) (dflt : α) :
  [Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α


```

Like `Promise.result`, but resolves to `dflt` if the promise is dropped without ever being resolved.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Promise.resolve "Permalink")opaque
```


IO.Promise.resolve {α : Type} (value : α) (promise : [IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.Promise.resolve {α : Type} (value : α)
  (promise : [IO.Promise](IO/Tasks-and-Threads/#IO___Promise "Documentation for IO.Promise") α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Resolves a `Promise`.
Only the first call to this function has an effect.
##  21.11.6. Communication Between Tasks[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Communication-Between-Tasks "Permalink")
In addition to the types and operations described in this section, `[IO.Ref](IO/Mutable-References/#IO___Ref "Documentation for IO.Ref")` can be used as a lock. Taking the reference (using `[take](IO/Mutable-References/#ST___Ref___take "Documentation for ST.Ref.take")`) causes other threads to block when reading until the reference is `[set](IO/Mutable-References/#ST___Ref___set "Documentation for ST.Ref.set")` again. This pattern is described in [the section on reference cells](IO/Mutable-References/#ref-locks).
###  21.11.6.1. Channels[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Communication-Between-Tasks--Channels "Permalink")
The types and functions in this section are available after importing `Std.Sync.Channel`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Channel "Permalink")structure
```


Std.Channel (α : Type) : Type


Std.Channel (α : Type) : Type


```

A multi-producer multi-consumer FIFO channel that offers both bounded and unbounded buffering and an asynchronous API. To switch into synchronous mode use `Channel.sync`.
If a channel needs to be closed to indicate some sort of completion event use `[Std.CloseableChannel](IO/Tasks-and-Threads/#Std___CloseableChannel "Documentation for Std.CloseableChannel")` instead. Note that `[Std.CloseableChannel](IO/Tasks-and-Threads/#Std___CloseableChannel "Documentation for Std.CloseableChannel")` introduces a need for error handling in some cases, thus `[Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel")` is usually easier to use if applicable.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Channel.new "Permalink")def
```


Std.Channel.new {α : Type} (capacity : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel") α)


Std.Channel.new {α : Type}
  (capacity : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel") α)


```

Create a new channel. If:
  * `capacity` is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` it will be unbounded (the default)
  * `capacity` is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 0` it will always force a rendezvous between sender and receiver
  * `capacity` is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") n` with `n > 0` it will use a buffer of size `n` and begin blocking once it is filled


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Channel.send "Permalink")def
```


Std.Channel.send {α : Type} (ch : [Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel") α) (v : α) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))


Std.Channel.send {α : Type}
  (ch : [Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel") α) (v : α) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))


```

Send a value through the channel, returning a task that will resolve once the transmission could be completed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Channel.recv "Permalink")def
```


Std.Channel.recv {α : Type} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (ch : [Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel") α) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)


Std.Channel.recv {α : Type} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (ch : [Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel") α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") α)


```

Receive a value from the channel, returning a task that will resolve once the transmission could be completed. Note that the task may resolve to `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the channel was closed before it could be completed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Channel.forAsync "Permalink")opaque
```


Std.Channel.forAsync {α : Type} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (f : α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))
  (ch : [Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel") α) (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") := [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))


Std.Channel.forAsync {α : Type}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (f : α → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))
  (ch : [Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel") α)
  (prio : [Task.Priority](IO/Tasks-and-Threads/#Task___Priority "Documentation for Task.Priority") :=
    [Task.Priority.default](IO/Tasks-and-Threads/#Task___Priority___default "Documentation for Task.Priority.default")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Task](IO/Tasks-and-Threads/#Task "Documentation for Task") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))


```

`ch.[forAsync](IO/Tasks-and-Threads/#Std___Channel___forAsync "Documentation for Std.Channel.forAsync") f` calls `f` for every message received on `ch`.
Note that if this function is called twice, each message will only arrive at exactly one invocation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Channel.sync "Permalink")def
```


Std.Channel.sync {α : Type} (ch : [Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel") α) : [Std.Channel.Sync](IO/Tasks-and-Threads/#Std___Channel___Sync "Documentation for Std.Channel.Sync") α


Std.Channel.sync {α : Type}
  (ch : [Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel") α) :
  [Std.Channel.Sync](IO/Tasks-and-Threads/#Std___Channel___Sync "Documentation for Std.Channel.Sync") α


```

This function is a no-op and just a convenient way to expose the synchronous API of the channel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Channel.Sync "Permalink")def
```


Std.Channel.Sync (α : Type) : Type


Std.Channel.Sync (α : Type) : Type


```

A multi-producer multi-consumer FIFO channel that offers both bounded and unbounded buffering and a synchronous API. This type acts as a convenient layer to use a channel in a blocking fashion and is not actually different from the original channel.
If a channel needs to be closed to indicate some sort of completion event use `Std.CloseableChannel.Sync` instead. Note that `Std.CloseableChannel.Sync` introduces a need for error handling in some cases, thus `[Std.Channel.Sync](IO/Tasks-and-Threads/#Std___Channel___Sync "Documentation for Std.Channel.Sync")` is usually easier to use if applicable.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.CloseableChannel "Permalink")def
```


Std.CloseableChannel (α : Type) : Type


Std.CloseableChannel (α : Type) : Type


```

A multi-producer multi-consumer FIFO channel that offers both bounded and unbounded buffering and an asynchronous API, to switch into synchronous mode use `CloseableChannel.sync`.
Additionally `[Std.CloseableChannel](IO/Tasks-and-Threads/#Std___CloseableChannel "Documentation for Std.CloseableChannel")` can be closed if necessary, unlike `[Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel")`. This introduces a need for error handling in some cases, thus it is usually easier to use `[Std.Channel](IO/Tasks-and-Threads/#Std___Channel "Documentation for Std.Channel")` if applicable.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.CloseableChannel.new "Permalink")def
```


Std.CloseableChannel.new {α : Type} (capacity : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Std.CloseableChannel](IO/Tasks-and-Threads/#Std___CloseableChannel "Documentation for Std.CloseableChannel") α)


Std.CloseableChannel.new {α : Type}
  (capacity : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Std.CloseableChannel](IO/Tasks-and-Threads/#Std___CloseableChannel "Documentation for Std.CloseableChannel") α)


```

Create a new channel. If:
  * `capacity` is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` it will be unbounded (the default)
  * `capacity` is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 0` it will always force a rendezvous between sender and receiver
  * `capacity` is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") n` with `n > 0` it will use a buffer of size `n` and begin blocking once it is filled


Synchronous channels can also be read using ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for` loops. In particular, there is an instance of type `[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") m ([Std.Channel.Sync](IO/Tasks-and-Threads/#Std___Channel___Sync "Documentation for Std.Channel.Sync") α) α` for every monad `m` with a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m` instance and `α` with an `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α` instance.
###  21.11.6.2. Mutexes[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Communication-Between-Tasks--Mutexes "Permalink")
The types and functions in this section are available after importing `Std.Sync.Mutex`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Mutex "Permalink")type
```


Std.Mutex (α : Type) : Type


Std.Mutex (α : Type) : Type


```

Mutual exclusion primitive (lock) guarding shared state of type `α`.
The type `Mutex α` is similar to `[IO.Ref](IO/Mutable-References/#IO___Ref "Documentation for IO.Ref") α`, except that concurrent accesses are guarded by a mutex instead of atomic pointer operations and busy-waiting.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Mutex.new "Permalink")def
```


Std.Mutex.new {α : Type} (a : α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Std.Mutex](IO/Tasks-and-Threads/#Std___Mutex "Documentation for Std.Mutex") α)


Std.Mutex.new {α : Type} (a : α) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Std.Mutex](IO/Tasks-and-Threads/#Std___Mutex "Documentation for Std.Mutex") α)


```

Creates a new mutex.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Mutex.atomically "Permalink")def
```


Std.Mutex.atomically {m : Type → Type} {α β : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m] (mutex : [Std.Mutex](IO/Tasks-and-Threads/#Std___Mutex "Documentation for Std.Mutex") α)
  (k : [Std.AtomicT](IO/Tasks-and-Threads/#Std___AtomicT "Documentation for Std.AtomicT") α m β) : m β


Std.Mutex.atomically {m : Type → Type}
  {α β : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m]
  (mutex : [Std.Mutex](IO/Tasks-and-Threads/#Std___Mutex "Documentation for Std.Mutex") α)
  (k : [Std.AtomicT](IO/Tasks-and-Threads/#Std___AtomicT "Documentation for Std.AtomicT") α m β) : m β


```

`mutex.[atomically](IO/Tasks-and-Threads/#Std___Mutex___atomically "Documentation for Std.Mutex.atomically") k` runs `k` with access to the mutex's state while locking the mutex.
Calling `mutex.atomically` while already holding the underlying `BaseMutex` in the same thread is undefined behavior. If this is unavoidable in your code, consider using `RecursiveMutex`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Mutex.atomicallyOnce "Permalink")def
```


Std.Mutex.atomicallyOnce {m : Type → Type} {α β : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m] (mutex : [Std.Mutex](IO/Tasks-and-Threads/#Std___Mutex "Documentation for Std.Mutex") α)
  (condvar : [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar")) (pred : [Std.AtomicT](IO/Tasks-and-Threads/#Std___AtomicT "Documentation for Std.AtomicT") α m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (k : [Std.AtomicT](IO/Tasks-and-Threads/#Std___AtomicT "Documentation for Std.AtomicT") α m β) : m β


Std.Mutex.atomicallyOnce {m : Type → Type}
  {α β : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m]
  (mutex : [Std.Mutex](IO/Tasks-and-Threads/#Std___Mutex "Documentation for Std.Mutex") α)
  (condvar : [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar"))
  (pred : [Std.AtomicT](IO/Tasks-and-Threads/#Std___AtomicT "Documentation for Std.AtomicT") α m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (k : [Std.AtomicT](IO/Tasks-and-Threads/#Std___AtomicT "Documentation for Std.AtomicT") α m β) : m β


```

`mutex.[atomicallyOnce](IO/Tasks-and-Threads/#Std___Mutex___atomicallyOnce "Documentation for Std.Mutex.atomicallyOnce") condvar pred k` runs `k`, waiting on `condvar` until `pred` returns true. Both `k` and `pred` have access to the mutex's state.
Calling `mutex.atomicallyOnce` while already holding the underlying `BaseMutex` in the same thread is undefined behavior. If this is unavoidable in your code, consider using `RecursiveMutex`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.AtomicT "Permalink")def
```


Std.AtomicT (σ : Type) (m : Type → Type) (α : Type) : Type


Std.AtomicT (σ : Type) (m : Type → Type)
  (α : Type) : Type


```

`AtomicT α m` is the monad that can be atomically executed inside mutual exclusion primitives like `Mutex α` with outside monad `m`. The action has access to the state `α` of the mutex (via `get` and `[set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set")`).
###  21.11.6.3. Condition Variables[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Tasks-and-Threads--Communication-Between-Tasks--Condition-Variables "Permalink")
The types and functions in this section are available after importing `Std.Sync.Mutex`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Condvar "Permalink")def
```


Std.Condvar : Type


Std.Condvar : Type


```

Condition variable, a synchronization primitive to be used with a `BaseMutex` or `Mutex`.
The thread that wants to modify the shared variable must:
  1. Lock the `BaseMutex` or `Mutex`
  2. Work on the shared variable
  3. Call `Condvar.notifyOne` or `Condvar.notifyAll` after it is done. Note that this may be done before or after the mutex is unlocked.


If working with a `Mutex` the thread that waits on the `Condvar` can use `Mutex.atomicallyOnce` to wait until a condition is true. If working with a `BaseMutex` it must:
  1. Lock the `BaseMutex`.
  2. Do one of the following:


  * Use `Condvar.waitUntil` to (potentially repeatedly wait) on the condition variable until the condition is true.
  * Implement the waiting manually by:
    1. Checking the condition
    2. Calling `Condvar.wait` which releases the `BaseMutex` and suspends execution until the condition variable is notified.
    3. Check the condition and resume waiting if not satisfied.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Condvar.new "Permalink")opaque
```


Std.Condvar.new : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar")


Std.Condvar.new : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar")


```

Creates a new condition variable.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Condvar.wait "Permalink")opaque
```


Std.Condvar.wait (condvar : [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar")) (mutex : Std.BaseMutex) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Std.Condvar.wait (condvar : [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar"))
  (mutex : Std.BaseMutex) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Waits until another thread calls `notifyOne` or `notifyAll`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Condvar.notifyOne "Permalink")opaque
```


Std.Condvar.notifyOne (condvar : [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Std.Condvar.notifyOne
  (condvar : [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Wakes up a single other thread executing `wait`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Condvar.notifyAll "Permalink")opaque
```


Std.Condvar.notifyAll (condvar : [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Std.Condvar.notifyAll
  (condvar : [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Wakes up all other threads executing `wait`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Condvar.waitUntil "Permalink")def
```


Std.Condvar.waitUntil.{u_1} {m : Type → Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] (condvar : [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar")) (mutex : Std.BaseMutex)
  (pred : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Std.Condvar.waitUntil.{u_1}
  {m : Type → Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m]
  (condvar : [Std.Condvar](IO/Tasks-and-Threads/#Std___Condvar "Documentation for Std.Condvar"))
  (mutex : Std.BaseMutex)
  (pred : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Waits on the condition variable until the predicate is true.
[←21.10. Random Numbers](IO/Random-Numbers/#The-Lean-Language-Reference--IO--Random-Numbers "21.10. Random Numbers")[22. Iterators→](Iterators/#iterators "22. Iterators")

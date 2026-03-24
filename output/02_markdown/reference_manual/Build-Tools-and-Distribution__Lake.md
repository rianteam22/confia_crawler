[←24. Build Tools and Distribution](Build-Tools-and-Distribution/#build-tools-and-distribution "24. Build Tools and Distribution")[24.2. Managing Toolchains with Elan→](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan "24.2. Managing Toolchains with Elan")
#  24.1. Lake[🔗](find/?domain=Verso.Genre.Manual.section&name=lake "Permalink")
Lake is the standard Lean build tool. It is responsible for:
  * Configuring builds and building Lean code
  * Fetching and building external dependencies
  * Integrating with Reservoir, the Lean package server
  * Running tests, linters, and other development workflows


Lake is extensible. It provides a rich API that can be used to define incremental build tasks for software artifacts that are not written in Lean, to automate administrative tasks, and to integrate with external workflows. For build configurations that do not need these features, Lake provides a declarative configuration language that can be written either in TOML or as a Lean file.
This section describes Lake's [command-line interface](Build-Tools-and-Distribution/Lake/#lake-cli), [configuration files](Build-Tools-and-Distribution/Lake/#lake-config), and [internal API](Build-Tools-and-Distribution/Lake/#lake-api). All three share a set of concepts and terminology.
##  24.1.1. Concepts and Terminology[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-vocab "Permalink")
A _package_ is the basic unit of Lean code distribution. A single package may contain multiple libraries or executable programs. A package consist of a directory that contains a [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) file together with source code. Packages may _require_ other packages, in which case those packages' code (more specifically, their [targets](Build-Tools-and-Distribution/Lake/#--tech-term-target)) are made available. The _direct dependencies_ of a package are those that it requires, and the _transitive dependencies_ are the direct dependencies of a package together with their transitive dependencies. Packages may either be obtained from [Reservoir](https://reservoir.lean-lang.org/), the Lean package repository, or from a manually-specified location. _Git dependencies_ are specified by a Git repository URL along with a revision (branch, tag, or hash) and must be cloned locally prior to build, while local _path dependencies_ are specified by a path relative to the package's directory.
A _workspace_ is a directory on disk that contains a working copy of a [package](Build-Tools-and-Distribution/Lake/#--tech-term-package)'s source code and the source code of all [transitive dependencies](Build-Tools-and-Distribution/Lake/#--tech-term-transitive-dependencies) that are not specified as local paths. The package for which the workspace was created is the _root package_. The workspace also contains any built [artifacts](Build-Tools-and-Distribution/Lake/#--tech-term-artifact) for the package, enabling [incremental builds](Build-Tools-and-Distribution/Lake/#--tech-term-incremental-build). Dependencies and artifacts do not need to be present for a directory to be considered a workspace; commands such as [`lake update`](Build-Tools-and-Distribution/Lake/#update) and [`lake build`](Build-Tools-and-Distribution/Lake/#build) produce them if they are missing. Lake is typically used in a workspace.[`lake init`](Build-Tools-and-Distribution/Lake/#init) and [`lake new`](Build-Tools-and-Distribution/Lake/#new), which create workspaces, are exceptions. Workspaces typically have the following layout:
  * `lean-toolchain`: The [toolchain file](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#--tech-term-toolchain-file).
  * `lakefile.toml` or `lakefile.lean`: The [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) file for the root package.
  * `lake-manifest.json`: The root package's [manifest](Build-Tools-and-Distribution/Lake/#--tech-term-manifest).
  * `.lake/`: Intermediate state managed by Lake, such as built [artifacts](Build-Tools-and-Distribution/Lake/#--tech-term-artifact) and dependency source code.
    * `.lake/lakefile.olean`: The root package's configuration, cached.
    * `.lake/packages/`: The workspace's _package directory_ , which contains copies of all non-local transitive dependencies of the root package, with their built artifacts in their own `.lake` directories.
    * `.lake/build/`: The _build directory_ , which contains built artifacts for the root package:
      * `.lake/build/bin`: The package's _binary directory_ , which contains built executables.
      * `.lake/build/lib`: The package's _library directory_ , which contains built libraries and [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file).
      * `.lake/build/ir`: The package's intermediate result directory, which contains generated intermediate artifacts, primarily C code.


Workspace Layout
A _package configuration_ file specifies the dependencies, settings, and targets of a package. Packages can specify configuration options that apply to all their contained targets. They can be written in two formats:
  * The [TOML format](Build-Tools-and-Distribution/Lake/#lake-config-toml) (`lakefile.toml`) is used for fully declarative package configurations.
  * The [Lean format](Build-Tools-and-Distribution/Lake/#lake-config-lean) (`lakefile.lean`) additionally supports the use of Lean code to configure the package in ways not supported by the declarative options.


A _manifest_ tracks the specific versions of other packages that are used in a package. Together, a manifest and a [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) file specify a unique set of transitive dependencies for the package. Before building, Lake synchronizes the local copy of each dependency with the version specified in the manifest. If no manifest is available, Lake fetches the latest matching versions of each dependency and creates a manifest. It is an error if the package names listed in the manifest do not match those used by the package; the manifest must be updated using [`lake update`](Build-Tools-and-Distribution/Lake/#update) prior to building. Manifests should be considered part of the package's code and should normally be checked into source control.
A _target_ represents an output that can be requested by a user. A persistent build output, such as object code, an executable binary, or an [`.olean` file](Elaboration-and-Compilation/#--tech-term-___olean-file), is called an _artifact_. In the process of producing an artifact, Lake may need to produce further artifacts; for example, compiling a Lean program into an executable requires that it and its dependencies be compiled to object files, which are themselves produced from C source files, which result from elaborating Lean sourcefiles and producing [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file). Each link in this chain is a target, and Lake arranges for each to be built in turn. At the start of the chain are the _initial targets_ :
  * [_Packages_](Build-Tools-and-Distribution/Lake/#--tech-term-package) are units of Lean code that are distributed as a unit.
  * _Libraries_ are collections of Lean [module](Source-Files-and-Modules/#--tech-term-module)s, organized hierarchically under one or more _module roots_.
  * _Executables_ consist of a _single_ module that defines `main`.
  * _External libraries_ are non-Lean **static** libraries that will be linked to the binaries of the package and its dependents, including both their shared libraries and executables.
  * _Custom targets_ contain arbitrary code to run a build, written using Lake's internal API.


In addition to their Lean code, packages, libraries, and executables contain configuration settings that affect subsequent build steps. Packages may specify a set of _default targets_. Default targets are the initial targets in the package that are to be built in contexts where a package is specified but specific targets are not.
The _log_ contains information produced during a build. Logs are saved so they can be replayed during [incremental builds](Build-Tools-and-Distribution/Lake/#--tech-term-incremental-build). Messages in the log have four levels, ordered by severity:
  1. _Trace messages_ contain internal build details that are often specific to the machine on which the build is running, including the specific invocations of Lean and other tools that are passed to the shell.
  2. _Informational messages_ contain general informational output that is not expected to indicate a problem with the code, such as the results of a ``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
     * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
     * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.
The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
     * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
     * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
     * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.
See also: `#reduce e` for evaluation by term reduction.
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) command.
  3. _Warnings_ indicate potential problems, such as unused variable bindings.
  4. _Errors_ explain why parsing and elaboration could not complete.


By default, trace messages are hidden and the others are shown. The threshold can be adjusted using the `--log-level[](Build-Tools-and-Distribution/Lake/#lake-option--log-level)` option, the `--verbose[](Build-Tools-and-Distribution/Lake/#lake-flag--verbose)` flag, or the `--quiet[](Build-Tools-and-Distribution/Lake/#lake-flag--quiet)` flag.
###  24.1.1.1. Builds[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Concepts-and-Terminology--Builds "Permalink")
Producing a desired [artifact](Build-Tools-and-Distribution/Lake/#--tech-term-artifact), such as a [`.olean` file](Elaboration-and-Compilation/#--tech-term-___olean-file) or an executable binary, is called a _build_. Builds are triggered by the [`lake build`](Build-Tools-and-Distribution/Lake/#build) command or by other commands that require an artifact to be present, such as [`lake exe`](Build-Tools-and-Distribution/Lake/#exe). A build consists of the following steps: 

Configuring the package
    
If [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) file is newer than the cached configuration file `lakefile.olean`, then the package configuration is re-elaborated. This also occurs when the cached file is missing or when the `--reconfigure[](Build-Tools-and-Distribution/Lake/#lake-flag--reconfigure)` or `-R[](Build-Tools-and-Distribution/Lake/#lake-flag-R)` flag is provided. Changes to options using `-K` do not trigger re-elaboration of the configuration file; `-R[](Build-Tools-and-Distribution/Lake/#lake-flag-R)` is necessary in these cases. 

Computing dependencies
    
The set of artifacts that are required to produce the desired output are determined, along with the [targets](Build-Tools-and-Distribution/Lake/#--tech-term-target) and [facets](Build-Tools-and-Distribution/Lake/#--tech-term-facet) that produce them. This process is recursive, and the result is a _graph_ of dependencies. The dependencies in this graph are distinct from those declared for a package: packages depend on other packages, while build targets depend on other build targets, which may be in the same package or in a different one. One facet of a given target may depend on other facets of the same target. Lake automatically analyzes the imports of Lean modules to discover their dependencies, and the `extraDepTargets[](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig-extraDepTargets)` field can be used to add additional dependencies to a target. 

Replaying traces
    
Rather than rebuilding everything in the dependency graph from scratch, Lake uses saved _trace files_ to determine which artifacts require building. During a build, Lake records which source files or other artifacts were used to produce each artifact, saving a hash of each input; these _traces_ are saved in the [build directory](Build-Tools-and-Distribution/Lake/#--tech-term-build-directory).More specifically, each artifact's trace file contains a Merkle tree hash mixture of its inputs' hashes. If the inputs are all unmodified, then the corresponding artifact is not rebuilt. Trace files additionally record the [log](Build-Tools-and-Distribution/Lake/#--tech-term-log) from each build task; these outputs are replayed as if the artifact had been built anew. Reusing prior build products when possible is called an _incremental build_. 

Building artifacts
    
When all unmodified dependencies in the dependency graph have been replayed from their trace files, Lake proceeds to build each artifact. This involves running the appropriate build tool on the input files and saving the artifact and its trace file, as specified in the corresponding facet.
Lake uses two separate hash algorithms. Text files are hashed after normalizing newlines, so that files that differ only by platform-specific newline conventions are hashed identically. Other files are hashed without any normalization.
Along with the trace files, Lean caches input hashes. Whenever an artifact is built, its hash is saved in a separate file that can be re-read instead of computing the hash from scratch. This is a performance optimization. This feature can be disabled, causing all hashes to be recomputed from their inputs, using the `--rehash[](Build-Tools-and-Distribution/Lake/#lake-flag--rehash)` command-line option.
During a build, the following directories are provided to the underlying build tools:
  * The _source directory_ contains Lean source code that is available for import.
  * The _library directories_ contain [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file) along with the shared and static libraries that are available for linking; it normally consists of the [root package](Build-Tools-and-Distribution/Lake/#--tech-term-root-package)'s library directory (found in `.lake/build/lib`), the library directories for the other packages in the workspace, the library directory for the current Lean toolchain, and the system library directory.
  * The _Lake home_ is the directory in which Lake is installed, including binaries, source code, and libraries. The libraries in the Lake home are needed to elaborate Lake configuration files, which have access to the full power of Lean.


###  24.1.1.2. Facets[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-facets "Permalink")
A _facet_ describes the production of a target from another. Conceptually, any target may have facets. However, executables, external libraries, and custom targets provide only a single implicit facet. Packages, libraries, and modules have multiple facets that can be requested by name when invoking [`lake build`](Build-Tools-and-Distribution/Lake/#build) to select the corresponding target.
When no facet is explicitly requested, but an initial target is designated, [`lake build`](Build-Tools-and-Distribution/Lake/#build) produces the initial target's _default facet_. Each type of initial target has a corresponding default facet (e.g. producing an executable binary from an executable target or building a package's [default targets](Build-Tools-and-Distribution/Lake/#--tech-term-default-targets)); other facets may be explicitly requested in the [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) or via Lake's [command-line interface](Build-Tools-and-Distribution/Lake/#lake-cli). Lake's internal API may be used to write custom facets.
The facets available for packages are: 

`extraDep` 
    
The default facets of the package's extra dependency targets, specified in the `extraDepTargets[](Build-Tools-and-Distribution/Lake/#Lake___PackageConfig-extraDepTargets)` field. 

`deps` 
    
The package's [direct dependencies](Build-Tools-and-Distribution/Lake/#--tech-term-direct-dependencies). 

`transDeps` 
    
The package's [transitive dependencies](Build-Tools-and-Distribution/Lake/#--tech-term-transitive-dependencies), topologically sorted. 

`optCache` 
    
A package's optional cached build archive (e.g., from Reservoir or GitHub). Will **not** cause the whole build to fail if the archive cannot be fetched. 

`cache` 
    
A package's cached build archive (e.g., from Reservoir or GitHub). Will cause the whole build to fail if the archive cannot be fetched. 

`optBarrel` 
    
A package's optional cached build archive (e.g., from Reservoir or GitHub). Will **not** cause the whole build to fail if the archive cannot be fetched. 

`barrel` 
    
A package's cached build archive (e.g., from Reservoir or GitHub). Will cause the whole build to fail if the archive cannot be fetched. 

`optRelease` 
    
A package's optional build archive from a GitHub release. Will **not** cause the whole build to fail if the release cannot be fetched. 

`release` 
    
A package's build archive from a GitHub release. Will cause the whole build to fail if the archive cannot be fetched.
The facets available for libraries are: 

`leanArts` 
    
The artifacts that the Lean compiler produces for the library or executable ([`*.olean`](Elaboration-and-Compilation/#--tech-term-___olean-file), `*.ilean`, and `*.c` files). 

`static` 
    
The static library produced by the C compiler from the `leanArts` (that is, a `*.a` file). 

`static.export` 
    
The static library produced by the C compiler from the `leanArts` (that is, a `*.a` file), with exported symbols. 

`shared` 
    
The shared library produced by the C compiler from the `leanArts` (that is, a `*.so`, `*.dll`, or `*.dylib` file, depending on the platform). 

`extraDep` 
    
A Lean library's `extraDepTargets[](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig-extraDepTargets)` and those of its package.
Executables have a single `exe` facet that consists of the executable binary.
The facets available for modules are: 

`lean` 
    
The module's Lean source file. 

`leanArts` (default)
    
The module's Lean artifacts (`*.olean`, `*.ilean`, `*.c` files). 

`deps` 
    
The module's dependencies (e.g., imports or shared libraries). 

`olean` 
    
The module's [`.olean` file](Elaboration-and-Compilation/#--tech-term-___olean-file).  

`ilean` 
    
The module's `.ilean` file, which is metadata used by the Lean language server. 

`header` 
    
The parsed module header of the module's source file. 

`input` 
    
The module's processed Lean source file. Combines tracing the file with parsing its header. 

`imports` 
    
The immediate imports of the Lean module, but not the full set of transitive imports.  

`precompileImports` 
    
The transitive imports of the Lean module, compiled to object code. 

`transImports` 
    
The transitive imports of the Lean module, as [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file). 

`allImports` 
    
Both the immediate and transitive imports of the Lean module. 

`setup` 
    
All of a module's dependencies: transitive local imports and shared libraries to be loaded with `--load-dynlib`. Returns the list of shared libraries to load along with their search path. 

`ir` 
    
The `.ir` file produced by `lean` (with the [experimental module system](Source-Files-and-Modules/#module-structure) enabled). 

`c` 
    
The C file produced by the Lean compiler. 

`bc` 
    
LLVM bitcode file, produced by the Lean compiler. 

`c.o` 
    
The compiled object file, produced from the C file. On Windows, this is equivalent to `.c.o.noexport`, while it is equivalent to `.c.o.export` on other platforms. 

`c.o.export` 
    
The compiled object file, produced from the C file, with Lean symbols exported. 

`c.o.noexport` 
    
The compiled object file, produced from the C file, with Lean symbols exported. 

`bc.o` 
    
The compiled object file, produced from the LLVM bitcode file. 

`o` 
    
The compiled object file for the configured backend. 

`dynlib` 
    
A shared library (e.g., for the Lean option `--load-dynlib`).
###  24.1.1.3. Scripts[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-scripts "Permalink")
Lake [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) files may include _Lake scripts_ , which are embedded programs that can be executed from the command line. Scripts are intended to be used for project-specific tasks that are not already well-served by Lake's other features. While ordinary executable programs are run in the `[IO](IO/Logical-Model/#IO "Documentation for IO")` [monad](Functors___-Monads-and--do--Notation/#--tech-term-Monad), scripts are run in `ScriptM`, which extends `[IO](IO/Logical-Model/#IO "Documentation for IO")` with information about the workspace. Because they are Lean definitions, Lake scripts can only be defined in the Lean configuration format.
###  24.1.1.4. Test and Lint Drivers[🔗](find/?domain=Verso.Genre.Manual.section&name=test-lint-drivers "Permalink")
A _test driver_ is responsible for running the tests for a package. Test drivers may be executable targets or [Lake scripts](Build-Tools-and-Distribution/Lake/#--tech-term-Lake-scripts), in which case the [`lake test`](Build-Tools-and-Distribution/Lake/#test) command runs them, or they may be libraries, in which case [`lake test`](Build-Tools-and-Distribution/Lake/#test) causes them to be elaborated, with the expectation that test failures are registered as elaboration failures.
Similarly, a _lint driver_ is responsible for checking the code for stylistic issues. Lint drivers may be executables or scripts, which are run by [`lake lint`](Build-Tools-and-Distribution/Lake/#lint).
A test or lint driver can be configured by either setting the `testDriver[](Build-Tools-and-Distribution/Lake/#Lake___PackageConfig-testDriver)` or `lintDriver[](Build-Tools-and-Distribution/Lake/#Lake___PackageConfig-lintDriver)` package configuration options or by tagging a script, executable, or library with the `test_driver` or `lint_driver` attribute in a Lean-format configuration file. A definition in a dependency can be used as a test or lint driver by using the `<pkg>/<name>` syntax for the appropriate configuration option.
###  24.1.1.5. GitHub Release Builds[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-github "Permalink")
Lake supports uploading and downloading build artifacts (i.e., the archived build directory) to/from the GitHub releases of packages. This enables end users to fetch pre-built artifacts from the cloud without needed to rebuild the package from source themselves. The `LAKE_NO_CACHE[](Build-Tools-and-Distribution/Lake/#LAKE_NO_CACHE)` environment variable can be used to disable this feature.
####  24.1.1.5.1. Downloading[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Concepts-and-Terminology--GitHub-Release-Builds--Downloading "Permalink")
To download artifacts, one should configure the package options `releaseRepo` and `buildArchive` to point to the GitHub repository hosting the release and the correct artifact name within it (if the defaults are not sufficient). Then, set `preferReleaseBuild := true` to tell Lake to fetch and unpack it as an extra package dependency.
Lake will only fetch release builds as part of its standard build process if the package wanting it is a dependency (as the root package is expected to modified and thus not often compatible with this scheme). However, should one wish to fetch a release for a root package (e.g., after cloning the release's source but before editing), one can manually do so via `lake build :release`.
Lake internally uses `curl` to download the release and `tar` to unpack it, so the end user must have both tools installed in order to use this feature. If Lake fails to fetch a release for any reason, it will move on to building from the source. This mechanism is not technically limited to GitHub: any Git host that uses the same URL scheme works as well.
####  24.1.1.5.2. Uploading[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Concepts-and-Terminology--GitHub-Release-Builds--Uploading "Permalink")
To upload a built package as an artifact to a GitHub release, Lake provides the [`lake upload`](Build-Tools-and-Distribution/Lake/#upload) command as a convenient shorthand. This command uses `tar` to pack the package's build directory into an archive and uses `gh release upload` to attach it to a pre-existing GitHub release for the specified tag. Thus, in order to use it, the package uploader (but not the downloader) needs to have `gh`, the GitHub CLI, installed and in `PATH`.
###  24.1.1.6. Artifact Caches[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-cache "Permalink")
**This is an experimental feature that is still undergoing development.**
Lake supports a _local artifact cache_ that stores individual build products, tracking the complete set of inputs that gave rise to them. Each [toolchain](Build-Tools-and-Distribution/#--tech-term-toolchain) has its own cache because intermediate build products are not compatible between toolchain versions. However, a toolchain's cache is shared between all local [workspaces](Build-Tools-and-Distribution/Lake/#--tech-term-workspace) that use it, so common dependencies don't need to be rebuilt. If two separate workspaces with the same toolchain depend on the same package, then they can share each others' build products.
Because it is an experimental feature, the local cache is disabled by default. It is only enabled when the `LAKE_ARTIFACT_CACHE[](Build-Tools-and-Distribution/Lake/#LAKE_ARTIFACT_CACHE)` environment variable is set to `true` or when the `enableArtifactCache` field is set to `true` in the [configuration file](Build-Tools-and-Distribution/Lake/#lake-config).
####  24.1.1.6.1. Remote Artifact Caches[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-cache-remote "Permalink")
Build products can be retrieved from remote cache servers and placed into the local cache. This makes it possible to completely avoid local builds. The [`lake cache get`](Build-Tools-and-Distribution/Lake/#cache-get) command is used to download artifacts into the local cache.
Compared to [GitHub release builds](Build-Tools-and-Distribution/Lake/#lake-github), the remote artifact cache is much more fine-grained. It tracks build products at the level of individual source files, [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file), and object code, rather than at the level of entire packages.
####  24.1.1.6.2. Mappings[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Concepts-and-Terminology--Artifact-Caches--Mappings "Permalink")
When passed the `-o` option, [`lake build`](Build-Tools-and-Distribution/Lake/#build) tracks the inputs used to generate each build product. These are stored to a _mappings file_ in JSON lines format, where each line of the file must be a valid JSON object. A mappings file tracks a single build, and includes all intermediate and final build products for the workspace's [root package](Build-Tools-and-Distribution/Lake/#--tech-term-root-package), but not for its dependencies. This includes build products that were already up to date and not regenerated. The [`lake cache put`](Build-Tools-and-Distribution/Lake/#cache-put) command uploads the build products in the mappings file to the remote from the local cache to the remote cache.
####  24.1.1.6.3. Configuration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Concepts-and-Terminology--Artifact-Caches--Configuration "Permalink")
Remote artifact caches are configured using the following environment variables:
  * `LAKE_CACHE_KEY[](Build-Tools-and-Distribution/Lake/#LAKE_CACHE_KEY)`
  * `LAKE_CACHE_ARTIFACT_ENDPOINT[](Build-Tools-and-Distribution/Lake/#LAKE_CACHE_ARTIFACT_ENDPOINT)`
  * `LAKE_CACHE_REVISION_ENDPOINT[](Build-Tools-and-Distribution/Lake/#LAKE_CACHE_REVISION_ENDPOINT)`


##  24.1.2. Command-Line Interface[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-cli "Permalink")
Lake's command-line interface is structured into a series of subcommands. All of the subcommands share the ability to be configured by certain environment variables and global command-line options. Each subcommand should be understood as a utility in its own right, with its own required argument syntax and documentation.
Some of Lake's commands delegate to other command-line utilities that are not included in a Lean distribution. These utilities must be available on the `PATH` in order to use the corresponding features:
  * `git` is required in order to access Git dependencies.
  * `tar` is required to create or extract cloud build archives, and `curl` is required to fetch them.
  * `gh` is required to upload build artifacts to GitHub releases.


Lean distributions include a C compiler toolchain.
###  24.1.2.1. Environment Variables[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-environment "Permalink")
When invoking the Lean compiler or other tools, Lake sets or modifies a number of environment variables. These values are system-dependent. Invoking [`lake env`](Build-Tools-and-Distribution/Lake/#env) without any arguments displays the environment variables and their values. Otherwise, the provided command is invoked in Lake's environment.
The following variables are set, overriding previous values:  
|  `LAKE`  |  The detected Lake executable   |  
| --- | --- |  
|  `LAKE_HOME[](Build-Tools-and-Distribution/Lake/#LAKE_HOME)`  |  The detected [Lake home](Build-Tools-and-Distribution/Lake/#--tech-term-Lake-home)  |  
|  `LEAN_SYSROOT[](Build-Tools-and-Distribution/Lake/#LEAN_SYSROOT)`  |  The detected Lean [toolchain](Build-Tools-and-Distribution/#--tech-term-toolchain) directory   |  
|  `LEAN_AR[](Build-Tools-and-Distribution/Lake/#LEAN_AR)`  |  The detected Lean `ar` binary   |  
|  `LEAN_CC[](Build-Tools-and-Distribution/Lake/#LEAN_CC)`  |  The detected C compiler (if not using the bundled one)  |  
The following variables are augmented with additional information:  
|  `LEAN_PATH`  |  Lake's and the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s Lean [library directories](Build-Tools-and-Distribution/Lake/#--tech-term-library-directories) are added.   |  
| --- | --- |  
|  `LEAN_SRC_PATH`  |  Lake's and the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s [source directories](Build-Tools-and-Distribution/Lake/#--tech-term-source-directory) are added.   |  
|  `PATH`  |  Lean's, Lake's, and the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s [binary directories](Build-Tools-and-Distribution/Lake/#--tech-term-binary-directory) are added. On Windows, Lean's and the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s [library directories](Build-Tools-and-Distribution/Lake/#--tech-term-library-directories) are also added.   |  
|  `DYLD_LIBRARY_PATH`  |  On macOS, Lean's and the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s [library directories](Build-Tools-and-Distribution/Lake/#--tech-term-library-directories) are added.   |  
|  `LD_LIBRARY_PATH`  |  On platforms other than Windows and macOS, Lean's and the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s [library directories](Build-Tools-and-Distribution/Lake/#--tech-term-library-directories) are added.  |  
Lake itself can be configured with the following environment variables:  
|  `ELAN_HOME`  |  The location of the [Elan](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan) installation, which is used for [automatic toolchain updates](Build-Tools-and-Distribution/Lake/#automatic-toolchain-updates).  |  
| --- | --- |  
|  `ELAN`  |  The location of the `elan` binary, which is used for [automatic toolchain updates](Build-Tools-and-Distribution/Lake/#automatic-toolchain-updates). If it is not set, an occurrence of `elan` must exist on the `PATH`.  |  
|  `LAKE_HOME`  |  The location of the Lake installation. This environment variable is only consulted when Lake is unable to determine its installation path from the location of the `lake` executable that's currently running.   |  
|  `LEAN_SYSROOT`  |  The location of the Lean installation, used to find the Lean compiler, the standard library, and other bundled tools. Lake first checks whether its binary is colocated with a Lean install, using that installation if so. If not, or if `LAKE_OVERRIDE_LEAN` is true, then Lake consults `LEAN_SYSROOT[](Build-Tools-and-Distribution/Lake/#LEAN_SYSROOT)`. If this is not set, Lake consults the `LEAN` environment variable to find the Lean compiler, and attempts to find the Lean installation relative to the compiler. If `LEAN[](Build-Tools-and-Distribution/Lake/#LEAN)` is set but empty, Lake considers Lean to be disabled. If `LEAN_SYSROOT[](Build-Tools-and-Distribution/Lake/#LEAN_SYSROOT)` and `LEAN[](Build-Tools-and-Distribution/Lake/#LEAN)` are unset, the first occurrence of `lean` on the `PATH` is used to find the installation.   |  
|  `LEAN_CC` and `LEAN_AR`  |  If `LEAN_CC[](Build-Tools-and-Distribution/Lake/#LEAN_CC)` and/or `LEAN_AR[](Build-Tools-and-Distribution/Lake/#LEAN_AR)` is set, its value is used as the C compiler or `ar` command when building libraries. If not, Lake will fall back to the bundled tool in the Lean installation. If the bundled tool is not found, the value of `CC` or `AR`, followed by a `cc` or `ar` on the `PATH`, are used.   |  
|  `LAKE_NO_CACHE`  |  If true, Lake does not use cached builds from [Reservoir](https://reservoir.lean-lang.org/) or [GitHub](Build-Tools-and-Distribution/Lake/#lake-github). This environment variable can be overridden using the `--try-cache[](Build-Tools-and-Distribution/Lake/#lake-flag--try-cache)` command-line option.  |  
|  `LAKE_ARTIFACT_CACHE`  |  If true, Lake uses the artifact cache. This is an experimental feature.  |  
|  `LAKE_CACHE_KEY`  |  Defines an authentication key for the [remote artifact cache](Build-Tools-and-Distribution/Lake/#lake-cache-remote).  |  
|  `LAKE_CACHE_ARTIFACT_ENDPOINT`  |  The base URL for the [remote artifact cache](Build-Tools-and-Distribution/Lake/#lake-cache-remote) used for artifact uploads. If set, then `LAKE_CACHE_REVISION_ENDPOINT[](Build-Tools-and-Distribution/Lake/#LAKE_CACHE_REVISION_ENDPOINT)` must also be set. If neither of these are set, Lake will use Reservoir instead.  |  
|  `LAKE_CACHE_REVISION_ENDPOINT`  |  The base URL for the [remote artifact cache](Build-Tools-and-Distribution/Lake/#lake-cache-remote) used to upload the [input/output mappings](Build-Tools-and-Distribution/Lake/#--tech-term-mappings-file) for each artifact. If set, then `LAKE_CACHE_ARTIFACT_ENDPOINT[](Build-Tools-and-Distribution/Lake/#LAKE_CACHE_ARTIFACT_ENDPOINT)` must also be set. If neither of these are set, Lake will use Reservoir instead.  |  
Lake considers an environment variable to be true when its value is `y`, `yes`, `t`, `true`, `on`, or `1`, compared case-insensitively. It considers a variable to be false when its value is `n`, `no`, `f`, `false`, `off`, or `0`, compared case-insensitively. If the variable is unset, or its value is neither true nor false, a default value is used.
###  24.1.2.2. Options[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Options "Permalink")
Lake's command-line interface provides a number of global options as well as subcommands that perform important tasks. Single-character flags cannot be combined; `-HR` is not equivalent to `-H -R`. 

`--version` 
    
Lake outputs its version and exits without doing anything else. 

`--help` or `-h` 
    
Lake outputs its version along with usage information and exits without doing anything else. Subcommands may be used with `--help[](Build-Tools-and-Distribution/Lake/#lake-flag--help)`, in which case usage information for the subcommand is output. 

`--dir=DIR` or `-d=DIR` 
    
Use the provided directory as location of the package instead of the current working directory. This is not always equivalent to changing to the directory first, because the version of `lake` indicated by the current directory's [toolchain file](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#--tech-term-toolchain-file) will be used, rather than that of `DIR`. 

`--file=FILE` or `-f=FILE` 
    
Use the specified [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) file instead of the default. 

`--old` 
    
Only rebuild modified modules, ignoring transitive dependencies. Modules that import the modified module will not be rebuilt. In order to accomplish this, file modification times are used instead of hashes to determine whether a module has changed. 

`--rehash` or `-H` 
    
Ignored cached file hashes, recomputing them. Lake uses hashes of dependencies to determine whether to rebuild an artifact. These hashes are cached on disk whenever a module is built. To save time during builds, these cached hashes are used instead of recomputing each hash unless `--rehash[](Build-Tools-and-Distribution/Lake/#lake-flag--rehash)` is specified. 

`--update` 
    
Update dependencies after the [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) is loaded but prior to performing other tasks, such as a build. This is equivalent to running `lake update` before the selected command, but it may be faster due to not having to load the configuration twice. 

`--packages=FILE` 
    
Use the contents of `FILE` to specify the versions of some or all dependencies instead of the manifest. `FILE` should be a syntactically valid manifest, but it does not need to be complete. 

`--reconfigure` or `-R` 
    
Normally, the [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) file is [elaborated](Notations-and-Macros/Elaborators/#--tech-term-elaborators) when a package is first configured, with the result cached to a [`.olean` file](Elaboration-and-Compilation/#--tech-term-___olean-file) that is used for future invocations until the package configuration Providing this flag causes the configuration file to be re-elaborated. 

`--keep-toolchain` 
    
By default, Lake attempts to update the local [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s [toolchain file](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#--tech-term-toolchain-file). Providing this flag disables [automatic toolchain updates](Build-Tools-and-Distribution/Lake/#automatic-toolchain-updates). 

`--no-build` 
    
Lake exits immediately if a build target is not up-to-date, returning a non-zero exit code. 

`--no-cache` 
    
Instead of using available cloud build caches, build all packages locally. Build caches are not downloaded. 

`--try-cache` 
    
attempt to download build caches for supported packages
###  24.1.2.3. Controlling Output[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Controlling-Output "Permalink")
These options provide allow control over the [log](Build-Tools-and-Distribution/Lake/#--tech-term-log) that is produced while building. In addition to showing or hiding messages, a build can be made to fail when warnings or even information is emitted; this can be used to enforce a style guide that disallows output during builds. 

`--quiet`, `-q` 
    
Hides informational logs and the progress indicator. 

`--verbose`, `-v` 
    
Shows trace logs (typically command invocations) and built [targets](Build-Tools-and-Distribution/Lake/#--tech-term-target). 

`--ansi`, `--no-ansi` 
    
Enables or disables the use of [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code) that add colors and animations to Lake's output. 

`--log-level=LV` 
    
Sets the minimum level of [logs](Build-Tools-and-Distribution/Lake/#--tech-term-log) to be shown when builds succeed. `LV` may be `trace`, `info`, `warning`, or `error`, compared case-insensitively. When a build fails, all levels are shown. The default log level is `info`. 

`--fail-level=LV` 
    
Sets the threshold at which a message in the [log](Build-Tools-and-Distribution/Lake/#--tech-term-log) causes a build to be considered a failure. If a message is emitted to the log with a level that is greater than or equal to the threshold, the build fails. `LV` may be `trace`, `info`, `warning`, or `error`, compared case-insensitively; it is `error` by default. 

`--iofail` 
    
Causes builds to fail if any I/O or other info is logged. This is equivalent to `--fail-level[](Build-Tools-and-Distribution/Lake/#lake-option--fail-level)=info`. 

`--wfail` 
    
Causes builds to fail if any warnings are logged. This is equivalent to `--fail-level[](Build-Tools-and-Distribution/Lake/#lake-option--fail-level)=warning`.
###  24.1.2.4. Automatic Toolchain Updates[🔗](find/?domain=Verso.Genre.Manual.section&name=automatic-toolchain-updates "Permalink")
The [`lake update`](Build-Tools-and-Distribution/Lake/#update) command checks for changes to dependencies, fetching their sources and updating the [manifest](Build-Tools-and-Distribution/Lake/#--tech-term-manifest) accordingly. By default, [`lake update`](Build-Tools-and-Distribution/Lake/#update) also attempts to update the [root package](Build-Tools-and-Distribution/Lake/#--tech-term-root-package)'s [toolchain file](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#--tech-term-toolchain-file) when a new version of a dependency specifies an updated toolchain. This behavior can be disabled with the `--keep-toolchain[](Build-Tools-and-Distribution/Lake/#lake-flag--keep-toolchain)` flag.
If multiple dependencies specify newer toolchains, Lake selects the newest compatible toolchain, if it exists. To determine the newest compatible toolchain, Lake parses the toolchain listed in the packages' `lean-toolchain` files into four categories:
  * Releases, which are compared by version number (e.g., `v4.4.0` < `v4.8.0` and `v4.6.0-rc1` < `v4.6.0`)
  * Nightly builds, which are compared by date (e.g., `nightly-2024-01-10` < `nightly-2024-10-01`)
  * Builds from pull requests to the Lean compiler, which are incomparable
  * Other versions, which are also incomparable


Toolchain versions from multiple categories are incomparable. If there is not a single newest toolchain, Lake will print a warning and continue updating without changing the toolchain.
If Lake does find a new toolchain, then it updates the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s `lean-toolchain` file accordingly and restarts the [`lake update`](Build-Tools-and-Distribution/Lake/#update) using the new toolchain's Lake. If [Elan](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan) is detected, it will spawn the new Lake process via `elan run` with the same arguments Lake was initially run with. If Elan is missing, it will prompt the user to restart Lake manually and exit with a special error code (namely, `4`). The Elan executable used by Lake can be configured using the `ELAN[](Build-Tools-and-Distribution/Lake/#ELAN)` environment variable.
###  24.1.2.5. Creating Packages[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Creating-Packages "Permalink")
[🔗](find/?domain=Manual.lakeCommand&name=new "Permalink")Lake command
```
lake new name [template][.language]
```

Running [`lake new`](Build-Tools-and-Distribution/Lake/#new) creates an initial Lean package in a new directory. This command is equivalent to creating a directory named `name` and then running [`lake init`](Build-Tools-and-Distribution/Lake/#init)
[🔗](find/?domain=Manual.lakeCommand&name=init "Permalink")Lake command
```
lake init name [template][.language]
```

Running [`lake init`](Build-Tools-and-Distribution/Lake/#init) creates an initial Lean package in the current directory. The package's contents are based on a template, with the names of the [package](Build-Tools-and-Distribution/Lake/#--tech-term-package), its [targets](Build-Tools-and-Distribution/Lake/#--tech-term-target), and their [module roots](Build-Tools-and-Distribution/Lake/#--tech-term-module-roots) derived from the name of the current directory.
The `template` may be: 

`std` (default)
    
Creates a package that contains a library and an executable. 

`exe` 
    
Creates a package that contains only an executable. 

`lib` 
    
Creates a package that contains only a library. 

`math` 
    
Creates a package that contains a library that depends on [Mathlib](https://github.com/leanprover-community/mathlib4).
The `language` selects the file format used for the [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) file and may be `lean` (the default) or `toml`.
###  24.1.2.6. Building and Running[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Building-and-Running "Permalink")
[🔗](find/?domain=Manual.lakeCommand&name=build "Permalink")Lake command
```
lake build [targets...] [-o mappings]
```

Builds the specified facts of the specified targets.
Each of the `targets` is specified by a string of the form:
`[[@]package[/]][target|[+]module][:facet]`
The optional `@` and `+` markers can be used to disambiguate packages and modules from file paths as well as executables, and libraries, which are specified by name as `target`. If not provided, `package` defaults to the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s [root package](Build-Tools-and-Distribution/Lake/#--tech-term-root-package). If the same target name exists in multiple packages in the workspace, then the first occurrence of the target name found in a topological sort of the package dependency graph is selected. Module targets may also be specified by their filename, with an optional facet after a colon.
The available [facets](Build-Tools-and-Distribution/Lake/#--tech-term-facet) depend on whether a package, library, executable, or module is to be built. They are listed in [the section on facets](Build-Tools-and-Distribution/Lake/#lake-facets).
When using the [local artifact cache](Build-Tools-and-Distribution/Lake/#lake-cache), the `-o` option saves a [mappings file](Build-Tools-and-Distribution/Lake/#--tech-term-mappings-file) that tracks the inputs and outputs of each step in the build. This file can be used with [`lake cache get`](Build-Tools-and-Distribution/Lake/#cache-get) and [`lake cache put`](Build-Tools-and-Distribution/Lake/#cache-put) to interact with a remote cache. The mappings file is in JSON Lines format, with one valid JSON object per line, and its filename extension is conventionally `.jsonl`.
Target and Facet Specifications  
|  `a`  |  The [default facet](Build-Tools-and-Distribution/Lake/#--tech-term-default-facet)(s) of target `a`  |  
| --- | --- |  
|  `@a`  |  The [default targets](Build-Tools-and-Distribution/Lake/#--tech-term-default-targets) of [package](Build-Tools-and-Distribution/Lake/#--tech-term-package) `a`  |  
|  `+A`  |  The Lean artifacts of module `A` (because the default facet of modules is `leanArts`)   |  
|  `@a/b`  |  The default facet of target `b` of package `a`  |  
|  `@a/+A:c`  |  The C file compiled from module `A` of package `a`  |  
|  `:foo`  |  The [root package](Build-Tools-and-Distribution/Lake/#--tech-term-root-package)'s facet `foo`  |  
|  `A/B/C.lean:o`  |  The compiled object code for the module in the file `A/B/C.lean`  |  
[🔗](find/?domain=Manual.lakeCommand&name=check-build "Permalink")Lake command
```
lake check-build 
```

Exits with code 0 if the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s [root package](Build-Tools-and-Distribution/Lake/#--tech-term-root-package) has any [default targets](Build-Tools-and-Distribution/Lake/#--tech-term-default-targets) configured. Errors (with exit code 1) otherwise.
[`lake check-build`](Build-Tools-and-Distribution/Lake/#check-build) does **not** verify that the configured default targets are valid. It merely verifies that at least one is specified.
[🔗](find/?domain=Manual.lakeCommand&name=query "Permalink")Lake command
```
lake query [targets...]
```

Builds a set of targets, reporting progress on standard error and outputting the results on standard out. Target results are output in the same order they are listed and end with a newline. If `--json` is set, results are formatted as JSON. Otherwise, they are printed as raw strings.
Targets which do not have output configured will be printed as an empty string or `null`. For executable targets, the output is the path to the built executable.
Targets are specified using the same syntax as in [`lake build`](Build-Tools-and-Distribution/Lake/#build).
[🔗](find/?domain=Manual.lakeCommand&name=exec "Permalink")Lake command
```
lake exe exe-target [args...]
```

**Alias:** `lake exec`
Looks for the executable target `exe-target` in the workspace, builds it if it is out of date, and then runs it with the given `args` in Lake's environment.
See [`lake build`](Build-Tools-and-Distribution/Lake/#build) for the syntax of target specifications and [`lake env`](Build-Tools-and-Distribution/Lake/#env) for a description of how the environment is set up.
[🔗](find/?domain=Manual.lakeCommand&name=clean "Permalink")Lake command
```
lake clean [packages...]
```

If no package is specified, deletes the [build directories](Build-Tools-and-Distribution/Lake/#--tech-term-build-directory) of every package in the workspace. Otherwise, it just deletes those of the specified `packages`.
[🔗](find/?domain=Manual.lakeCommand&name=env "Permalink")Lake command
```
lake env [cmd [args...]]
```

When `cmd` is provided, it is executed in [the Lake environment](Build-Tools-and-Distribution/Lake/#lake-environment) with arguments `args`.
If `cmd` is not provided, Lake prints the environment in which it runs tools. This environment is system-specific.
[🔗](find/?domain=Manual.lakeCommand&name=lean "Permalink")Lake command
```
lake lean file [-- args...]
```

Builds the imports of the given `file` and then runs `lean` on it using the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s [root package](Build-Tools-and-Distribution/Lake/#--tech-term-root-package)'s additional Lean arguments and the given `args`, in that order. The `lean` process is executed in [Lake's environment](Build-Tools-and-Distribution/Lake/#lake-environment).
###  24.1.2.7. Module Imports[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Module-Imports "Permalink")
[🔗](find/?domain=Manual.lakeCommand&name=shake "Permalink")Lake command
```
lake shake [options...] [module ...]
```

Checks the current project for unused imports by analyzing generated [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file) to deduce required imports, ensuring that every import contributes some constant or other elaboration dependency.
If a `module` is specified, then it and all files that are transitively reachable from it are checked. Otherwise, the package's [default targets](Build-Tools-and-Distribution/Lake/#--tech-term-default-targets) are checked.
Source files can contain special comments to control the behavior of [`lake shake`](Build-Tools-and-Distribution/Lake/#shake): 

`module -- shake: keep-downstream` 
    
Preserves this module in all downstream modules. 

`module -- shake: keep-all` 
    
Preserves all existing imports in this module. 

`import X -- shake: keep` 
    
Preserves this specific import.
The `options` may be: 

`--force` 
    
Skip the `lake build --no-build` sanity check 

`--keep-implied` 
    
Preserve imports implied by other imports 

`--keep-prefix` 
    
Prefer parent module imports over specific submodules 

`--keep-public` 
    
Preserve all `public` imports for API stability 

`--add-public` 
    
Add new imports as `public` if they were in the original public closure 

`--explain` 
    
Show which constants require each import 

`--fix` 
    
Apply suggested fixes directly to source files 

`--gh-style` 
    
Output in GitHub problem matcher format
###  24.1.2.8. Development Tools[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Development-Tools "Permalink")
Lake includes support for specifying standard development tools and workflows. On the command line, these tools can be invoked using the appropriate `lake` subcommands.
####  24.1.2.8.1. Tests and Linters[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Development-Tools--Tests-and-Linters "Permalink")
[🔗](find/?domain=Manual.lakeCommand&name=test "Permalink")Lake command
```
lake test [-- args...]
```

Test the workspace's root package using its configured [test driver](Build-Tools-and-Distribution/Lake/#--tech-term-test-driver).
A test driver that is an executable will be built and then run with the package configuration's `testDriverArgs` plus the CLI `args`. A test driver that is a [Lake script](Build-Tools-and-Distribution/Lake/#--tech-term-Lake-scripts) is run with the same arguments as an executable test driver. A library test driver will just be built; it is expected that tests are implemented such that failures cause the build to fail via elaboration-time errors.
[🔗](find/?domain=Manual.lakeCommand&name=lint "Permalink")Lake command
```
lake lint [-- args...]
```

Lint the workspace's root package using its configured lint driver
A script lint driver will be run with the package configuration's `lintDriverArgs` plus the CLI `args`. An executable lint driver will be built and then run like a script.
[🔗](find/?domain=Manual.lakeCommand&name=check-test "Permalink")Lake command
```
lake check-test 
```

Check if there is a properly configured test driver
Exits with code 0 if the workspace's root package has a properly configured lint driver. Errors (with code 1) otherwise.
Does NOT verify that the configured test driver actually exists in the package or its dependencies. It merely verifies that one is specified.
This is useful for distinguishing between failing tests and incorrectly configured packages.
[🔗](find/?domain=Manual.lakeCommand&name=check-lint "Permalink")Lake command
```
lake check-lint 
```

Check if there is a properly configured lint driver
Exits with code 0 if the workspace's root package has a properly configured lint driver. Errors (with code 1) otherwise.
Does NOT verify that the configured lint driver actually exists in the package or its dependencies. It merely verifies that one is specified.
This is useful for distinguishing between failing lints and incorrectly configured packages.
####  24.1.2.8.2. Scripts[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Development-Tools--Scripts "Permalink")
[🔗](find/?domain=Manual.lakeCommand&name=scripts "Permalink")Lake command
```
lake script list 
```

**Alias:** `lake scripts`
Lists the available [scripts](Build-Tools-and-Distribution/Lake/#lake-scripts) in the workspace.
[🔗](find/?domain=Manual.lakeCommand&name=run "Permalink")Lake command
```
lake script run [[package/]script [args...]]
```

**Alias:** `lake run`
This command runs the `script` of the workspace (or the specified `package`), passing `args` to it.
A bare [`lake run`](Build-Tools-and-Distribution/Lake/#script-run) command will run the default script(s) of the root package(with no arguments).
[🔗](find/?domain=Manual.lakeCommand&name=script%20doc "Permalink")Lake command
```
lake script doc script
```

Prints the documentation comment for `script`.
####  24.1.2.8.3. Language Server[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Development-Tools--Language-Server "Permalink")
[🔗](find/?domain=Manual.lakeCommand&name=serve "Permalink")Lake command
```
lake serve [-- args...]
```

Runs the Lean language server in the workspace's root project with the [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration)'s `moreServerArgs` field and `args`.
This command is typically invoked by editors or other tooling, rather than manually.
###  24.1.2.9. Dependency Management[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Dependency-Management "Permalink")
[🔗](find/?domain=Manual.lakeCommand&name=update "Permalink")Lake command
```
lake update [packages...]
```

Updates the Lake package [manifest](Build-Tools-and-Distribution/Lake/#--tech-term-manifest) (i.e., `lake-manifest.json`), downloading and upgrading packages as needed. For each new (transitive) [Git dependency](Build-Tools-and-Distribution/Lake/#--tech-term-Git-dependencies), the appropriate commit is cloned into a subdirectory of the workspace's [package directory](Build-Tools-and-Distribution/Lake/#--tech-term-package-directory). No copy is made of local dependencies.
If a set of packages `packages` is specified, then these dependencies are upgraded to the latest version compatible with the package's configuration (or removed if removed from the configuration). If there are dependencies on multiple versions of the same package, an arbitrary version is selected.
A bare [`lake update`](Build-Tools-and-Distribution/Lake/#update) will upgrade all dependencies.
###  24.1.2.10. Packaging and Distribution[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Packaging-and-Distribution "Permalink")
[🔗](find/?domain=Manual.lakeCommand&name=upload "Permalink")Lake command
```
lake upload tag
```

Packs the root package's `buildDir` into a `tar.gz` archive using `tar` and then uploads the asset to the pre-existing [GitHub](https://github.com) release `tag` using [`gh`](https://cli.github.com/). Other hosts are not yet supported.
####  24.1.2.10.1. Cached Cloud Builds[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Packaging-and-Distribution--Cached-Cloud-Builds "Permalink")
**These commands are still experimental.** They are likely change in future versions of Lake based on user feedback. Packages that use Reservoir cloud build archives should enable the `platformIndependent[](Build-Tools-and-Distribution/Lake/#Lake___PackageConfig-platformIndependent)` setting.
[🔗](find/?domain=Manual.lakeCommand&name=pack "Permalink")Lake command
```
lake pack [archive.tar.gz]
```

Packs the root package's [build directory](Build-Tools-and-Distribution/Lake/#--tech-term-build-directory) into a gzipped tar archive using `tar`. If a path for the archive is not specified, the archive in the package's Lake directory (`.lake`) and named according to its `buildArchive` setting. This command does not build any artifacts: it only archives what is present. Users should ensure that the desired artifacts are present before running this command.
[🔗](find/?domain=Manual.lakeCommand&name=unpack "Permalink")Lake command
```
lake unpack [archive.tar.gz]
```

Unpacks the contents of the gzipped tar archive `archive.tgz` into the root package's [build directory](Build-Tools-and-Distribution/Lake/#--tech-term-build-directory). If `archive.tgz` is not specified, the package's `buildArchive` setting is used to determine a filename, and the file is expected in package's Lake directory (`.lake`).
###  24.1.2.11. Local Caches[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Local-Caches "Permalink")
[`lake cache get`](Build-Tools-and-Distribution/Lake/#cache-get) and [`lake cache put`](Build-Tools-and-Distribution/Lake/#cache-put) are used to interact with remote cache servers. These commands are **experimental** , and are only useful if the [local cache](Build-Tools-and-Distribution/Lake/#lake-cache) is enabled.
Both commands can be configured to use a cache scope, which is a server-specific identifier for a set of artifacts for a package. On Reservoir, scopes are currently identical with GitHub repositories, but may include toolchain and platform information in the future. Other remote artifact caches may use any scope scheme that they want. Cache scopes are specified using the `--scope` option. Cache scopes are not identical to the scopes used to require packages from Reservoir.
[🔗](find/?domain=Manual.lakeCommand&name=cache%20get "Permalink")Lake command
```
lake cache get [mappings] [--max-revs= cn] [--rev= commit-hash] [--repo= github-repo] [--platform= target-triple] [--toolchain=name] [--scope= remote-scope]
```

Downloads artifacts for packages in the workspace from a remote cache service to the local Lake [artifact cache](Build-Tools-and-Distribution/Lake/#--tech-term-local-artifact-cache). The cache service used can be specified via the `--service` option. Otherwise, Lake will use the system default, or, if none is configured, Reservoir. See [`lake cache services`](Build-Tools-and-Distribution/Lake/#cache-services) for more information on how to configure services.
If an input-to-outputs `mappings` file, a `remote-scope`, or a `github-repo` is provided, Lake will download artifacts for the root package. Otherwise, it will download artifacts for each package in the root's dependency tree in order (using Reservoir). Non-Reservoir dependencies will be skipped.
For Reservoir, setting `--repo[](Build-Tools-and-Distribution/Lake/#lake-option--repo)` will make Lake lookup artifacts for the root package by a repository name, rather than the package's. This can be used to download artifacts for a fork of the Reservoir package (if such artifacts are available). The `--platform[](Build-Tools-and-Distribution/Lake/#lake-option--platform)` and `--toolchain[](Build-Tools-and-Distribution/Lake/#lake-option--toolchain)` options can be used to download artifacts for a different platform/toolchain configuration than Lake detects. For a custom endpoint, the full prefix Lake uses can be set via `--scope[](Build-Tools-and-Distribution/Lake/#lake-option--scope)`.
If `--rev` is not set, Lake uses the package's current revision to look up artifacts. Lake will download the artifacts for the most recent commit with available mappings. It will backtrack up to `--max-revs`, which defaults to 100. If set to 0, Lake will search the repository's whole history, or as far back as Git will allow.
While downloading, Lake will continue on when a download for an artifact fails or if the download process for a whole package fails. However, it will report this and exit with a nonzero status code in such cases.
[🔗](find/?domain=Manual.lakeCommand&name=cache%20put "Permalink")Lake command
```
lake cache put mappings scope-option
```

Uploads the input-to-outputs mappings contained in the specified file along with the corresponding output artifacts to a remote cache. The cache service used can be specified via the `--service` option. If not specified, Lake will use the system default, or error if none is configured. See [`lake cache services`](Build-Tools-and-Distribution/Lake/#cache-services) for more information on how to configure services.
Files are uploaded using the AWS Signature Version 4 authentication protocol via `curl`. Thus, the service should generally be an S3-compatible bucket. The authentication key is set via the `LAKE_CACHE_KEY[](Build-Tools-and-Distribution/Lake/#LAKE_CACHE_KEY)` environment variable.
Since Lake does not currently use cryptographically secure hashes for artifacts and outputs, uploads to the cache are prefixed with a scope to avoid clashes. This scoped is configured with the following options:  
|  `--scope[](Build-Tools-and-Distribution/Lake/#lake-option--scope)``=``<remote-scope>`  |  Sets a fixed scope   |  
| --- | --- |  
|  `--repo``=``<github-repo>`  |  Uses the repository + toolchain & platform   |  
|  `--toolchain``=``<name>`  |  With `--repo[](Build-Tools-and-Distribution/Lake/#lake-option--repo)`, sets the toolchain   |  
|  `--platform``=``<target-triple>`  |  With `--repo[](Build-Tools-and-Distribution/Lake/#lake-option--repo)`, sets the platform  |  
At least one of `--scope[](Build-Tools-and-Distribution/Lake/#lake-option--scope)` or `--repo[](Build-Tools-and-Distribution/Lake/#lake-option--repo)` must be set. If `--repo[](Build-Tools-and-Distribution/Lake/#lake-option--repo)` is used, Lake will produce a scope by augmenting the repository with toolchain and platform information as it deems necessary. If `--scope[](Build-Tools-and-Distribution/Lake/#lake-option--scope)` is set, Lake will use the specified scope verbatim.
Artifacts are uploaded to the artifact endpoint with a file name derived from their Lake content hash (and prefixed by the repository or scope). The mappings file is uploaded to the revision endpoint with a file name derived from the package's current Git revision (and prefixed by the full scope). As such, the command will warn if the work tree currently has changes.
[🔗](find/?domain=Manual.lakeCommand&name=cache%20clean "Permalink")Lake command
```
lake cache clean 
```

Deletes the configured Lake [artifact cache](Build-Tools-and-Distribution/Lake/#--tech-term-local-artifact-cache) directory. If a workspace configuration exists, this will delete the cache directory it uses. Otherwise, it will delete the default Lake cache directory for the system.
[🔗](find/?domain=Manual.lakeCommand&name=cache%20services "Permalink")Lake command
```
lake cache services 
```

Prints the name of each configured remote cache service (one per line). Additional services can be added by modifying the system Lake configuration file, which is usually located at `~/.lake/config.toml` but can be set via the `LAKE_CONFIG` environment variable.
The configuration of the system cache could look something like the following:

```
cache.defaultService = "my-s3"
cache.defaultUploadService = "my-s3"

[[cache.service]]
name = "my-s3"
kind = "s3"
artifactEndpoint = "https://my-s3.com/a0"
revisionEndpoint = "https://my-s3.com/r0"

```

If no `cache.defaultService` is configured, Lake will use Reservoir by default.
###  24.1.2.12. Configuration Files[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Command-Line-Interface--Configuration-Files "Permalink")
[🔗](find/?domain=Manual.lakeCommand&name=translate-config "Permalink")Lake command
```
lake translate-config lang [out-file]
```

Translates the loaded package's configuration into another of Lake's supported configuration languages (i.e., either `lean` or `toml`). The produced file is written to `out-file` or, if not provided, the path of the configuration file with the new language's extension. If the output file already exists, Lake will error.
Translation is lossy. It does not preserve comments or formatting and non-declarative configuration is discarded.
##  24.1.3. Configuration File Format[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-config "Permalink")
Lake offers two formats for [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) files: 

TOML
    
The TOML configuration format is fully declarative. Projects that don't include custom targets, facets, or scripts can use the TOML format. Because TOML parsers are available for a wide variety of languages, using this format facilitates integration with tools that are not written in Lean. 

Lean
    
The Lean configuration format is more flexible and allows for custom targets, facets, and scripts. It features an embedded domain-specific language for describing the declarative subset of configuration options that is available from the TOML format. Additionally, the Lake API can be used to express build configurations that are outside of the possibilities of the declarative options.
The command [`lake translate-config`](Build-Tools-and-Distribution/Lake/#translate-config) can be used to automatically convert between the two formats.
Both formats are processed similarly by Lake, which extracts the [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) from the configuration file in the form of internal structure types. When the package is [configured](Build-Tools-and-Distribution/Lake/#--tech-term-Configuring), the resulting data structures are written to `lakefile.olean` in the [build directory](Build-Tools-and-Distribution/Lake/#--tech-term-build-directory).
###  24.1.3.1. Declarative TOML Format[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-config-toml "Permalink")
TOML[ _Tom's Obvious Minimal Language_](https://toml.io/en/) is a standardized format for configuration files. configuration files describe the most-used, declarative subset of Lake [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) files. TOML files denote _tables_ , which map keys to values. Values may consist of strings, numbers, arrays of values, or further tables. Because TOML allows considerable flexibility in file structure, this reference documents the values that are expected rather than the specific syntax used to produce them.
The contents of `lakefile.toml` should denote a TOML table that describes a Lean package. This configuration consists of both scalar fields that describe the entire package, as well as the following fields that contain arrays of further tables:
  * `require`
  * `lean_lib`
  * `lean_exe`


Fields that are not part of the configuration tables described here are presently ignored. To reduce the risk of typos, this is likely to change in the future. Field names not used by Lake should not be used to store metadata to be processed by other tools.
####  24.1.3.1.1. Package Configuration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Declarative-TOML-Format--Package-Configuration "Permalink")
The top-level contents of `lakefile.toml` specify the options that apply to the package itself, including metadata such as the name and version, the locations of the files in the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace), compiler flags to be used for all [targets](Build-Tools-and-Distribution/Lake/#--tech-term-target), and The only mandatory field is `name`, which declares the package's name.
TOML table
```
Package Configuration
```

A `Package`'s declarative configuration.
**Metadata:**
These options describe the package. They are used by [Reservoir](https://reservoir.lean-lang.org/) to index and display packages. If a field is left out, Reservoir may use information from the package's GitHub repository to fill in details. 

`name`
    
**Contains:** The package name
The package's name. 

`version`
    
**Contains:** Version string
The package version. Versions have the form:

```
v!"<major>.<minor>.<patch>[-<specialDescr>]"

```

A version with a `-` suffix is considered a "prerelease".
Lake suggest the following guidelines for incrementing versions:
  * **Major version increment** _(e.g., v1.3.0 → v2.0.0)_ Indicates significant breaking changes in the package. Package users are not expected to update to the new version without manual intervention.
  * **Minor version increment** _(e.g., v1.3.0 → v1.4.0)_ Denotes notable changes that are expected to be generally backwards compatible. Package users are expected to update to this version automatically and should be able to fix any breakages and/or warnings easily.
  * **Patch version increment** _(e.g., v1.3.0 → v1.3.1)_ Reserved for bug fixes and small touchups. Package users are expected to update automatically and should not expect significant breakage, except in the edge case of users relying on the behavior of patched bugs.


**Note that backwards-incompatible changes may occur at any version increment.** The is because the current nature of Lean (e.g., transitive imports, rich metaprogramming, reducibility in proofs), makes it infeasible to define a completely stable interface for a package. Instead, the different version levels indicate a change's intended significance and how difficult migration is expected to be.
Versions of form the `0.x.x` are considered development versions prior to first official release. Like prerelease, they are not expected to closely follow the above guidelines.
Packages without a defined version default to `0.0.0`. 

`versionTags`
    
**Contains:** String pattern
Git tags of this package's repository that should be treated as versions. Package indices (e.g., Reservoir) can make use of this information to determine the Git revisions corresponding to released versions.
Defaults to tags that are "version-like". That is, start with a `v` followed by a digit. 

`description`
    
**Contains:** String
A short description for the package (e.g., for Reservoir). 

`keywords`
    
**Contains:** Array of strings
Custom keywords associated with the package. Reservoir can make use of a package's keywords to group related packages together and make it easier for users to discover them.
Good keywords include the domain (e.g., `math`, `software-verification`, `devtool`), specific subtopics (e.g., `topology`, `cryptology`), and significant implementation details (e.g., `dsl`, `ffi`, `cli`). For instance, Lake's keywords could be `devtool`, `cli`, `dsl`, `package-manager`, and `build-system`. 

`homepage`
    
**Contains:** String
A URL to information about the package.
Reservoir will already include a link to the package's GitHub repository (if the package is sourced from there). Thus, users are advised to specify something else for this (if anything). 

`license`
    
**Contains:** String
The package's license (if one). Should be a valid [SPDX License Expression](https://spdx.github.io/spdx-spec/v3.0/annexes/SPDX-license-expressions/).
Reservoir requires that packages uses an OSI-approved license to be included in its index, and currently only supports single identifier SPDX expressions. For, a list of OSI-approved SPDX license identifiers, see the [SPDX LIcense List](https://spdx.org/licenses/). 

`licenseFiles`
    
**Contains:** Array of paths
Files containing licensing information for the package.
These should be the license files that users are expected to include when distributing package sources, which may be more then one file for some licenses. For example, the Apache 2.0 license requires the reproduction of a `NOTICE` file along with the license (if such a file exists).
Defaults to `#["LICENSE"]`. 

`readmeFile`
    
**Contains:** Path
The path to the package's README.
A README should be a Markdown file containing an overview of the package. Reservoir displays the rendered HTML of this file on a package's page. A nonstandard location can be used to provide a different README for Reservoir and GitHub.
Defaults to `README.md`. 

`reservoir`
    
**Contains:** Boolean
Whether Reservoir should include the package in its index. When set to `false`, Reservoir will not add the package to its index and will remove it if it was already there (when Reservoir is next updated).
**Layout:**
These options control the top-level directory layout of the package and its build directory. Further paths specified by libraries, executables, and targets within the package are relative to these directories. 

`srcDir`
    
**Contains:** Path
The directory containing the package's Lean source files. Defaults to the package's directory.
(This will be passed to `lean` as the `-R` option.) 

`buildDir`
    
**Contains:** Path
The directory to which Lake should output the package's build results. Defaults to `defaultBuildDir` (i.e., `.lake/build`). 

`nativeLibDir`
    
**Contains:** Path
The build subdirectory to which Lake should output the package's native libraries (e.g., `.a`, `.so`, `.dll` files). Defaults to `defaultNativeLibDir` (i.e., `lib`). 

`binDir`
    
**Contains:** Path
The build subdirectory to which Lake should output the package's binary executable. Defaults to `defaultBinDir` (i.e., `bin`). 

`irDir`
    
**Contains:** Path
The build subdirectory to which Lake should output the package's intermediary results (e.g., `.c` and `.o` files). Defaults to `defaultIrDir` (i.e., `ir`). 

`packagesDir`
    
**Contains:** Path
The directory to which Lake should download remote dependencies. Defaults to `defaultPackagesDir` (i.e., `.lake/packages`).
**Building and Running:**
These options configure how code is built and run in the package. Libraries, executables, and other [targets](Build-Tools-and-Distribution/Lake/#--tech-term-target) within a package can further add to parts of this configuration. 

`extraDepTargets`
    
**Contains:** Array of strings
An `Array` of target names to build whenever the package is used. 

`precompileModules`
    
**Contains:** Boolean
Whether to compile each of the package's module into a native shared library that is loaded whenever the module is imported. This speeds up evaluation of metaprograms and enables the interpreter to run functions marked `@[extern]`.
Defaults to `false`. 

`defaultTargets`
    
**Contains:** default targets' names (array)
The names of the package's targets to build by default (i.e., on a bare `lake build` of the package). 

`moreGlobalServerArgs`
    
**Contains:** Array of strings
Additional arguments to pass to the Lean language server (i.e., `lean --server`) launched by `lake serve`, both for this package and also for any packages browsed from this one in the same session. 

`leanLibDir`
    
**Contains:** Path
The build subdirectory to which Lake should output the package's binary Lean libraries (e.g., `.olean`, `.ilean` files). Defaults to `defaultLeanLibDir` (i.e., `lib`). 

`buildType`
    
**Contains:** one of `"debug"`, `"relWithDebInfo"`, `"minSizeRel"`, `"release"`
The mode in which the modules should be built (e.g., `debug`, `release`). Defaults to `release`. 

`leanOptions`
    
**Contains:** Array of Lean options
An `Array` of additional options to pass to both the Lean language server (i.e., `lean --server`) launched by `lake serve` and to `lean` when compiling a module's Lean source files. 

`moreLeanArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `lean` when compiling a module's Lean source files. 

`weakLeanArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `lean` when compiling a module's Lean source files.
Unlike `moreLeanArgs`, these arguments do not affect the trace of the build result, so they can be changed without triggering a rebuild. They come _before_ `moreLeanArgs`. 

`moreLeancArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when compiling a module's C source files generated by `lean`.
Lake already passes some flags based on the `buildType`, but you can change this by, for example, adding `-O0` and `-UNDEBUG`. 

`moreServerOptions`
    
**Contains:** Array of Lean options
Additional options to pass to the Lean language server (i.e., `lean --server`) launched by `lake serve`. 

`weakLeancArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when compiling a module's C source files generated by `lean`.
Unlike `moreLeancArgs`, these arguments do not affect the trace of the build result, so they can be changed without triggering a rebuild. They come _before_ `moreLeancArgs`. 

`moreLinkArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when linking (e.g., for shared libraries or binary executables). These will come _after_ the paths of the linked objects. 

`weakLinkArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when linking (e.g., for shared libraries or binary executables). These will come _after_ the paths of the linked objects.
Unlike `moreLinkArgs`, these arguments do not affect the trace of the build result, so they can be changed without triggering a rebuild. They come _before_ `moreLinkArgs`. 

`platformIndependent`
    
**Contains:** Boolean (optional)
Asserts whether Lake should assume Lean modules are platform-independent.
  * If `false`, Lake will add `System.Platform.target` to the module traces within the code unit (e.g., package or library). This will force Lean code to be re-elaborated on different platforms.
  * If `true`, Lake will exclude platform-dependent elements (e.g., precompiled modules, external libraries) from a module's trace, preventing re-elaboration on different platforms. Note that this will not effect modules outside the code unit in question. For example, a platform-independent package which depends on a platform-dependent library will still be platform-dependent.
  * If `none`, Lake will construct traces as natural. That is, it will include platform-dependent artifacts in the trace if they module depends on them, but otherwise not force modules to be platform-dependent.


There is no check for correctness here, so a configuration can lie and Lake will not catch it. Defaults to `none`.
**Testing and Linting:**
The CLI commands [`lake test`](Build-Tools-and-Distribution/Lake/#test) and [`lake lint`](Build-Tools-and-Distribution/Lake/#lint) use definitions configured by the [workspace](Build-Tools-and-Distribution/Lake/#--tech-term-workspace)'s [root package](Build-Tools-and-Distribution/Lake/#--tech-term-root-package) to perform testing and linting. The code that is run to perform tests and linting is referred to as the test or lint driver. In Lean configuration files, these can be specified by applying the `@[test_driver]` or `@[lint_driver]` attributes to a [Lake script](Build-Tools-and-Distribution/Lake/#--tech-term-Lake-scripts) or an executable or library target. In both Lean and TOML configuration files, they can also be configured by setting these options. A target or script `TGT` from a dependency `PKG` can be specified as a test or lint driver using the string `"PKG/TGT"` 

`testDriver`
    
**Contains:** String
The name of the script, executable, or library by `lake test` when this package is the workspace root. To point to a definition in another package, use the syntax `<pkg>/<def>`.
A script driver will be run by `lake test` with the arguments configured in `testDriverArgs` followed by any specified on the CLI (e.g., via `lake lint -- <args>...`). An executable driver will be built and then run like a script. A library will just be built. 

`testDriverArgs`
    
**Contains:** Array of strings
Arguments to pass to the package's test driver. These arguments will come before those passed on the command line via `lake test -- <args>...`. 

`lintDriver`
    
**Contains:** String
The name of the script or executable used by `lake lint` when this package is the workspace root. To point to a definition in another package, use the syntax `<pkg>/<def>`.
A script driver will be run by `lake lint` with the arguments configured in `lintDriverArgs` followed by any specified on the CLI (e.g., via `lake lint -- <args>...`). An executable driver will be built and then run like a script. 

`lintDriverArgs`
    
**Contains:** Array of strings
Arguments to pass to the package's linter. These arguments will come before those passed on the command line via `lake lint -- <args>...`.
**Cloud Releases:**
These options define a cloud release for the package, as described in the section on [GitHub release builds](Build-Tools-and-Distribution/Lake/#lake-github). 

`releaseRepo`
    
**Contains:** String (optional)
The URL of the GitHub repository to upload and download releases of this package. If `none` (the default), for downloads, Lake uses the URL the package was download from (if it is a dependency) and for uploads, uses `gh`'s default. 

`buildArchive`
    
**Contains:** String (optional)
A custom name for the build archive for the GitHub cloud release. If `none` (the default), Lake defaults to `{(pkg-)name}-{System.Platform.target}.tar.gz`. 

`preferReleaseBuild`
    
**Contains:** Boolean
Whether to prefer downloading a prebuilt release (from GitHub) rather than building this package from the source when this package is used as a dependency.
**Other Fields:** 

`bootstrap`
    
**Contains:** Boolean
**For internal use.** Whether this package is Lean itself. 

`enableArtifactCache?`
    
**Contains:** Boolean (optional)
Whether to enables Lake's local, offline artifact cache for the package.
Artifacts (i.e., build products) of packages will be shared across local copies by storing them in a cache associated with the Lean toolchain. This can significantly reduce initial build times and disk space usage when working with multiple copies of large projects or large dependencies.
As a caveat, build targets which support the artifact cache will not be stored in their usual location within the build directory. Thus, projects with custom build scripts that rely on specific location of artifacts may wish to disable this feature.
If `none` (the default), this will fallback to (in order):
  * The `LAKE_ARTIFACT_CACHE` environment variable (if set).
  * The workspace root's `enableArtifactCache` configuration (if set and this package is a dependency).
  * **Lake's default** : The package can use artifacts from the cache, but cannot write to it.



`restoreAllArtifacts`
    
**Contains:** Boolean
Whether, when the local artifact cache is enabled, Lake should copy all cached artifacts into the build directory. This ensures the build results are available to external consumers who expect them in the build directory.
Defaults to `false`. 

`libPrefixOnWindows`
    
**Contains:** Boolean
Whether native libraries (of this package) should be prefixed with `lib` on Windows.
Unlike Unix, Windows does not require native libraries to start with `lib` and, by convention, they usually do not. However, for consistent naming across all platforms, users may wish to enable this.
Defaults to `false`. 

`allowImportAll`
    
**Contains:** Boolean
Whether downstream packages can `import all` modules of this package.
If enabled, downstream users will be able to access the `private` internals of modules, including definition bodies not marked as `@[expose]`. This may also, in the future, prevent compiler optimization which rely on `private` definitions being inaccessible outside their own package.
Defaults to `false`. 

`moreLinkObjs`
    
**Contains:** Array of paths
Additional target objects to use when linking (both static and shared). These will come _after_ the paths of native facets. 

`moreLinkLibs`
    
**Contains:** Array of dynamic libraries
Additional target libraries to pass to `leanc` when linking (e.g., for shared libraries or binary executables). These will come _after_ the paths of other link objects.
Minimal TOML Package Configuration
The minimal TOML configuration for a Lean [package](Build-Tools-and-Distribution/Lake/#--tech-term-package) sets only the package's name, using the default values for all other fields. This package contains no [targets](Build-Tools-and-Distribution/Lake/#--tech-term-target), so there is no code to be built.

```
name = "example-package"

```

Library TOML Package Configuration
The minimal TOML configuration for a Lean [package](Build-Tools-and-Distribution/Lake/#--tech-term-package) sets the package's name and defines a library target. This library is named `Sorting`, and its modules are expected under the `Sorting.*` hierarchy.

```
name = "example-package"
defaultTargets = ["Sorting"]

[[[lean_lib](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig)]]
[name](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig-name) = "Sorting"

```

####  24.1.3.1.2. Dependencies[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Declarative-TOML-Format--Dependencies "Permalink")
Dependencies are specified in the `[[[require](Build-Tools-and-Distribution/Lake/#Lake___Dependency)]]` field array of a package configuration, which specifies both the name and the source of each package. There are three kinds of sources:
  * [Reservoir](https://reservoir.lean-lang.org/), or an alternative package registry
  * Git repositories, which may be local paths or URLs
  * Local paths


TOML table
```
Requiring Packages — [[require]]
```

A `Dependency` of a package. It specifies a package which another package depends on. This encodes the information contained in the `require` DSL syntax.
The `path[](Build-Tools-and-Distribution/Lake/#Lake___Dependency-path)` and `git[](Build-Tools-and-Distribution/Lake/#Lake___Dependency-git)` fields specify an explicit source for a dependency. If neither are provided, then the dependency is fetched from [Reservoir](https://reservoir.lean-lang.org/), or an alternative registry if one has been configured. The `scope[](Build-Tools-and-Distribution/Lake/#Lake___Dependency-scope)` field is required when fetching a package from Reservoir.
**Fields:** 

`path`
    
**Contains:** Path
A dependency on the local filesystem, specified by its path. 

`git`
    
**Contains:** Git specification
A dependency in a Git repository, specified either by its URL as a string or by a table with the keys:
  * `url`: the repository URL
  * `subDir`: the subdirectory of the Git repository that contains the package's source code



`rev`
    
**Contains:** Git revision
For Git or Reservoir dependencies, this field specifies the Git revision, which may be a branch name, a tag name, or a specific hash. On Reservoir, the `version` field takes precedence over this field. 

`source`
    
**Contains:** Package Source
A dependency source, specified as a self-contained table, which is used when neither the `git` nor the `path` key is present. The key `type` should be either the string `"git"` or the string `"path"`. If the type is `"path"`, then there must be a further key `"path"` whose value is a string that provides the location of the package on disk. If the type is `"git"`, then the following keys should be present:
  * `url`: the repository URL
  * `rev`: the Git revision, which may be a branch name, a tag name, or a specific hash (optional)
  * `subDir`: the subdirectory of the Git repository that contains the package's source code



`version`
    
**Contains:** version as string
The target version of the dependency. A Git revision can be specified with the syntax `git#<rev>`. 

`name`
    
**Contains:** String
The package name of the dependency. This name must match the one declared in its configuration file, as that name is used to index its target data types. For this reason, the package name must also be unique across packages in the dependency graph. 

`scope`
    
**Contains:** String
An additional qualifier used to distinguish packages of the same name in a Lake registry. On Reservoir, this is the package owner.
Requiring Packages from Reservoir
The package `example` can be required from Reservoir using this TOML configuration:

```
[[[require](Build-Tools-and-Distribution/Lake/#Lake___Dependency)]]
[name](Build-Tools-and-Distribution/Lake/#Lake___Dependency-name) = "example"
[version](Build-Tools-and-Distribution/Lake/#Lake___Dependency-version) = "2.12"
[scope](Build-Tools-and-Distribution/Lake/#Lake___Dependency-scope) = "exampleDev"

```

Requiring Packages from Git
The package `example` can be required from a Git repository using this TOML configuration:

```
[[[require](Build-Tools-and-Distribution/Lake/#Lake___Dependency)]]
[name](Build-Tools-and-Distribution/Lake/#Lake___Dependency-name) = "example"
[git](Build-Tools-and-Distribution/Lake/#Lake___Dependency-git) = "https://git.example.com/example.git"
[rev](Build-Tools-and-Distribution/Lake/#Lake___Dependency-rev) = "main"
[version](Build-Tools-and-Distribution/Lake/#Lake___Dependency-version) = "2.12"

```

In particular, the package will be checked out from the `main` branch, and the version number specified in the package's [configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) should match `2.12`.
Requiring Packages from a Git tag
The package `example` can be required from the tag `v2.12` in a Git repository using this TOML configuration:

```
[[[require](Build-Tools-and-Distribution/Lake/#Lake___Dependency)]]
[name](Build-Tools-and-Distribution/Lake/#Lake___Dependency-name) = "example"
[git](Build-Tools-and-Distribution/Lake/#Lake___Dependency-git) = "https://git.example.com/example.git"
[rev](Build-Tools-and-Distribution/Lake/#Lake___Dependency-rev) = "v2.12"

```

The version number specified in the package's [configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) is not used.
Requiring Reservoir Packages from a Git tag
The package `example`, found using Reservoir, can be required from the tag `v2.12` in its Git repository using this TOML configuration:

```
[[[require](Build-Tools-and-Distribution/Lake/#Lake___Dependency)]]
[name](Build-Tools-and-Distribution/Lake/#Lake___Dependency-name) = "example"
[rev](Build-Tools-and-Distribution/Lake/#Lake___Dependency-rev) = "v2.12"
[scope](Build-Tools-and-Distribution/Lake/#Lake___Dependency-scope) = "exampleDev"

```

The version number specified in the package's [configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) is not used.
Requiring Packages from Paths
The package `example` can be required from the local path `../example` using this TOML configuration:

```
[[[require](Build-Tools-and-Distribution/Lake/#Lake___Dependency)]]
[name](Build-Tools-and-Distribution/Lake/#Lake___Dependency-name) = "example"
[path](Build-Tools-and-Distribution/Lake/#Lake___Dependency-path) = "../example"

```

Dependencies on local paths are useful when developing multiple packages in a single repository, or when testing whether a change to a dependency fixes a bug in a downstream package.
Sources as Tables
The information about the package source can be written in an explicit table.

```
[[[require](Build-Tools-and-Distribution/Lake/#Lake___Dependency)]]
[name](Build-Tools-and-Distribution/Lake/#Lake___Dependency-name) = "example"
[source](Build-Tools-and-Distribution/Lake/#Lake___Dependency-source) = {type = "git", url = "https://example.com/example.git"}

```

####  24.1.3.1.3. Library Targets[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Declarative-TOML-Format--Library-Targets "Permalink")
Library targets are expected in the `lean_lib` array of tables.
TOML table
```
Library Targets — [[lean_lib]]
```

A Lean library's declarative configuration.
**Fields:** 

`name`
    
**Contains:** The library name
The library's name, which is typically the same as its single module root. 

`srcDir`
    
**Contains:** Path
The subdirectory of the package's source directory containing the library's Lean source files. Defaults simply to said `srcDir`.
(This will be passed to `lean` as the `-R` option.) 

`roots`
    
**Contains:** Array of strings
The root module(s) of the library. Submodules of these roots (e.g., `Lib.Foo` of `Lib`) are considered part of the library. Defaults to a single root of the target's name. 

`libName`
    
**Contains:** String
The name of the library artifact. Used as a base for the file names of its static and dynamic binaries. Defaults to the mangled name of the target. 

`libPrefixOnWindows`
    
**Contains:** Boolean
Whether static and shared binaries of this library should be prefixed with `lib` on Windows.
Unlike Unix, Windows does not require native libraries to start with `lib` and, by convention, they usually do not. However, for consistent naming across all platforms, users may wish to enable this.
Defaults to `false`. 

`needs`
    
**Contains:** Array of targets
An `Array` of targets to build before the executable's modules. 

`extraDepTargets`
    
**Contains:** Array of strings
**Deprecated. Use`needs` instead.** An `Array` of target names to build before the library's modules. 

`precompileModules`
    
**Contains:** Boolean
Whether to compile each of the library's modules into a native shared library that is loaded whenever the module is imported. This speeds up evaluation of metaprograms and enables the interpreter to run functions marked `@[extern]`.
Defaults to `false`. 

`defaultFacets`
    
**Contains:** Array of strings
An `Array` of library facets to build on a bare `lake build` of the library. For example, `#[LeanLib.sharedFacet]` will build the shared library facet. 

`allowImportAll`
    
**Contains:** Boolean
Whether downstream packages can `import all` modules of this library.
If enabled, downstream users will be able to access the `private` internals of modules, including definition bodies not marked as `@[expose]`. This may also, in the future, prevent compiler optimization which rely on `private` definitions being inaccessible outside their own package.
Defaults to `false`. 

`buildType`
    
**Contains:** one of `"debug"`, `"relWithDebInfo"`, `"minSizeRel"`, `"release"`
The mode in which the modules should be built (e.g., `debug`, `release`). Defaults to `release`. 

`leanOptions`
    
**Contains:** Array of Lean options
An `Array` of additional options to pass to both the Lean language server (i.e., `lean --server`) launched by `lake serve` and to `lean` when compiling a module's Lean source files. 

`moreLeanArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `lean` when compiling a module's Lean source files. 

`weakLeanArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `lean` when compiling a module's Lean source files.
Unlike `moreLeanArgs`, these arguments do not affect the trace of the build result, so they can be changed without triggering a rebuild. They come _before_ `moreLeanArgs`. 

`moreLeancArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when compiling a module's C source files generated by `lean`.
Lake already passes some flags based on the `buildType`, but you can change this by, for example, adding `-O0` and `-UNDEBUG`. 

`moreServerOptions`
    
**Contains:** Array of Lean options
Additional options to pass to the Lean language server (i.e., `lean --server`) launched by `lake serve`. 

`weakLeancArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when compiling a module's C source files generated by `lean`.
Unlike `moreLeancArgs`, these arguments do not affect the trace of the build result, so they can be changed without triggering a rebuild. They come _before_ `moreLeancArgs`. 

`moreLinkObjs`
    
**Contains:** Array of paths
Additional target objects to use when linking (both static and shared). These will come _after_ the paths of native facets. 

`moreLinkLibs`
    
**Contains:** Array of dynamic libraries
Additional target libraries to pass to `leanc` when linking (e.g., for shared libraries or binary executables). These will come _after_ the paths of other link objects. 

`moreLinkArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when linking (e.g., for shared libraries or binary executables). These will come _after_ the paths of the linked objects. 

`weakLinkArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when linking (e.g., for shared libraries or binary executables). These will come _after_ the paths of the linked objects.
Unlike `moreLinkArgs`, these arguments do not affect the trace of the build result, so they can be changed without triggering a rebuild. They come _before_ `moreLinkArgs`. 

`platformIndependent`
    
**Contains:** Boolean (optional)
Asserts whether Lake should assume Lean modules are platform-independent.
  * If `false`, Lake will add `System.Platform.target` to the module traces within the code unit (e.g., package or library). This will force Lean code to be re-elaborated on different platforms.
  * If `true`, Lake will exclude platform-dependent elements (e.g., precompiled modules, external libraries) from a module's trace, preventing re-elaboration on different platforms. Note that this will not effect modules outside the code unit in question. For example, a platform-independent package which depends on a platform-dependent library will still be platform-dependent.
  * If `none`, Lake will construct traces as natural. That is, it will include platform-dependent artifacts in the trace if they module depends on them, but otherwise not force modules to be platform-dependent.


There is no check for correctness here, so a configuration can lie and Lake will not catch it. Defaults to `none`. 

`dynlibs`
    
**Contains:** Array of dynamic libraries 

`plugins`
    
**Contains:** Array of dynamic libraries
Minimal Library Target
This library declaration supplies only a name:

```
[[[lean_lib](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig)]]
[name](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig-name) = "TacticTools"

```

The library's source is located in the package's default source directory, in the module hierarchy rooted at `TacticTools`.
Configured Library Target
This library declaration supplies more options:

```
[[[lean_lib](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig)]]
[name](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig-name) = "TacticTools"
[srcDir](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig-srcDir) = "src"
[precompileModules](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig-precompileModules) = true
```

The library's source is located in the directory `src`, in the module hierarchy rooted at `TacticTools`. If its modules are accessed at elaboration time, they will be compiled to native code and linked in, rather than run in the interpreter.
####  24.1.3.1.4. Executable Targets[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Declarative-TOML-Format--Executable-Targets "Permalink")
TOML table
```
Executable Targets — [[lean_exe]]
```

A Lean executable's declarative configuration.
**Fields:** 

`name`
    
**Contains:** The executable's name
The executable's name. 

`srcDir`
    
**Contains:** Path
The subdirectory of the package's source directory containing the executable's Lean source file. Defaults simply to said `srcDir`.
(This will be passed to `lean` as the `-R` option.) 

`root`
    
**Contains:** String
The root module of the binary executable. Should include a `main` definition that will serve as the entry point of the program.
The root is built by recursively building its local imports (i.e., fellow modules of the workspace).
Defaults to the name of the target. 

`exeName`
    
**Contains:** String
The name of the binary executable. Defaults to the target name with any `.` replaced with a `-`. 

`needs`
    
**Contains:** Array of targets
An `Array` of targets to build before the executable's modules. 

`extraDepTargets`
    
**Contains:** Array of strings
**Deprecated. Use`needs` instead.** An `Array` of target names to build before the executable's modules. 

`supportInterpreter`
    
**Contains:** Boolean
Enables the executable to interpret Lean files (e.g., via `Lean.Elab.runFrontend`) by exposing symbols within the executable to the Lean interpreter.
Implementation-wise, on Windows, the Lean shared libraries are linked to the executable and, on other systems, the executable is linked with `-rdynamic`. This increases the size of the binary on Linux and, on Windows, requires `libInit_shared.dll` and `libleanshared.dll` to be co-located with the executable or part of `PATH` (e.g., via `lake exe`). Thus, this feature should only be enabled when necessary.
Defaults to `false`. 

`buildType`
    
**Contains:** one of `"debug"`, `"relWithDebInfo"`, `"minSizeRel"`, `"release"`
The mode in which the modules should be built (e.g., `debug`, `release`). Defaults to `release`. 

`leanOptions`
    
**Contains:** Array of Lean options
An `Array` of additional options to pass to both the Lean language server (i.e., `lean --server`) launched by `lake serve` and to `lean` when compiling a module's Lean source files. 

`moreLeanArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `lean` when compiling a module's Lean source files. 

`weakLeanArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `lean` when compiling a module's Lean source files.
Unlike `moreLeanArgs`, these arguments do not affect the trace of the build result, so they can be changed without triggering a rebuild. They come _before_ `moreLeanArgs`. 

`moreLeancArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when compiling a module's C source files generated by `lean`.
Lake already passes some flags based on the `buildType`, but you can change this by, for example, adding `-O0` and `-UNDEBUG`. 

`moreServerOptions`
    
**Contains:** Array of Lean options
Additional options to pass to the Lean language server (i.e., `lean --server`) launched by `lake serve`. 

`weakLeancArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when compiling a module's C source files generated by `lean`.
Unlike `moreLeancArgs`, these arguments do not affect the trace of the build result, so they can be changed without triggering a rebuild. They come _before_ `moreLeancArgs`. 

`moreLinkObjs`
    
**Contains:** Array of paths
Additional target objects to use when linking (both static and shared). These will come _after_ the paths of native facets. 

`moreLinkLibs`
    
**Contains:** Array of dynamic libraries
Additional target libraries to pass to `leanc` when linking (e.g., for shared libraries or binary executables). These will come _after_ the paths of other link objects. 

`moreLinkArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when linking (e.g., for shared libraries or binary executables). These will come _after_ the paths of the linked objects. 

`weakLinkArgs`
    
**Contains:** Array of strings
Additional arguments to pass to `leanc` when linking (e.g., for shared libraries or binary executables). These will come _after_ the paths of the linked objects.
Unlike `moreLinkArgs`, these arguments do not affect the trace of the build result, so they can be changed without triggering a rebuild. They come _before_ `moreLinkArgs`. 

`platformIndependent`
    
**Contains:** Boolean (optional)
Asserts whether Lake should assume Lean modules are platform-independent.
  * If `false`, Lake will add `System.Platform.target` to the module traces within the code unit (e.g., package or library). This will force Lean code to be re-elaborated on different platforms.
  * If `true`, Lake will exclude platform-dependent elements (e.g., precompiled modules, external libraries) from a module's trace, preventing re-elaboration on different platforms. Note that this will not effect modules outside the code unit in question. For example, a platform-independent package which depends on a platform-dependent library will still be platform-dependent.
  * If `none`, Lake will construct traces as natural. That is, it will include platform-dependent artifacts in the trace if they module depends on them, but otherwise not force modules to be platform-dependent.


There is no check for correctness here, so a configuration can lie and Lake will not catch it. Defaults to `none`. 

`dynlibs`
    
**Contains:** Array of dynamic libraries 

`plugins`
    
**Contains:** Array of dynamic libraries
Minimal Executable Target
This executable declaration supplies only a name:

```
[[[lean_exe](Build-Tools-and-Distribution/Lake/#Lake___LeanExeConfig)]]
[name](Build-Tools-and-Distribution/Lake/#Lake___LeanExeConfig-name) = "trustworthytool"

```

The executable's `main` function is expected in a module named `trustworthytool.lean` in the package's default source file path. The resulting executable is named `trustworthytool`.
[Live ↪](javascript:openLiveLink\("CYUwZgBAtghglgOwgLggGTgZwC4QMrYBOiA5hIEmEEAkgPIQCqVC2AzAEwoC8EYArkgH0InAHwQADr0IgIABiA"\))
Configured Executable Target
The name `trustworthy-tool` is not a valid Lean name due to the dash (`-`). To use this name for an executable target, an explicit module root must be supplied. Even though `trustworthy-tool` is a perfectly acceptable name for an executable, the target also specifies that the result of compilation and linking should be named `tt`.

```
[[[lean_exe](Build-Tools-and-Distribution/Lake/#Lake___LeanExeConfig)]]
[name](Build-Tools-and-Distribution/Lake/#Lake___LeanExeConfig-name) = "trustworthy-tool"
[root](Build-Tools-and-Distribution/Lake/#Lake___LeanExeConfig-root) = "TrustworthyTool"
[exeName](Build-Tools-and-Distribution/Lake/#Lake___LeanExeConfig-exeName) = "tt"

```

The executable's `main` function is expected in a module named `TrustworthyTool.lean` in the package's default source file path.
[Live ↪](javascript:openLiveLink\("CYUwZgBAtghglgOwgLggGTgZwC4QMrYBOiA5hIEmEEAkgPIQCqVC2AzAEwoC8EYArkgH0InAHwQADr0IgIABiA"\))
###  24.1.3.2. Lean Format[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-config-lean "Permalink")
The Lean format for Lake [package configuration](Build-Tools-and-Distribution/Lake/#--tech-term-package-configuration) files provides a domain-specific language for the declarative features that are supported in the TOML format. Additionally, it provides the ability to write Lean code to implement any necessary build logic that is not expressible declaratively. The Lean configuration file is named `lakefile.lean`.
Because the Lean format is a Lean source file, it can be edited using all the features of the Lean language server. Additionally, Lean's metaprogramming framework allows elaboration-time side effects to be used to implement features such as configuration steps that are conditional on the current platform. However, a consequence of the Lean configuration format being a Lean file is that it is not feasible to process such files using tools that are not themselves written in Lean.
####  24.1.3.2.1. Declarative Fields[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Declarative-Fields "Permalink")
The declarative subset of the Lean configuration format uses sequences of declaration fields to specify configuration options.
syntaxDeclarative Fields
A field assignment in a declarative configuration.

```
[
A field assignment in a declarative configuration. 
declField](Build-Tools-and-Distribution/Lake/#Lake___DSL___declField-next) ::=
    


A field assignment in a declarative configuration. 


ident := term
```

####  24.1.3.2.2. Packages[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Packages "Permalink")
syntaxPackage Configuration

```
command ::= ...
    | 


Defines the configuration of a Lake package.  Has many forms:


```
package «pkg-name»
package «pkg-name» { /- config opts -/ }
package «pkg-name» where /- config opts -/

```

There can only be one `package` declaration per Lake configuration file. The defined package configuration will be available for reference as `_package`.
`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? ([@[](Attributes/#Lean___Parser___Term___attributes-next) [attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next),* []](Attributes/#Lean___Parser___Term___attributes-next))? package identOrStr
```

```
command ::= ...
    | 


Defines the configuration of a Lake package.  Has many forms:


```
package «pkg-name»
package «pkg-name» { /- config opts -/ }
package «pkg-name» where /- config opts -/

```

There can only be one `package` declaration per Lake configuration file. The defined package configuration will be available for reference as `_package`.
`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? ([@[](Attributes/#Lean___Parser___Term___attributes-next)[attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next),*[]](Attributes/#Lean___Parser___Term___attributes-next))? package identOrStr where [` A field assignment in a declarative configuration.  `declField](Build-Tools-and-Distribution/Lake/#Lake___DSL___declField-next)*
```

```
command ::= ...
    | 


Defines the configuration of a Lake package.  Has many forms:


```
package «pkg-name»
package «pkg-name» { /- config opts -/ }
package «pkg-name» where /- config opts -/

```

There can only be one `package` declaration per Lake configuration file. The defined package configuration will be available for reference as `_package`.
`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? ([@[](Attributes/#Lean___Parser___Term___attributes-next)[attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next),*[]](Attributes/#Lean___Parser___Term___attributes-next))? package identOrStr { [` A field assignment in a declarative configuration.  `declField](Build-Tools-and-Distribution/Lake/#Lake___DSL___declField-next);* } (where `
 
`letRecDecl` matches the body of a let-rec declaration: a doc comment, attributes, and then a let declaration without the `let` keyword, such as `/-- foo -/ @[simp] bar := 1`. 
`letRecDecl;*)?
```

There can only be one ``Lake.DSL.packageCommand : command`
Defines the configuration of a Lake package. Has many forms:

```
package «pkg-name»
package «pkg-name» { /- config opts -/ }
package «pkg-name» where /- config opts -/

```

There can only be one `package` declaration per Lake configuration file. The defined package configuration will be available for reference as `_package`.
``package` declaration per Lake configuration file. The defined package configuration will be available for reference as `_package`.
syntaxPost-Update Hooks

```
command ::= ...
    | 


Declare a post-lake update hook for the package.
Runs the monadic action is after a successful lake update execution
in this package or one of its downstream dependents.


**Example**


This feature enables Mathlib to synchronize the Lean toolchain and run
cache get after a lake update:


```
lean_exe cache
post_update pkg do
  let wsToolchainFile := (← getRootPackage).dir / "lean-toolchain"
  let mathlibToolchain ← IO.FS.readFile <| pkg.dir / "lean-toolchain"
  IO.FS.writeFile wsToolchainFile mathlibToolchain
  let exeFile ← runBuild cache.fetch
  let exitCode ← env exeFile.toString #["get"]
  if exitCode ≠ 0 then
    error s!"{pkg.name}: failed to fetch cache"

```

` post_update simpleBinder? (declValSimple | declValDo)
```

Declare a post-`lake update` hook for the package. Runs the monadic action is after a successful `lake update` execution in this package or one of its downstream dependents.
**Example**
This feature enables Mathlib to synchronize the Lean toolchain and run `cache get` after a `lake update`:

```
lean_exe cache
post_update pkg do
  let wsToolchainFile := (← getRootPackage).dir / "lean-toolchain"
  let mathlibToolchain ← IO.FS.readFile <| pkg.dir / "lean-toolchain"
  IO.FS.writeFile wsToolchainFile mathlibToolchain
  let exeFile ← runBuild cache.fetch
  let exitCode ← env exeFile.toString #["get"]
  if exitCode ≠ 0 then
    error s!"{pkg.name}: failed to fetch cache"

```

####  24.1.3.2.3. Dependencies[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Dependencies "Permalink")
Dependencies are specified using the ``Lake.DSL.requireDecl : command`
Adds a new package dependency to the workspace. The general syntax is:

```
require ["<scope>" /] <pkg-name> [@ <version>]
  [from <source>] [with <options>]

```

The `from` clause tells Lake where to locate the dependency. See the `fromClause` syntax documentation (e.g., hover over it) to see the different forms this clause can take.
Without a `from` clause, Lake will lookup the package in the default registry (i.e., Reservoir) and use the information there to download the package at the requested `version`. The `scope` is used to disambiguate between packages in the registry with the same `pkg-name`. In Reservoir, this scope is the package owner (e.g., `leanprover` of `@leanprover/doc-gen4`).
The `with` clause specifies a `NameMap String` of Lake options used to configure the dependency. This is equivalent to passing `-K` options to the dependency on the command line.
`[`require`](Build-Tools-and-Distribution/Lake/#Lake___DSL___requireDecl) declaration.
syntaxRequiring Packages

```
command ::= ...
    | 


Adds a new package dependency to the workspace. The general syntax is:


```
require ["<scope>" /] <pkg-name> [@ <version>]
  [from <source>] [with <options>]

```

The `from` clause tells Lake where to locate the dependency. See the `fromClause` syntax documentation (e.g., hover over it) to see the different forms this clause can take.
Without a `from` clause, Lake will lookup the package in the default registry (i.e., Reservoir) and use the information there to download the package at the requested `version`. The `scope` is used to disambiguate between packages in the registry with the same `pkg-name`. In Reservoir, this scope is the package owner (e.g., `leanprover` of `@leanprover/doc-gen4`).
The `with` clause specifies a `NameMap String` of Lake options used to configure the dependency. This is equivalent to passing `-K` options to the dependency on the command line.
`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment) require depName (`
 
The version of the package to require. To specify a Git revision, use the syntax `@ git <rev>`.
`@ git? term)? `
 
Specifies a specific source from which to draw the package dependency. Dependencies that are downloaded from a remote source will be placed into the workspace's `packagesDir`.
**Path Dependencies**

```
from <path>

```

Lake loads the package located at a fixed `path` relative to the requiring package's directory.
**Git Dependencies**

```
from git <url> [@ <rev>] [/ <subDir>]

```

Lake clones the Git repository available at the specified fixed Git `url`, and checks out the specified revision `rev`. The revision can be a commit hash, branch, or tag. If none is provided, Lake defaults to `master`. After checkout, Lake loads the package located in `subDir` (or the repository root if no subdirectory is specified).
`fromClause? (with term)?
```

The `@` clause specifies a package version, which is used when requiring a package from [Reservoir](https://reservoir.lean-lang.org/). The version may either be a string that specifies the version declared in the package's `version` field, or a specific Git revision. Git revisions may be branch names, tag names, or commit hashes.
The optional ``
 
Specifies a specific source from which to draw the package dependency. Dependencies that are downloaded from a remote source will be placed into the workspace's `packagesDir`.
**Path Dependencies**

```
from <path>

```

Lake loads the package located at a fixed `path` relative to the requiring package's directory.
**Git Dependencies**

```
from git <url> [@ <rev>] [/ <subDir>]

```

Lake clones the Git repository available at the specified fixed Git `url`, and checks out the specified revision `rev`. The revision can be a commit hash, branch, or tag. If none is provided, Lake defaults to `master`. After checkout, Lake loads the package located in `subDir` (or the repository root if no subdirectory is specified).
`fromClause` specifies a package source other than Reservoir, which may be either a Git repository or a local path.
The ``Lake.DSL.requireDecl : command`
Adds a new package dependency to the workspace. The general syntax is:

```
require ["<scope>" /] <pkg-name> [@ <version>]
  [from <source>] [with <options>]

```

The `from` clause tells Lake where to locate the dependency. See the `fromClause` syntax documentation (e.g., hover over it) to see the different forms this clause can take.
Without a `from` clause, Lake will lookup the package in the default registry (i.e., Reservoir) and use the information there to download the package at the requested `version`. The `scope` is used to disambiguate between packages in the registry with the same `pkg-name`. In Reservoir, this scope is the package owner (e.g., `leanprover` of `@leanprover/doc-gen4`).
The `with` clause specifies a `NameMap String` of Lake options used to configure the dependency. This is equivalent to passing `-K` options to the dependency on the command line.
`[`with`](Build-Tools-and-Distribution/Lake/#Lake___DSL___requireDecl) clause specifies a `NameMap [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` of Lake options that will be used to configure the dependency. This is equivalent to passing `-K` options to [`lake build`](Build-Tools-and-Distribution/Lake/#build) when building the dependency on the command line.
syntaxPackage Sources
Specifies a specific source from which to draw the package dependency. Dependencies that are downloaded from a remote source will be placed into the workspace's `packagesDir`.
**Path Dependencies**

```
from <path>

```

Lake loads the package located at a fixed `path` relative to the requiring package's directory.
**Git Dependencies**

```
from git <url> [@ <rev>] [/ <subDir>]

```

Lake clones the Git repository available at the specified fixed Git `url`, and checks out the specified revision `rev`. The revision can be a commit hash, branch, or tag. If none is provided, Lake defaults to `master`. After checkout, Lake loads the package located in `subDir` (or the repository root if no subdirectory is specified).

```
fromClause ::=
    


Specifies a specific source from which to draw the package dependency.
Dependencies that are downloaded from a remote source will be placed
into the workspace's packagesDir.


**Path Dependencies**


```
from <path>

```

Lake loads the package located at a fixed `path` relative to the requiring package's directory.
**Git Dependencies**

```
from git <url> [@ <rev>] [/ <subDir>]

```

Lake clones the Git repository available at the specified fixed Git `url`, and checks out the specified revision `rev`. The revision can be a commit hash, branch, or tag. If none is provided, Lake defaults to `master`. After checkout, Lake loads the package located in `subDir` (or the repository root if no subdirectory is specified).
`from term
```

```
fromClause ::= ...
    | 


Specifies a specific source from which to draw the package dependency.
Dependencies that are downloaded from a remote source will be placed
into the workspace's packagesDir.


**Path Dependencies**


```
from <path>

```

Lake loads the package located at a fixed `path` relative to the requiring package's directory.
**Git Dependencies**

```
from git <url> [@ <rev>] [/ <subDir>]

```

Lake clones the Git repository available at the specified fixed Git `url`, and checks out the specified revision `rev`. The revision can be a commit hash, branch, or tag. If none is provided, Lake defaults to `master`. After checkout, Lake loads the package located in `subDir` (or the repository root if no subdirectory is specified).
`from git term (@ term)? (/ term)?
```

####  24.1.3.2.4. Targets[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Targets "Permalink")
[Targets](Build-Tools-and-Distribution/Lake/#--tech-term-target) are typically added to the set of default targets by applying the `default_target` attribute, rather than by explicitly listing them.
attributeSpecifying Default Targets

```
attr ::= ...
    | default_target
```

Marks a target as a default, to be built when no other target is specified.
#####  24.1.3.2.4.1. Libraries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Targets--Libraries "Permalink")
syntaxLibrary Targets
To define a library in which all configurable fields have their default values, use ``Lake.DSL.leanLibCommand : command`
Define a new Lean library target for the package. Can optionally be provided with a configuration of type `LeanLibConfig`. Has many forms:

```
lean_lib «target-name»
lean_lib «target-name» { /- config opts -/ }
lean_lib «target-name» where /- config opts -/

```

``lean_lib` with no further fields.

```
command ::= ...
    | 


Define a new Lean library target for the package.
Can optionally be provided with a configuration of type LeanLibConfig.
Has many forms:


```
lean_lib «target-name»
lean_lib «target-name» { /- config opts -/ }
lean_lib «target-name» where /- config opts -/

```

`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? [attributes](Attributes/#Lean___Parser___Term___attributes-next)? lean_lib identOrStr
```

The default configuration can be modified by providing the new values.

```
command ::= ...
    | 


Define a new Lean library target for the package.
Can optionally be provided with a configuration of type LeanLibConfig.
Has many forms:


```
lean_lib «target-name»
lean_lib «target-name» { /- config opts -/ }
lean_lib «target-name» where /- config opts -/

```

`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? [attributes](Attributes/#Lean___Parser___Term___attributes-next)? lean_lib identOrStr where [` A field assignment in a declarative configuration.  `declField](Build-Tools-and-Distribution/Lake/#Lake___DSL___declField-next)*
```

```
command ::= ...
    | 


Define a new Lean library target for the package.
Can optionally be provided with a configuration of type LeanLibConfig.
Has many forms:


```
lean_lib «target-name»
lean_lib «target-name» { /- config opts -/ }
lean_lib «target-name» where /- config opts -/

```

`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? [attributes](Attributes/#Lean___Parser___Term___attributes-next)? lean_lib identOrStr { [` A field assignment in a declarative configuration.  `declField](Build-Tools-and-Distribution/Lake/#Lake___DSL___declField-next);* } (where `
 
`letRecDecl` matches the body of a let-rec declaration: a doc comment, attributes, and then a let declaration without the `let` keyword, such as `/-- foo -/ @[simp] bar := 1`. 
`letRecDecl;*)?
```

The fields of ``Lake.DSL.leanLibCommand : command`
Define a new Lean library target for the package. Can optionally be provided with a configuration of type `LeanLibConfig`. Has many forms:

```
lean_lib «target-name»
lean_lib «target-name» { /- config opts -/ }
lean_lib «target-name» where /- config opts -/

```

``lean_lib` are those of the `[LeanLibConfig](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig___mk "Documentation for Lake.LeanLibConfig")` structure.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.LeanLibConfig.mk "Permalink")structure
```


Lake.LeanLibConfig (name : Lean.Name) : Type


Lake.LeanLibConfig (name : Lean.Name) :
  Type


```

A Lean library's declarative configuration.
#  Constructor

```
[Lake.LeanLibConfig.mk](Build-Tools-and-Distribution/Lake/#Lake___LeanLibConfig___mk "Documentation for Lake.LeanLibConfig.mk")
```

#  Extends
  * `Lake.LeanConfig`


#  Fields

```
buildType : [Lake.BuildType](Build-Tools-and-Distribution/Lake/#Lake___BuildType___debug "Documentation for Lake.BuildType")
```

Inherited from 
  1. `Lake.LeanConfig`



```
leanOptions : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.LeanOption](Build-Tools-and-Distribution/Lake/#Lean___LeanOption___mk "Documentation for Lean.LeanOption")
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreLeanArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
weakLeanArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreLeancArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreServerOptions : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.LeanOption](Build-Tools-and-Distribution/Lake/#Lean___LeanOption___mk "Documentation for Lean.LeanOption")
```

Inherited from 
  1. `Lake.LeanConfig`



```
weakLeancArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreLinkObjs : Lake.TargetArray [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreLinkLibs : Lake.TargetArray Lake.Dynlib
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreLinkArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
weakLinkArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
backend : [Lake.Backend](Build-Tools-and-Distribution/Lake/#Lake___Backend___c "Documentation for Lake.Backend")
```

Inherited from 
  1. `Lake.LeanConfig`



```
platformIndependent : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Inherited from 
  1. `Lake.LeanConfig`



```
dynlibs : Lake.TargetArray Lake.Dynlib
```

Inherited from 
  1. `Lake.LeanConfig`



```
plugins : Lake.TargetArray Lake.Dynlib
```

Inherited from 
  1. `Lake.LeanConfig`



```
srcDir : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")
```

The subdirectory of the package's source directory containing the library's Lean source files. Defaults simply to said `srcDir`.
(This will be passed to `lean` as the `-R` option.)

```
roots : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") Lean.Name
```

The root module(s) of the library. Submodules of these roots (e.g., `Lib.Foo` of `Lib`) are considered part of the library. Defaults to a single root of the target's name.

```
globs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lake.Glob](Build-Tools-and-Distribution/Lake/#Lake___Glob___one "Documentation for Lake.Glob")
```

An `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` of module `Glob`s to build for the library. Defaults to a `Glob.one` of each of the library's `roots`.
Submodule globs build every source file within their directory. Local imports of glob'ed files (i.e., fellow modules of the workspace) are also recursively built.

```
libName : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

The name of the library artifact. Used as a base for the file names of its static and dynamic binaries. Defaults to the mangled name of the target.

```
libPrefixOnWindows : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Whether static and shared binaries of this library should be prefixed with `lib` on Windows.
Unlike Unix, Windows does not require native libraries to start with `lib` and, by convention, they usually do not. However, for consistent naming across all platforms, users may wish to enable this.
Defaults to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.

```
needs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") Lake.PartialBuildKey
```

An `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` of targets to build before the executable's modules.

```
extraDepTargets : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") Lean.Name
```

**Deprecated. Use`needs` instead.** An `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` of target names to build before the library's modules.

```
precompileModules : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Whether to compile each of the library's modules into a native shared library that is loaded whenever the module is imported. This speeds up evaluation of metaprograms and enables the interpreter to run functions marked `@[[extern](Run-Time-Code/Foreign-Function-Interface/#Lean___Parser___Attr___extern "Documentation for syntax")]`.
Defaults to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.

```
defaultFacets : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") Lean.Name
```

An `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` of library facets to build on a bare `lake build` of the library. For example, `#[LeanLib.sharedFacet]` will build the shared library facet.

```
nativeFacets : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") (Lake.ModuleFacet [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))
```

The module facets to build and combine into the library's static and shared libraries. If `shouldExport` is true, the module facets should export any symbols a user may expect to lookup in the library. For example, the Lean interpreter will use exported symbols in linked libraries.
Defaults to a singleton of `Module.oExportFacet` (if `shouldExport`) or `Module.oFacet`. That is, the object files compiled from the Lean sources, potentially with exported Lean symbols.

```
allowImportAll : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Whether downstream packages can `import all` modules of this library.
If enabled, downstream users will be able to access the `private` internals of modules, including definition bodies not marked as `@[expose]`. This may also, in the future, prevent compiler optimization which rely on `private` definitions being inaccessible outside their own package.
Defaults to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
#####  24.1.3.2.4.2. Executables[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Targets--Executables "Permalink")
syntaxExecutable Targets
To define an executable in which all configurable fields have their default values, use ``Lake.DSL.leanExeCommand : command`
Define a new Lean binary executable target for the package. Can optionally be provided with a configuration of type `LeanExeConfig`. Has many forms:

```
lean_exe «target-name»
lean_exe «target-name» { /- config opts -/ }
lean_exe «target-name» where /- config opts -/

```

``lean_exe` with no further fields.

```
command ::= ...
    | 


Define a new Lean binary executable target for the package.
Can optionally be provided with a configuration of type LeanExeConfig.
Has many forms:


```
lean_exe «target-name»
lean_exe «target-name» { /- config opts -/ }
lean_exe «target-name» where /- config opts -/

```

`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? [attributes](Attributes/#Lean___Parser___Term___attributes-next)? lean_exe identOrStr
```

The default configuration can be modified by providing the new values.

```
command ::= ...
    | 


Define a new Lean binary executable target for the package.
Can optionally be provided with a configuration of type LeanExeConfig.
Has many forms:


```
lean_exe «target-name»
lean_exe «target-name» { /- config opts -/ }
lean_exe «target-name» where /- config opts -/

```

`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? [attributes](Attributes/#Lean___Parser___Term___attributes-next)? lean_exe identOrStr where [` A field assignment in a declarative configuration.  `declField](Build-Tools-and-Distribution/Lake/#Lake___DSL___declField-next)*
```

```
command ::= ...
    | 


Define a new Lean binary executable target for the package.
Can optionally be provided with a configuration of type LeanExeConfig.
Has many forms:


```
lean_exe «target-name»
lean_exe «target-name» { /- config opts -/ }
lean_exe «target-name» where /- config opts -/

```

`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? [attributes](Attributes/#Lean___Parser___Term___attributes-next)? lean_exe identOrStr { [` A field assignment in a declarative configuration.  `declField](Build-Tools-and-Distribution/Lake/#Lake___DSL___declField-next);* } (where `
 
`letRecDecl` matches the body of a let-rec declaration: a doc comment, attributes, and then a let declaration without the `let` keyword, such as `/-- foo -/ @[simp] bar := 1`. 
`letRecDecl;*)?
```

The fields of ``Lake.DSL.leanExeCommand : command`
Define a new Lean binary executable target for the package. Can optionally be provided with a configuration of type `LeanExeConfig`. Has many forms:

```
lean_exe «target-name»
lean_exe «target-name» { /- config opts -/ }
lean_exe «target-name» where /- config opts -/

```

``lean_exe` are those of the `[LeanExeConfig](Build-Tools-and-Distribution/Lake/#Lake___LeanExeConfig___mk "Documentation for Lake.LeanExeConfig")` structure.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.LeanExeConfig.toLeanConfig "Permalink")structure
```


Lake.LeanExeConfig (name : Lean.Name) : Type


Lake.LeanExeConfig (name : Lean.Name) :
  Type


```

A Lean executable's declarative configuration.
#  Constructor

```
[Lake.LeanExeConfig.mk](Build-Tools-and-Distribution/Lake/#Lake___LeanExeConfig___mk "Documentation for Lake.LeanExeConfig.mk")
```

#  Extends
  * `Lake.LeanConfig`


#  Fields

```
buildType : [Lake.BuildType](Build-Tools-and-Distribution/Lake/#Lake___BuildType___debug "Documentation for Lake.BuildType")
```

Inherited from 
  1. `Lake.LeanConfig`



```
leanOptions : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.LeanOption](Build-Tools-and-Distribution/Lake/#Lean___LeanOption___mk "Documentation for Lean.LeanOption")
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreLeanArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
weakLeanArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreLeancArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreServerOptions : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.LeanOption](Build-Tools-and-Distribution/Lake/#Lean___LeanOption___mk "Documentation for Lean.LeanOption")
```

Inherited from 
  1. `Lake.LeanConfig`



```
weakLeancArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreLinkObjs : Lake.TargetArray [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreLinkLibs : Lake.TargetArray Lake.Dynlib
```

Inherited from 
  1. `Lake.LeanConfig`



```
moreLinkArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
weakLinkArgs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Inherited from 
  1. `Lake.LeanConfig`



```
backend : [Lake.Backend](Build-Tools-and-Distribution/Lake/#Lake___Backend___c "Documentation for Lake.Backend")
```

Inherited from 
  1. `Lake.LeanConfig`



```
platformIndependent : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Inherited from 
  1. `Lake.LeanConfig`



```
dynlibs : Lake.TargetArray Lake.Dynlib
```

Inherited from 
  1. `Lake.LeanConfig`



```
plugins : Lake.TargetArray Lake.Dynlib
```

Inherited from 
  1. `Lake.LeanConfig`



```
srcDir : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")
```

The subdirectory of the package's source directory containing the executable's Lean source file. Defaults simply to said `srcDir`.
(This will be passed to `lean` as the `-R` option.)

```
root : Lean.Name
```

The root module of the binary executable. Should include a `main` definition that will serve as the entry point of the program.
The root is built by recursively building its local imports (i.e., fellow modules of the workspace).
Defaults to the name of the target.

```
exeName : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

The name of the binary executable. Defaults to the target name with any `[.](Tactic-Proofs/The-Tactic-Language/#___ "Documentation for tactic")` replaced with a `-`.

```
needs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") Lake.PartialBuildKey
```

An `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` of targets to build before the executable's modules.

```
extraDepTargets : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") Lean.Name
```

**Deprecated. Use`needs` instead.** An `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` of target names to build before the executable's modules.

```
supportInterpreter : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Enables the executable to interpret Lean files (e.g., via `Lean.Elab.runFrontend`) by exposing symbols within the executable to the Lean interpreter.
Implementation-wise, on Windows, the Lean shared libraries are linked to the executable and, on other systems, the executable is linked with `-rdynamic`. This increases the size of the binary on Linux and, on Windows, requires `libInit_shared.dll` and `libleanshared.dll` to be co-located with the executable or part of `PATH` (e.g., via `lake exe`). Thus, this feature should only be enabled when necessary.
Defaults to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.

```
nativeFacets : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") (Lake.ModuleFacet [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))
```

The module facets to build and combine into the executable. If `shouldExport` is true, the module facets should export any symbols a user may expect to lookup in the executable. For example, the Lean interpreter will use exported symbols in the executable. Thus, `shouldExport` will be `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `supportInterpreter := true`.
Defaults to a singleton of `Module.oExportFacet` (if `shouldExport`) or `Module.oFacet`. That is, the object file compiled from the Lean source, potentially with exported Lean symbols.
#####  24.1.3.2.4.3. External Libraries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Targets--External-Libraries "Permalink")
Because external libraries may be written in any language and require arbitrary build steps, they are defined as programs written in the `FetchM` monad that produce a `Job`. External library targets should produce a build job that carries out the build and then returns the location of the resulting static library. For the external library to link properly when `precompileModules` is on, the static library produced by an `extern_lib` target must follow the platform's naming conventions for libraries (i.e., be named foo.a on Windows or libfoo.a on Unix-like systems). The utility function `Lake.nameToStaticLib` converts a library name into its proper file name for current platform.
syntaxExternal Library Targets

```
command ::= ...
    | 


Define a new external library target for the package. Has one form:


```
extern_lib «target-name» (pkg : NPackage _package.name) :=
  /- build term of type `FetchM (Job FilePath)` -/

```

The `pkg` parameter (and its type specifier) is optional. It is of type `NPackage _package.name` to provably demonstrate the package provided is the package in which the target is defined.
The term should build the external library's **static** library.
`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? [attributes](Attributes/#Lean___Parser___Term___attributes-next)? extern_lib identOrStr simpleBinder? := term `
 
Termination hints are `termination_by` and `decreasing_by`, in that order.
`(where `
 
`letRecDecl` matches the body of a let-rec declaration: a doc comment, attributes, and then a let declaration without the `let` keyword, such as `/-- foo -/ @[simp] bar := 1`. 
`letRecDecl*)?
```

Define a new external library target for the package. Has one form:

```
extern_lib «target-name» (pkg : NPackage _package.name) :=
  /- build term of type `FetchM (Job FilePath)` -/

```

The `pkg` parameter (and its type specifier) is optional. It is of type `NPackage _package.name` to provably demonstrate the package provided is the package in which the target is defined.
The term should build the external library's **static** library.
#####  24.1.3.2.4.4. Custom Targets[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Targets--Custom-Targets "Permalink")
Custom targets may be used to define any incrementally-built artifact whatsoever, using the Lake API.
syntaxCustom Targets

```
command ::= ...
    | 


Define a new custom target for the package. Has one form:


```
target «target-name» (pkg : NPackage _package.name) : α :=
  /- build term of type `FetchM (Job α)` -/

```

The `pkg` parameter (and its type specifier) is optional. It is of type `NPackage _package.name` to provably demonstrate the package provided is the package in which the target is defined.
`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? [attributes](Attributes/#Lean___Parser___Term___attributes-next)? target identOrStr simpleBinder? : term := term `
 
Termination hints are `termination_by` and `decreasing_by`, in that order.
`(where `
 
`letRecDecl` matches the body of a let-rec declaration: a doc comment, attributes, and then a let declaration without the `let` keyword, such as `/-- foo -/ @[simp] bar := 1`. 
`letRecDecl*)?
```

Define a new external library target for the package. Has one form:

```
extern_lib «target-name» (pkg : NPackage _package.name) :=
  /- build term of type `FetchM (Job FilePath)` -/

```

The `pkg` parameter (and its type specifier) is optional. It is of type `NPackage _package.name` to provably demonstrate the package provided is the package in which the target is defined.
The term should build the external library's **static** library.
#####  24.1.3.2.4.5. Custom Facets[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Targets--Custom-Facets "Permalink")
Custom facets allow additional artifacts to be incrementally built from a module, library, or package.
syntaxCustom Package Facets
Package facets allow the production of an artifact or set of artifacts from a whole package. The Lake API makes it possible to query a package for its libraries; thus, one common use for a package facet is to build a given facet of each library.

```
command ::= ...
    | 


Define a new package facet. Has one form:


```
package_facet «facet-name» (pkg : Package) : α :=
  /- build term of type `FetchM (Job α)` -/

```

The `pkg` parameter (and its type specifier) is optional.
`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? ([@[](Attributes/#Lean___Parser___Term___attributes-next)[attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next),*[]](Attributes/#Lean___Parser___Term___attributes-next))? package_facet identOrStr simpleBinder? : term := term `
 
Termination hints are `termination_by` and `decreasing_by`, in that order.
`(where `
 
`letRecDecl` matches the body of a let-rec declaration: a doc comment, attributes, and then a let declaration without the `let` keyword, such as `/-- foo -/ @[simp] bar := 1`. 
`letRecDecl*)?
```

Define a new package facet. Has one form:

```
package_facet «facet-name» (pkg : Package) : α :=
  /- build term of type `FetchM (Job α)` -/

```

The `pkg` parameter (and its type specifier) is optional.
syntaxCustom Library Facets
Library facets allow the production of an artifact or set of artifacts from a library. The Lake API makes it possible to query a library for its modules; thus, one common use for a library facet is to build a given facet of each module.

```
command ::= ...
    | 


Define a new library facet. Has one form:


```
library_facet «facet-name» (lib : LeanLib) : α :=
  /- build term of type `FetchM (Job α)` -/

```

The `lib` parameter (and its type specifier) is optional.
`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? ([@[](Attributes/#Lean___Parser___Term___attributes-next)[attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next),*[]](Attributes/#Lean___Parser___Term___attributes-next))? library_facet identOrStr simpleBinder? : term := term `
 
Termination hints are `termination_by` and `decreasing_by`, in that order.
`(where `
 
`letRecDecl` matches the body of a let-rec declaration: a doc comment, attributes, and then a let declaration without the `let` keyword, such as `/-- foo -/ @[simp] bar := 1`. 
`letRecDecl*)?
```

Define a new library facet. Has one form:

```
library_facet «facet-name» (lib : LeanLib) : α :=
  /- build term of type `FetchM (Job α)` -/

```

The `lib` parameter (and its type specifier) is optional.
syntaxCustom Module Facets
Module facets allow the production of an artifact or set of artifacts from a module, typically by invoking a command-line tool.

```
command ::= ...
    | 


Define a new module facet. Has one form:


```
module_facet «facet-name» (mod : Module) : α :=
  /- build term of type `FetchM (Job α)` -/

```

The `mod` parameter (and its type specifier) is optional.
`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? ([@[](Attributes/#Lean___Parser___Term___attributes-next)[attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next),*[]](Attributes/#Lean___Parser___Term___attributes-next))? module_facet identOrStr simpleBinder? : term := term `
 
Termination hints are `termination_by` and `decreasing_by`, in that order.
`(where `
 
`letRecDecl` matches the body of a let-rec declaration: a doc comment, attributes, and then a let declaration without the `let` keyword, such as `/-- foo -/ @[simp] bar := 1`. 
`letRecDecl*)?
```

Define a new module facet. Has one form:

```
module_facet «facet-name» (mod : Module) : α :=
  /- build term of type `FetchM (Job α)` -/

```

The `mod` parameter (and its type specifier) is optional.
####  24.1.3.2.5. Configuration Value Types[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Configuration-Value-Types "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.BuildType.relWithDebInfo "Permalink")inductive type
```


Lake.BuildType : Type


Lake.BuildType : Type


```

Lake equivalent of CMake's [`CMAKE_BUILD_TYPE`](https://stackoverflow.com/a/59314670).
#  Constructors

```
debug : [Lake.BuildType](Build-Tools-and-Distribution/Lake/#Lake___BuildType___debug "Documentation for Lake.BuildType")
```

Debug optimization, asserts enabled, custom debug code enabled, and debug info included in executable (so you can step through the code with a debugger and have address to source-file:line-number translation). For example, passes `-O0 -g` when compiling C code.

```
relWithDebInfo : [Lake.BuildType](Build-Tools-and-Distribution/Lake/#Lake___BuildType___debug "Documentation for Lake.BuildType")
```

Optimized, _with_ debug info, but no debug code or asserts (e.g., passes `-O3 -g -DNDEBUG` when compiling C code).

```
minSizeRel : [Lake.BuildType](Build-Tools-and-Distribution/Lake/#Lake___BuildType___debug "Documentation for Lake.BuildType")
```

Same as `[release](Build-Tools-and-Distribution/Lake/#Lake___BuildType___debug "Documentation for Lake.BuildType.release")` but optimizing for size rather than speed (e.g., passes `-Os -DNDEBUG` when compiling C code).

```
release : [Lake.BuildType](Build-Tools-and-Distribution/Lake/#Lake___BuildType___debug "Documentation for Lake.BuildType")
```

High optimization level and no debug info, code, or asserts (e.g., passes `-O3 -DNDEBUG` when compiling C code).
In Lake's DSL, _globs_ are patterns that match sets of module names. There is a coercion from names to globs that match the name in question, and there are two postfix operators for constructing further globs.
syntaxGlob Syntax
The glob pattern `N.*` matches `N` or any submodule for which `N` is a prefix.

```
term ::= ...
    | name.*
```

The glob pattern `N.+` matches any submodule for which `N` is a strict prefix, but not `N` itself.

```
term ::= ...
    | name.+
```

Whitespace is not permitted between the name and `.*` or `.+`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.Glob.andSubmodules "Permalink")inductive type
```


Lake.Glob : Type


Lake.Glob : Type


```

A specification of a set of module names.
#  Constructors

```
one : Lean.Name → [Lake.Glob](Build-Tools-and-Distribution/Lake/#Lake___Glob___one "Documentation for Lake.Glob")
```

Selects just the specified module name.

```
submodules : Lean.Name → [Lake.Glob](Build-Tools-and-Distribution/Lake/#Lake___Glob___one "Documentation for Lake.Glob")
```

Selects all submodules of the specified module, but not the module itself.

```
andSubmodules : Lean.Name → [Lake.Glob](Build-Tools-and-Distribution/Lake/#Lake___Glob___one "Documentation for Lake.Glob")
```

Selects the specified module and all submodules.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.LeanOption.value "Permalink")structure
```


Lean.LeanOption : Type


Lean.LeanOption : Type


```

An option that is used by Lean as if it was passed using `-D`.
#  Constructor

```
[Lean.LeanOption.mk](Build-Tools-and-Distribution/Lake/#Lean___LeanOption___mk "Documentation for Lean.LeanOption.mk")
```

#  Fields

```
name : Lean.Name
```

The option's name.

```
value : Lean.LeanOptionValue
```

The option's value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.Backend "Permalink")inductive type
```


Lake.Backend : Type


Lake.Backend : Type


```

Compiler backend with which to compile Lean.
#  Constructors

```
c : [Lake.Backend](Build-Tools-and-Distribution/Lake/#Lake___Backend___c "Documentation for Lake.Backend")
```

Force the C backend.

```
llvm : [Lake.Backend](Build-Tools-and-Distribution/Lake/#Lake___Backend___c "Documentation for Lake.Backend")
```

Force the LLVM backend.

```
default : [Lake.Backend](Build-Tools-and-Distribution/Lake/#Lake___Backend___c "Documentation for Lake.Backend")
```

Use the default backend. Can be overridden by more specific configuration.
####  24.1.3.2.6. Scripts[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Scripts "Permalink")
Lake scripts are used to automate tasks that require access to a package configuration but do not participate in incremental builds of artifacts from code. Scripts run in the `ScriptM` monad, which is `[IO](IO/Logical-Model/#IO "Documentation for IO")` with an additional [reader monad](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#--tech-term-Reader-monads) [transformer](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#--tech-term-monad-transformer) that provides access to the package configuration. In particular, a script should have the type `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → ScriptM [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`. Workspace information in scripts is primarily accessed via the `[MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") ScriptM` instance.
syntaxScript Declarations

```
command ::= ...
    | 


Define a new Lake script for the package.


**Example**


```
/-- Display a greeting -/
script «script-name» (args) do
  if h : 0 < args.length then
    IO.println s!"Hello, {args[0]'h}!"
  else
    IO.println "Hello, world!"
  return 0

```

`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? ([@[](Attributes/#Lean___Parser___Term___attributes-next)[attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next),*[]](Attributes/#Lean___Parser___Term___attributes-next))? script identOrStr simpleBinder? := term `
 
Termination hints are `termination_by` and `decreasing_by`, in that order.
`(where `
 
`letRecDecl` matches the body of a let-rec declaration: a doc comment, attributes, and then a let declaration without the `let` keyword, such as `/-- foo -/ @[simp] bar := 1`. 
`letRecDecl*)?
```

Define a new Lake script for the package.
**Example**

```
/-- Display a greeting -/
script «script-name» (args) do
  if h : 0 < args.length then
    IO.println s!"Hello, {args[0]'h}!"
  else
    IO.println "Hello, world!"
  return 0

```

[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.ScriptM "Permalink")def
```


Lake.ScriptM (α : Type) : Type


Lake.ScriptM (α : Type) : Type


```

The type of a `Script`'s monad.
It is an `[IO](IO/Logical-Model/#IO "Documentation for IO")` monad equipped information about the Lake configuration.
attributeDefault Scripts

```
attr ::= ...
    | default_script
```

Marks a [Lake script](Build-Tools-and-Distribution/Lake/#--tech-term-Lake-scripts) as the [package](Build-Tools-and-Distribution/Lake/#--tech-term-package)'s default.
####  24.1.3.2.7. Utilities[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Configuration-File-Format--Lean-Format--Utilities "Permalink")
syntaxThe Current Directory

```
term ::= ...
    | 


A macro that expands to the path of package's directory
during the Lakefile's elaboration.


__dir__
```

A macro that expands to the path of package's directory during the Lakefile's elaboration.
syntaxConfiguration Options

```
term ::= ...
    | 


A macro that expands to the specified configuration option (or none,
if the option has not been set) during the Lakefile's elaboration.


Configuration arguments are set either via the Lake CLI (by the -K option)
or via the with clause in a require statement.


get_config? ident
```

A macro that expands to the specified configuration option (or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, if the option has not been set) during the Lakefile's elaboration.
Configuration arguments are set either via the Lake CLI (by the `-K` option) or via the `with` clause in a `require` statement.
syntaxCompile-Time Conditionals

```
command ::= ...
    | 


The meta if command has two forms:


```
meta if <c:term> then <a:command>
meta if <c:term> then <a:command> else <b:command>

```

It expands to the command `a` if the term `c` evaluates to true (at elaboration time). Otherwise, it expands to command `b` (if an `else` clause is provided).
One can use this command to specify, for example, external library targets only available on specific platforms:

```
meta if System.Platform.isWindows then
extern_lib winOnlyLib := ...
else meta if System.Platform.isOSX then
extern_lib macOnlyLib := ...
else
extern_lib linuxOnlyLib := ...

```

`meta if term then `
 
The `do` command syntax groups multiple similarly indented commands together. The group can then be passed to another command that usually only accepts a single command (e.g., `meta if`).
`cmdDo (else `
 
The `do` command syntax groups multiple similarly indented commands together. The group can then be passed to another command that usually only accepts a single command (e.g., `meta if`).
`cmdDo)?
```

The `meta if` command has two forms:

```
meta if <c:term> then <a:command>
meta if <c:term> then <a:command> else <b:command>

```

It expands to the command `a` if the term `c` evaluates to true (at elaboration time). Otherwise, it expands to command `b` (if an `else` clause is provided).
One can use this command to specify, for example, external library targets only available on specific platforms:

```
meta if System.Platform.isWindows then
extern_lib winOnlyLib := ...
else meta if System.Platform.isOSX then
extern_lib macOnlyLib := ...
else
extern_lib linuxOnlyLib := ...

```

syntaxCommand Sequences

```
cmdDo ::= ...
    | 


The do command syntax groups multiple similarly indented commands together.
The group can then be passed to another command that usually only accepts a
single command (e.g., meta if).


command
```

```
cmdDo ::= ...
    | 


The do command syntax groups multiple similarly indented commands together.
The group can then be passed to another command that usually only accepts a
single command (e.g., meta if).


do
        command
        command*
```

The `do` command syntax groups multiple similarly indented commands together. The group can then be passed to another command that usually only accepts a single command (e.g., `meta if`).
syntaxCompile-Time Side Effects

```
term ::= ...
    | 


Executes a term of type IO α at elaboration-time
and produces an expression corresponding to the result via ToExpr α.


run_io doSeq
```

Executes a term of type `[IO](IO/Logical-Model/#IO "Documentation for IO") α` at elaboration-time and produces an expression corresponding to the result via `ToExpr α`.
##  24.1.4. Script API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=lake-api "Permalink")
In addition to ordinary `[IO](IO/Logical-Model/#IO "Documentation for IO")` effects, Lake scripts have access to the Lake environment (which provides information about the current toolchain, such as the location of the Lean compiler) and the current workspace. This access is provided in `ScriptM`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.ScriptM "Permalink")def
```


Lake.ScriptM (α : Type) : Type


Lake.ScriptM (α : Type) : Type


```

The type of a `Script`'s monad.
It is an `[IO](IO/Logical-Model/#IO "Documentation for IO")` monad equipped information about the Lake configuration.
###  24.1.4.1. Accessing the Environment[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Script-API-Reference--Accessing-the-Environment "Permalink")
Monads that provide access to information about the current Lake environment (such as the locations of Lean, Lake, and other tools) have `[MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv")` instances. This is true for all of the monads in the Lake API, including `ScriptM`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.MonadLakeEnv "Permalink")def
```


Lake.MonadLakeEnv.{u} (m : Type → Type u) : Type u


Lake.MonadLakeEnv.{u}
  (m : Type → Type u) : Type u


```

A monad equipped with a (read-only) detected environment for Lake.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLakeEnv "Permalink")def
```


Lake.getLakeEnv.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] :
  m Lake.Env


Lake.getLakeEnv.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] : m Lake.Env


```

Gets the current Lake environment.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getNoCache "Permalink")def
```


Lake.getNoCache.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] [Lake.MonadBuild m] : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Lake.getNoCache.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  [Lake.MonadBuild m] : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns the `LAKE_NO_CACHE`/`` Lake configuration.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getTryCache "Permalink")def
```


Lake.getTryCache.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] [Lake.MonadBuild m] : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Lake.getTryCache.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  [Lake.MonadBuild m] : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns whether the `LAKE_NO_CACHE`/`` Lake configuration is **NOT** set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getPkgUrlMap "Permalink")def
```


Lake.getPkgUrlMap.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m (Lean.NameMap [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))


Lake.getPkgUrlMap.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m (Lean.NameMap [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))


```

Returns the `LAKE_PACKAGE_URL_MAP` for the Lake environment. Empty if none.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getElanToolchain "Permalink")def
```


Lake.getElanToolchain.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Lake.getElanToolchain.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Returns the name of Elan toolchain for the Lake environment. Empty if none.
####  24.1.4.1.1. Search Path Helpers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Script-API-Reference--Accessing-the-Environment--Search-Path-Helpers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getEnvLeanPath "Permalink")def
```


Lake.getEnvLeanPath.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m System.SearchPath


Lake.getEnvLeanPath.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m System.SearchPath


```

Returns the detected `LEAN_PATH` value of the Lake environment.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getEnvLeanSrcPath "Permalink")def
```


Lake.getEnvLeanSrcPath.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m System.SearchPath


Lake.getEnvLeanSrcPath.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m System.SearchPath


```

Returns the detected `LEAN_SRC_PATH` value of the Lake environment.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getEnvSharedLibPath "Permalink")def
```


Lake.getEnvSharedLibPath.{u_1} {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m System.SearchPath


Lake.getEnvSharedLibPath.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m System.SearchPath


```

Returns the detected `sharedLibPathEnvVar` value of the Lake environment.
####  24.1.4.1.2. Elan Install Helpers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Script-API-Reference--Accessing-the-Environment--Elan-Install-Helpers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getElanInstall? "Permalink")def
```


Lake.getElanInstall?.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.ElanInstall)


Lake.getElanInstall?.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.ElanInstall)


```

Returns the detected Elan installation (if one).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getElanHome? "Permalink")def
```


Lake.getElanHome?.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))


Lake.getElanHome?.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))


```

Returns the root directory of the detected Elan installation (i.e., `ELAN_HOME`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getElan? "Permalink")def
```


Lake.getElan?.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))


Lake.getElan?.{u_1} {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))


```

Returns the path of the `elan` binary in the detected Elan installation.
####  24.1.4.1.3. Lean Install Helpers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Script-API-Reference--Accessing-the-Environment--Lean-Install-Helpers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanInstall "Permalink")def
```


Lake.getLeanInstall.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m Lake.LeanInstall


Lake.getLeanInstall.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m Lake.LeanInstall


```

Returns the detected Lean installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanSysroot "Permalink")def
```


Lake.getLeanSysroot.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLeanSysroot.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the root directory of the detected Lean installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanSrcDir "Permalink")def
```


Lake.getLeanSrcDir.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLeanSrcDir.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the Lean source directory of the detected Lean installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanLibDir "Permalink")def
```


Lake.getLeanLibDir.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLeanLibDir.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the Lean library directory of the detected Lean installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanIncludeDir "Permalink")def
```


Lake.getLeanIncludeDir.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLeanIncludeDir.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the C include directory of the detected Lean installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanSystemLibDir "Permalink")def
```


Lake.getLeanSystemLibDir.{u_1} {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLeanSystemLibDir.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the system library directory of the detected Lean installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLean "Permalink")def
```


Lake.getLean.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLean.{u_1} {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the path of the `lean` binary in the detected Lean installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanc "Permalink")def
```


Lake.getLeanc.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLeanc.{u_1} {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the path of the `leanc` binary in the detected Lean installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanSharedLib "Permalink")def
```


Lake.getLeanSharedLib.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLeanSharedLib.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the path of the `libleanshared` library in the detected Lean installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanAr "Permalink")def
```


Lake.getLeanAr.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLeanAr.{u_1} {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Get the path of the `ar` binary in the detected Lean installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanCc "Permalink")def
```


Lake.getLeanCc.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLeanCc.{u_1} {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Get the path of C compiler in the detected Lean installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanCc? "Permalink")def
```


Lake.getLeanCc?.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))


Lake.getLeanCc?.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))


```

Get the optional `LEAN_CC` compiler override of the detected Lean installation.
####  24.1.4.1.4. Lake Install Helpers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Script-API-Reference--Accessing-the-Environment--Lake-Install-Helpers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLakeInstall "Permalink")def
```


Lake.getLakeInstall.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m Lake.LakeInstall


Lake.getLakeInstall.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m Lake.LakeInstall


```

Get the detected Lake installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLakeHome "Permalink")def
```


Lake.getLakeHome.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLakeHome.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Get the root directory of the detected Lake installation (e.g., `LAKE_HOME`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLakeSrcDir "Permalink")def
```


Lake.getLakeSrcDir.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLakeSrcDir.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Get the source directory of the detected Lake installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLakeLibDir "Permalink")def
```


Lake.getLakeLibDir.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLakeLibDir.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Get the Lean library directory of the detected Lake installation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLake "Permalink")def
```


Lake.getLake.{u_1} {m : Type → Type u_1} [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


Lake.getLake.{u_1} {m : Type → Type u_1}
  [[Lake.MonadLakeEnv](Build-Tools-and-Distribution/Lake/#Lake___MonadLakeEnv "Documentation for Lake.MonadLakeEnv") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Get the path of the `lake` binary in the detected Lake installation.
###  24.1.4.2. Accessing the Workspace[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Build-Tools-and-Distribution--Lake--Script-API-Reference--Accessing-the-Workspace "Permalink")
Monads that provide access to information about the current Lake workspace have `[MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace")` instances. In particular, there are instances for `ScriptM` and `LakeM`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.MonadWorkspace.mk "Permalink")type class
```


Lake.MonadWorkspace.{u} (m : Type → Type u) : Type u


Lake.MonadWorkspace.{u}
  (m : Type → Type u) : Type u


```

A monad equipped with a (read-only) Lake `Workspace`.
#  Instance Constructor

```
[Lake.MonadWorkspace.mk](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace.mk").{u}
```

#  Methods

```
getWorkspace : m Lake.Workspace
```

Gets the current Lake workspace.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getRootPackage "Permalink")def
```


Lake.getRootPackage.{u_1} {m : Type → Type u_1} [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m Lake.Package


Lake.getRootPackage.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m Lake.Package


```

Returns the root package of the context's workspace.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.findPackageByName? "Permalink")def
```


Lake.findPackageByName?.{u_1} {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] (name : Lean.Name) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.Package)


Lake.findPackageByName?.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  (name : Lean.Name) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.Package)


```

Returns the first package in the workspace (if any) that has been assigned the `name`.
This can be used to find the package corresponding to a user-provided name. If the package's unique identifier is already available, use `findPackageByKey?`instead.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.findPackageByKey? "Permalink")def
```


Lake.findPackageByKey?.{u_1} {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] (keyName : Lean.Name) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (Lake.NPackage keyName))


Lake.findPackageByKey?.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  (keyName : Lean.Name) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (Lake.NPackage keyName))


```

Returns the unique package in the workspace (if any) that is identified by `keyName`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.findModule? "Permalink")def
```


Lake.findModule?.{u_1} {m : Type → Type u_1} [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] (name : Lean.Name) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.Module)


Lake.findModule?.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  (name : Lean.Name) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.Module)


```

Locate the named, buildable, importable, local module in the workspace.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.findLeanExe? "Permalink")def
```


Lake.findLeanExe?.{u_1} {m : Type → Type u_1} [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] (name : Lean.Name) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.LeanExe)


Lake.findLeanExe?.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  (name : Lean.Name) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.LeanExe)


```

Try to find a Lean executable in the workspace with the given name.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.findLeanLib? "Permalink")def
```


Lake.findLeanLib?.{u_1} {m : Type → Type u_1} [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] (name : Lean.Name) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.LeanLib)


Lake.findLeanLib?.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  (name : Lean.Name) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.LeanLib)


```

Try to find a Lean library in the workspace with the given name.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.findExternLib? "Permalink")def
```


Lake.findExternLib?.{u_1} {m : Type → Type u_1} [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] (name : Lean.Name) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.ExternLib)


Lake.findExternLib?.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  (name : Lean.Name) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Lake.ExternLib)


```

Try to find an external library in the workspace with the given name.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanPath "Permalink")def
```


Lake.getLeanPath.{u_1} {m : Type → Type u_1} [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m System.SearchPath


Lake.getLeanPath.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m System.SearchPath


```

Returns the paths added to `LEAN_PATH` by the context's workspace.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getLeanSrcPath "Permalink")def
```


Lake.getLeanSrcPath.{u_1} {m : Type → Type u_1} [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m System.SearchPath


Lake.getLeanSrcPath.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m System.SearchPath


```

Returns the paths added to `LEAN_SRC_PATH` by the context's workspace.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getSharedLibPath "Permalink")def
```


Lake.getSharedLibPath.{u_1} {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m System.SearchPath


Lake.getSharedLibPath.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m System.SearchPath


```

Returns the paths added to the shared library path by the context's workspace.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getAugmentedLeanPath "Permalink")def
```


Lake.getAugmentedLeanPath.{u_1} {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m System.SearchPath


Lake.getAugmentedLeanPath.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m System.SearchPath


```

Returns the augmented `LEAN_PATH` set by the context's workspace.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getAugmentedLeanSrcPath "Permalink")def
```


Lake.getAugmentedLeanSrcPath.{u_1} {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m System.SearchPath


Lake.getAugmentedLeanSrcPath.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m System.SearchPath


```

Returns the augmented `LEAN_SRC_PATH` set by the context's workspace.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getAugmentedSharedLibPath "Permalink")def
```


Lake.getAugmentedSharedLibPath.{u_1} {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m System.SearchPath


Lake.getAugmentedSharedLibPath.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m System.SearchPath


```

Returns the augmented shared library path set by the context's workspace.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lake.getAugmentedEnv "Permalink")def
```


Lake.getAugmentedEnv.{u_1} {m : Type → Type u_1} [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m]
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod"))


Lake.getAugmentedEnv.{u_1}
  {m : Type → Type u_1}
  [[Lake.MonadWorkspace](Build-Tools-and-Distribution/Lake/#Lake___MonadWorkspace___mk "Documentation for Lake.MonadWorkspace") m] [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] :
  m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod"))


```

Returns the augmented environment variables set by the context's workspace.
[←24. Build Tools and Distribution](Build-Tools-and-Distribution/#build-tools-and-distribution "24. Build Tools and Distribution")[24.2. Managing Toolchains with Elan→](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan "24.2. Managing Toolchains with Elan")

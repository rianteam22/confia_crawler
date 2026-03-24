[←24.1. Lake](Build-Tools-and-Distribution/Lake/#lake "24.1. Lake")[Validating a Lean Proof→](ValidatingProofs/#validating-proofs "Validating a Lean Proof")
#  24.2. Managing Toolchains with Elan[🔗](find/?domain=Verso.Genre.Manual.section&name=elan "Permalink")
Elan is the Lean toolchain manager. It is responsible both for installing [toolchains](Build-Tools-and-Distribution/#--tech-term-toolchain) and for running their constituent programs. Elan makes it possible to seamlessly work on a variety of projects, each of which is designed to be built with a particular version of Lean, without having to manually install and select toolchain versions. Each project is typically configured to use a particular version, which is transparently installed as needed, and changes to the Lean version are tracked automatically.
##  24.2.1. Selecting Toolchains[🔗](find/?domain=Verso.Genre.Manual.section&name=elan-toolchain-versions "Permalink")
When using Elan, the version of each tool on the `PATH` is a proxy that invokes the correct version. The proxy determines the appropriate toolchain version for the current context, ensures that it is installed, and then invokes the underlying tool in the appropriate toolchain installation. These proxies can be instructed to use a specific version by passing it as an argument prefixed with `+`, so `lake +4.0.0` invokes `lake` version `4.0.0`, after installing it if necessary.
###  24.2.1.1. Toolchain Identifiers[🔗](find/?domain=Verso.Genre.Manual.section&name=elan-channels "Permalink")
Toolchains are specified by providing a toolchain identifier that is either a _channel_ , which identifies a particular type of Lean release, and optionally an origin, or a _custom toolchain name_ established by [`elan toolchain link`](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#toolchain-link). Channels may be: 

`stable` 
    
The latest stable Lean release. Elan automatically tracks stable releases and offers to upgrade when a new one is released. 

`beta` 
    
The latest release candidate. Release candidates are builds of Lean that are intended to become the next stable release. They are made available for widespread user testing. 

`nightly` 
    
The latest nightly build. Nightly builds are useful for experimenting with new Lean features to provide feedback to the developers. 

A version number or specific nightly release
    
Each Lean version number identifies a channel that contains only that release. The version number may optionally be preceded with a `v`, so `v4.17.0` and `4.17.0` are equivalent. Similarly, `nightly-YYYY-MM-DD` specifies the nightly release from the specified date. A project's [toolchain file](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#--tech-term-toolchain-file) should typically contain a specific version of Lean, rather than a general channel, to make it easier to coordinate between developers and to build and test older versions of the project. An archive of Lean releases and nightly builds is maintained. 

A custom local toolchain
    
The command [`elan toolchain link`](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#toolchain-link) can be used to establish a custom toolchain name in Elan for a local build of Lean. This is especially useful when working on the Lean compiler itself.
Specifying an _origin_ instructs Elan to install Lean toolchains from a particular source. By default, this is the official project repository on GitHub, identified as [`leanprover/lean4`](https://github.com/leanprover/lean4/releases). If specified, an origin should precede the channel, with a colon, so `stable` is equivalent to `leanprover/lean4:stable`. When installing nightly releases, `-nightly` is appended to the origin, so `leanprover/lean4:nightly-2025-03-25` consults the [`leanprover/lean4-nightly`](https://github.com/leanprover/lean4-nightly/releases) repository to download releases. Origins are not used for custom toolchain names.
###  24.2.1.2. Determining the Current Toolchain[🔗](find/?domain=Verso.Genre.Manual.section&name=elan-toolchain-config "Permalink")
Elan associates toolchains with directories, and uses the toolchain of the most recent parent directory of the current working directory that has a configured toolchain. A directory's toolchain may result from a toolchain file or from an override configured with [`elan override`](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan-override).
The current toolchain is determined by first searching for a configured toolchain for the current directory, walking up through parent directories until a toolchain version is found or there are no more parents. A directory has a configured toolchain if there is a configured [toolchain override](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#--tech-term-toolchain-override) for the directory or if it contains a `lean-toolchain` file. More recent parents take precedence over their ancestors, and if a directory has both an override and a toolchain file, then the override takes precedence. If no directory toolchain is found, then Elan's configured _default toolchain_ is used as a fallback.
The most common way to configure a Lean toolchain is with a _toolchain file_. The toolchain file is a text file named `lean-toolchain` that contains a single line with a valid [toolchain identifier](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan-channels). This file is typically located in the root directory of a project and checked in to version control with the code, ensuring that everyone working on the project uses the same version. Updating to a new Lean toolchain requires only editing this file, and the new version is automatically downloaded and run the next time a Lean file is opened or built.
In certain advanced use cases where more flexibility is required, a _toolchain override_ can be configured. Like toolchain files, overrides associate a toolchain version with a directory and its children. Unlike toolchain files, overrides are stored in Elan's configuration rather than in a local file. They are typically used when a specific local configuration is required that does not make sense for other developers, such as testing a project with a locally-built Lean compiler.
##  24.2.2. Toolchain Locations[🔗](find/?domain=Verso.Genre.Manual.section&name=elan-dir "Permalink")
By default, Elan stores installed toolchains in `.elan/toolchains` in the user's home directory, and its proxies are kept in `.elan/bin`, which is added to the path when Elan is installed. The environment variable `ELAN_HOME` can be used to change this location. It should be set both prior to installing Elan and in all sessions that use Lean in order to ensure that Elan's files are found.
##  24.2.3. Command-Line Interface[🔗](find/?domain=Verso.Genre.Manual.section&name=elan-cli "Permalink")
In addition to the proxies that automatically select, install, and invoke the correct versions of Lean tools, Elan provides a command-line interface for querying and configuring its settings. This tool is called `elan`. Like [Lake](Build-Tools-and-Distribution/Lake/#lake), its command-line interface is structured around subcommands.
Elan can be invoked with following flags: 

`--help` or `-h` 
    
Describes the current subcommand in detail. 

`--verbose` or `-v` 
    
Enables verbose output. 

`--version` or `-V` 
    
Displays the Elan version.
###  24.2.3.1. Querying Toolchains[🔗](find/?domain=Verso.Genre.Manual.section&name=elan-show "Permalink")
The [`elan show`](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#show-next) command displays the current toolchain (as determined by the current directory) and lists all installed toolchains.
[🔗](find/?domain=Manual.elanCommand&name=show "Permalink")Elan command
```
elan show 
```

Shows the name of the active toolchain and the version of `lean`.
If there are multiple toolchains installed, then they are all listed.
Here is typical output from [`elan show`](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#show-next) in a project with a `lean-toolchain` file:

```
installed toolchains
--------------------

leanprover/lean4:nightly-2025-03-25
leanprover/lean4:v4.17.0  (resolved from default 'stable')
leanprover/lean4:v4.16.0
leanprover/lean4:v4.9.0

active toolchain
----------------

leanprover/lean4:v4.9.0 (overridden by '/PATH/TO/PROJECT/lean-toolchain')
Lean (version 4.9.0, arm64-apple-darwin23.5.0, commit 8f9843a4a5fe, Release)

```

The `installed toolchains` section lists all the toolchains currently available on the system. The `active toolchain` section identifies the current toolchain and describes how it was selected. In this case, the toolchain was selected due to a `lean-toolchain` file.
###  24.2.3.2. Setting the Default Toolchain[🔗](find/?domain=Verso.Genre.Manual.section&name=elan-default "Permalink")
Elan's configuration file specifies a [default toolchain](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#--tech-term-default-toolchain) to be used when there is no `lean-toolchain` file or [toolchain override](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#--tech-term-toolchain-override) for the current directory. Rather than manually editing the file, this value is typically changed using the [`elan default`](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#default) command.
[🔗](find/?domain=Manual.elanCommand&name=default "Permalink")Elan command
```
elan default toolchain
```

Sets the default toolchain to `toolchain`, which should be a [valid toolchain identifier](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan-channels) such as `stable`, `nightly`, or `4.17.0`.
###  24.2.3.3. Managing Installed Toolchains[🔗](find/?domain=Verso.Genre.Manual.section&name=elan-toolchain "Permalink")
The `elan toolchain` family of subcommands is used to manage the installed toolchains. Toolchains are stored in Elan's [toolchain directory](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan-dir).
Installed toolchains can take up substantial disk space. Elan tracks the Lean projects in which it is invoked, saving a list. This list of projects can be used to determine which toolchains are in active use and automatically delete unused toolchain versions with [`elan toolchain gc`](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#toolchain-gc).
[🔗](find/?domain=Manual.elanCommand&name=toolchain%20list "Permalink")Elan command
```
elan toolchain list 
```

Lists the currently-installed toolchains. This is a subset of the output of [`elan show`](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#show-next).
[🔗](find/?domain=Manual.elanCommand&name=toolchain%20install "Permalink")Elan command
```
elan toolchain install toolchain
```

Installs the indicated `toolchain`. The toolchain's name should be [an identifier that's suitable for inclusion in a `lean-toolchain` file](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan-channels).
[🔗](find/?domain=Manual.elanCommand&name=toolchain%20uninstall "Permalink")Elan command
```
elan toolchain uninstall toolchain
```

Uninstalls the indicated `toolchain`. The toolchain's name should the name of an installed toolchain. Use [`elan toolchain list`](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#toolchain-list) to see the installed toolchains with their names.
[🔗](find/?domain=Manual.elanCommand&name=toolchain%20link "Permalink")Elan command
```
elan toolchain link local-name path
```

Creates a new local toolchain named `local-name`, using the Lean toolchain found at `path`.
[🔗](find/?domain=Manual.elanCommand&name=toolchain%20gc "Permalink")Elan command
```
elan toolchain gc [--delete] [--json]
```

This command is still considered experimental.
Determines which of the installed toolchains are in use, offering to delete those that are not. All the installed toolchains are listed, separated into those that are in use and those that are not.
A toolchain is classified as “in use” if
  * it is the default toolchain,
  * it is registered as an override, or
  * there is a directory with a `lean-toolchain` file referencing the toolchain and elan has been used in the directory before.


For safety reasons, [`elan toolchain gc`](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#toolchain-gc) will not actually delete any toolchains unless the `--delete` flag is passed. This may be relaxed in the future when the implementation is deemed sufficiently mature. The `--json` flag causes [`elan toolchain gc`](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#toolchain-gc) to emit the list of used and unused toolchains in a JSON format that's suitable for other tools.
###  24.2.3.4. Managing Directory Overrides[🔗](find/?domain=Verso.Genre.Manual.section&name=elan-override "Permalink")
Directory-specific [toolchain overrides](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#--tech-term-toolchain-override) are a local configuration that takes precedence over `lean-toolchain` files. The `elan override` commands manage overrides.
[🔗](find/?domain=Manual.elanCommand&name=override%20list "Permalink")Elan command
```
elan override list 
```

Lists all the currently configured directory overrides in two columns. The left column contains the directories in which the Lean version is overridden, and the right column lists the toolchain version.
[🔗](find/?domain=Manual.elanCommand&name=override%20set "Permalink")Elan command
```
elan override set toolchain
```

Sets `toolchain` as an override for the current directory.
[🔗](find/?domain=Manual.elanCommand&name=override%20unset "Permalink")Elan command
```
elan override unset [--nonexistent] [--path path]
```

If `--nonexistent` flag is provided, all overrides that are configured for directories that don't currently exist are removed. If `--path` is provided, then the override set for `path` is removed. Otherwise, the override for the current directory is removed.
###  24.2.3.5. Running Tools and Commands[🔗](find/?domain=Verso.Genre.Manual.section&name=elan-run "Permalink")
The commands in this section provide the ability to run a command in a specific toolchain and to locate a tool from a particular toolchain on disk. This can be useful when experimenting with different Lean versions, for cross-version testing, and for integrating Elan with other tools.
[🔗](find/?domain=Manual.elanCommand&name=run "Permalink")Elan command
```
elan run [--install] toolchain command ...
```

Configures an environment to use the given toolchain and then runs the specified program. The toolchain will be installed if the `--install` flag is provided. The command may be any program; it does not need to be a command that's part of a toolchain such as `lean` or `lake`. This can be used for testing arbitrary toolchains without setting an override.
[🔗](find/?domain=Manual.elanCommand&name=which "Permalink")Elan command
```
elan which command
```

Displays the full path to the toolchain-specific binary for `command`.
###  24.2.3.6. Managing Elan[🔗](find/?domain=Verso.Genre.Manual.section&name=elan-self "Permalink")
Elan can manage its own installation. It can upgrade itself, remove itself, and help configure tab completion for many popular shells.
[🔗](find/?domain=Manual.elanCommand&name=self%20update "Permalink")Elan command
```
elan self update 
```

Downloads and installs updates to Elan itself.
[🔗](find/?domain=Manual.elanCommand&name=self%20uninstall "Permalink")Elan command
```
elan self uninstall 
```

Uninstalls Elan.
[🔗](find/?domain=Manual.elanCommand&name=completions "Permalink")Elan command
```
elan completions shell
```

Generates shell completion scripts for Elan, enabling tab completion for Elan commands in a variety of shells. See the output of `elan help completions` for a description of how to install them.
[←24.1. Lake](Build-Tools-and-Distribution/Lake/#lake "24.1. Lake")[Validating a Lean Proof→](ValidatingProofs/#validating-proofs "Validating a Lean Proof")

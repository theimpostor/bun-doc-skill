# Installation
Source: https://bun.com/docs/installation

Install Bun with npm, Homebrew, Docker, or the official script.

## Overview

Bun ships as a single, dependency-free executable. You can install it via script, package manager, or Docker across macOS, Linux, and Windows.

> Tip: After installation, verify with `bun --version` and `bun --revision`.

## Installation

### macOS & Linux
**File:** `curl`
```bash
curl -fsSL https://bun.com/install | bash
```

> Note
**Linux users**  The `unzip` package is required to install Bun. Use `sudo apt install unzip` to install the unzip package. Kernel version 5.6 or higher is strongly recommended, but the minimum is 5.1. Use `uname -r` to check Kernel version.

### Windows
**File:** `PowerShell`
```powershell
powershell -c "irm bun.sh/install.ps1|iex"
```

> Warning
Bun requires Windows 10 version 1809 or later.

For support and discussion, please join the **#windows** channel on our [Discord](https://bun.com/discord).

### Package Managers
**File:** `npm`
```bash
npm install -g bun # the last `npm` command you'll ever need
```

**File:** `Homebrew`
```bash
brew install oven-sh/bun/bun
```

**File:** `Scoop`
```bash
scoop install bun
```

### Docker
Bun provides a Docker image that supports both Linux x64 and arm64.

**File:** `Docker`
```bash
docker pull oven/bun
docker run --rm --init --ulimit memlock=-1:-1 oven/bun
```

### Image Variants

There are also image variants for different operating systems:

**File:** `Docker`
```bash
docker pull oven/bun:debian
docker pull oven/bun:slim
docker pull oven/bun:distroless
docker pull oven/bun:alpine
```

To check that Bun was installed successfully, open a new terminal window and run:

```bash
bun --version
# Output: 1.x.y

# See the precise commit of `oven-sh/bun` that you're using
bun --revision
# Output: 1.x.y+b7982ac13189
```

> Warning
If you've installed Bun but are seeing a `command not found` error, you may have to manually add the installation
directory (`~/.bun/bin`) to your `PATH`.

### Add Bun to your PATH
### macOS & Linux
### Determine which shell you're using
```bash
echo $SHELL
# /bin/zsh  or /bin/bash or /bin/fish
```

### Open your shell configuration file
* For bash: `~/.bashrc`
* For zsh: `~/.zshrc`
* For fish: `~/.config/fish/config.fish`

### Add the Bun directory to PATH
Add this line to your configuration file:

```bash
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"
```

### Reload your shell configuration
```bash
source ~/.bashrc  # or ~/.zshrc
```

### Windows
### Determine if the bun binary is properly installed
```bash
& "$env:USERPROFILE\.bun\bin\bun" --version
```

If the command runs successfully but `bun --version` is not recognized, it means that bun is not in your system's PATH. To fix this, open a Powershell terminal and run the following command:

```bash
[System.Environment]::SetEnvironmentVariable(
  "Path",
  [System.Environment]::GetEnvironmentVariable("Path", "User") + ";$env:USERPROFILE\.bun\bin",
  [System.EnvironmentVariableTarget]::User
)
```

### Restart your terminal
After running the command, restart your terminal and test with `bun --version`

```bash
bun --version
```

***

## Upgrading

Once installed, the binary can upgrade itself:

```bash
bun upgrade
```

> Tip
**Homebrew users** <br>
To avoid conflicts with Homebrew, use `brew upgrade bun` instead.

**Scoop users** <br>
To avoid conflicts with Scoop, use `scoop update bun` instead.

***

## Canary Builds

[-> View canary build](https://github.com/oven-sh/bun/releases/tag/canary)

Bun automatically releases an (untested) canary build on every commit to main. To upgrade to the latest canary build:

```bash
# Upgrade to latest canary
bun upgrade --canary

# Switch back to stable
bun upgrade --stable
```

The canary build is useful for testing new features and bug fixes before they're released in a stable build. To help the Bun team fix bugs faster, canary builds automatically upload crash reports to Bun's team.

***

## Installing Older Versions

Since Bun is a single binary, you can install older versions by re-running the installer script with a specific version.

### Linux & macOS
To install a specific version, pass the git tag to the install script:

```bash
curl -fsSL https://bun.com/install | bash -s "bun-v1.3.3"
```

### Windows
On Windows, pass the version number to the PowerShell install script:

**File:** `PowerShell`
```powershell
iex "& {$(irm https://bun.com/install.ps1)} -Version 1.3.3"
```

***

## Direct Downloads

To download Bun binaries directly, visit the [releases page on GitHub](https://github.com/oven-sh/bun/releases).

### Latest Version Downloads

### Linux x64
Link: `https://github.com/oven-sh/bun/releases/latest/download/bun-linux-x64.zip`
Standard Linux x64 binary

### Linux x64 Baseline
Link: `https://github.com/oven-sh/bun/releases/latest/download/bun-linux-x64-baseline.zip`
For older CPUs without AVX2

### Windows x64
Link: `https://github.com/oven-sh/bun/releases/latest/download/bun-windows-x64.zip`
Standard Windows binary

### Windows x64 Baseline
Link: `https://github.com/oven-sh/bun/releases/latest/download/bun-windows-x64-baseline.zip`
For older CPUs without AVX2

### Windows ARM64
Link: `https://github.com/oven-sh/bun/releases/latest/download/bun-windows-aarch64.zip`
Windows on ARM (Snapdragon, etc.)

### macOS ARM64
Link: `https://github.com/oven-sh/bun/releases/latest/download/bun-darwin-aarch64.zip`
Apple Silicon (M1/M2/M3)

### macOS x64
Link: `https://github.com/oven-sh/bun/releases/latest/download/bun-darwin-x64.zip`
Intel Macs

### Linux ARM64
Link: `https://github.com/oven-sh/bun/releases/latest/download/bun-linux-aarch64.zip`
ARM64 Linux systems

### Musl Binaries

For distributions without `glibc` (Alpine Linux, Void Linux):

* [Linux x64 musl](https://github.com/oven-sh/bun/releases/latest/download/bun-linux-x64-musl.zip)
* [Linux x64 musl baseline](https://github.com/oven-sh/bun/releases/latest/download/bun-linux-x64-musl-baseline.zip)
* [Linux ARM64 musl](https://github.com/oven-sh/bun/releases/latest/download/bun-linux-aarch64-musl.zip)

> Note
If you encounter an error like `bun: /lib/x86_64-linux-gnu/libm.so.6: version GLIBC_2.29 not found`, try using the
musl binary. Bun's install script automatically chooses the correct binary for your system.

***

## CPU Requirements

Bun has specific CPU requirements based on the binary you're using:

### Standard Builds
**x64 binaries** target the Haswell CPU architecture (AVX and AVX2 instructions required)

| Platform | Intel Requirement               | AMD Requirement    |
| -------- | ------------------------------- | ------------------ |
| x64      | Haswell (4th gen Core) or newer | Excavator or newer |

### Baseline Builds
**x64-baseline binaries** target the Nehalem architecture for older CPUs

| Platform     | Intel Requirement               | AMD Requirement    |
| ------------ | ------------------------------- | ------------------ |
| x64-baseline | Nehalem (1st gen Core) or newer | Bulldozer or newer |

> Warning
Baseline builds are slower than regular builds. Use them only if you encounter an "Illegal
Instruction" error.

> Note
Bun does not support CPUs older than the baseline target, which mandates the SSE4.2 extension. macOS requires version
13.0 or later.

***

## Uninstall

To remove Bun from your system:

### macOS & Linux
```bash
rm -rf ~/.bun
```

### Windows
**File:** `PowerShell`
```powershell
powershell -c ~\.bun\uninstall.ps1
```

### Package Managers
**File:** `npm`
```bash
npm uninstall -g bun
```

**File:** `Homebrew`
```bash
brew uninstall bun
```

**File:** `Scoop`
```bash
scoop uninstall bun
```

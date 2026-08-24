# Upgrade Bun to the latest version
Source: https://bun.com/docs/guides/util/upgrade


Bun upgrades itself with the built-in `bun upgrade` command.

```bash
bun upgrade
```

`bun upgrade` downloads and installs the latest stable version of Bun, replacing the currently installed version. If you're on a canary build, `bun upgrade` installs the latest canary build instead.

> Note: To see the current version of Bun, run `bun --version`.

***

## Verify the upgrade

After upgrading, verify the new version:

```bash
bun --version
# Output: 1.x.y

# See the exact commit of the Bun binary
bun --revision
# Output: 1.x.y+abc123def
```

***

## Upgrade to canary builds

Canary builds are published automatically from the `main` branch once a commit's CI tests pass. They're useful for trying new features or verifying bug fixes before a release.

```bash
bun upgrade --canary
```

> Warning: Canary builds are not recommended for production use. They may contain bugs or breaking changes.

***

## Switch back to stable

If you're on a canary build and want to return to the latest stable release:

```bash
bun upgrade --stable
```

***

## Install a specific version

To install a specific version of Bun, use the install script with a version tag:

### macOS & Linux
```bash
curl -fsSL https://bun.sh/install | bash -s "bun-v1.3.3"
```

### Windows
**File:** `PowerShell`
```powershell
iex "& {$(irm https://bun.sh/install.ps1)} -Version 1.3.3"
```

***

## Package manager users

If you installed Bun with a package manager, upgrade with that package manager instead of `bun upgrade` to avoid conflicts.

> Tip
**Homebrew users** <br>
Use `brew upgrade bun` instead.

**Scoop users** <br>
Use `scoop update bun` instead.

***

## See also

* [Installation](/docs/installation) — Install Bun for the first time
* [Update packages](/docs/pm/cli/update) — Update dependencies to latest versions

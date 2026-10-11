# bun publish
Source: https://bun.com/docs/pm/cli/publish

Use `bun publish` to publish a package to the npm registry


`bun publish` packs your package into a tarball and strips catalog and workspace protocols from the `package.json`, resolving versions if necessary. It then publishes to the registry specified in your configuration files. Both `bunfig.toml` and `.npmrc` files are supported.

```sh
## Publishing the package from the current working directory
bun publish
```

```txt
bun publish v1.3.3 (ca7428e9)

packed 203B package.json
packed 224B README.md
packed 30B index.ts
packed 0.64KB tsconfig.json

Total files: 4
Shasum: 79e2b4377b63f4de38dc7ea6e5e9dbee08311a69
Integrity: sha512-6QSNlDdSwyG/+[...]X6wXHriDWr6fA==
Unpacked size: 1.1KB
Packed size: 0.76KB
Tag: latest
Access: default
Registry: http://localhost:4873/

 + publish-1@1.0.0
```

To pack and publish separately, run `bun pm pack`, then `bun publish` with the path to the output tarball.

```sh
bun pm pack
...
bun publish ./package.tgz
```

> Note
`bun publish` does not run lifecycle scripts (`prepublishOnly/prepack/prepare/postpack/publish/postpublish`) if you
provide a tarball path. Scripts run only when `bun publish` packs the package itself.

### `--access`

`--access` sets the access level of the package being published, either `public` or `restricted`. Unscoped packages are always public, and publishing an unscoped package with `--access restricted` is an error.

```sh
bun publish --access public
```

You can also set `--access` in the `publishConfig` field of your `package.json`.

**File:** `package.json`
```json
{
  "publishConfig": {
    "access": "restricted"
  }
}
```

### `--tag`

Set the tag of the package version being published. By default, the tag is `latest`. The initial version of a package is always given the `latest` tag in addition to the specified tag.

```sh
bun publish --tag alpha
```

You can also set `--tag` in the `publishConfig` field of your `package.json`.

**File:** `package.json`
```json
{
  "publishConfig": {
    "tag": "next"
  }
}
```

### `--dry-run`

`--dry-run` runs the publish process without publishing the package, so you can verify what would be published.

```sh
bun publish --dry-run
```

### `--tolerate-republish`

Exit with code 0 instead of 1 if the package version already exists. Useful in CI/CD where jobs may be re-run.

```sh
bun publish --tolerate-republish
```

### `--gzip-level`

Set the gzip compression level used when packing the package, from `0` to `9` (default `9`). Only applies to `bun publish` without a tarball path argument.

### `--auth-type`

If you have 2FA enabled for your npm account, `bun publish` prompts you for a one-time password, either through a browser or in the CLI. `--auth-type` tells the npm registry which method you prefer: `web` (the default) or `legacy`.

```sh
bun publish --auth-type legacy
...
This operation requires a one-time password.
Enter OTP: 123456
...
```

### `--otp`

Provide a one-time password directly to the CLI. If the password is valid, `bun publish` skips the extra one-time password prompt before publishing:

```sh
bun publish --otp 123456
```

> Note
`bun publish` respects the `NPM_CONFIG_TOKEN` environment variable, useful when publishing from GitHub Actions or
other automated workflows.

---

## CLI Usage

```bash
bun publish dist
```

### Publishing Options

### `--access`

Type: `string`
Set the access level of the package being published, either `public` or `restricted`. Unscoped packages are always public; publishing an unscoped package with `--access restricted` is an error.

```sh
bun publish --access public
```

You can also set `--access` in the `publishConfig` field of your `package.json`.

**File:** `package.json`
```json
{
  "publishConfig": {
    "access": "restricted"
  }
}
```


### `--tag`

Type: `string`; Default: `latest`
Set the tag of the package version being published. By default, the tag is `latest`. The initial version of a package is always given the `latest` tag in addition to the specified tag.

```sh
bun publish --tag alpha
```

You can also set `--tag` in the `publishConfig` field of your `package.json`.

**File:** `package.json`
```json
{
  "publishConfig": {
    "tag": "next"
  }
}
```


### `--dry-run`

Type: `boolean`
Simulate the publish process without publishing the package, to verify its contents first.

```sh
bun publish --dry-run
```


### `--tolerate-republish`

Type: `boolean`
`bun publish` exits with code 0 instead of 1 when the version being published already exists in the registry.

### `--gzip-level`

Type: `string`; Default: `9`
Specify the level of gzip compression to use when packing the package. Only applies to `bun publish` without a tarball
path argument. Values range from `0` to `9` (default is `9`).

### `--auth-type`

Type: `string`; Default: `web`

If you have 2FA enabled for your npm account, `bun publish` prompts you for a one-time password, either through a browser or the CLI. `--auth-type` tells the npm registry which method you prefer: `web` (the default) or `legacy`.

```sh
bun publish --auth-type legacy
...
This operation requires a one-time password.
Enter OTP: 123456
...
```


### `--otp`

Type: `string`

Provide a one-time password directly to the CLI. A valid password skips the extra one-time password prompt before publishing.

```sh
bun publish --otp 123456
```

> Note
`bun publish` respects the `NPM_CONFIG_TOKEN` environment variable, so you can publish from GitHub Actions or other
automated workflows.


### Registry Configuration

#### Custom Registry

### `--registry`

Type: `string`
Use a specific registry by default, overriding .npmrc, bunfig.toml and environment variables. A registry configured
for the package's scope (`@scope:registry=` in .npmrc or `[install.scopes]` in bunfig.toml) still takes precedence.

```bash
bun publish --registry https://my-private-registry.com
```

#### SSL Certificates

### `--ca`

Type: `string`
Provide Certificate Authority signing certificate

### `--cafile`

Type: `string`
Path to Certificate Authority certificate file

**File:** `Inline`
```bash
bun publish --ca "-----BEGIN CERTIFICATE-----..."
```

**File:** `Certificate`
```bash
bun publish --cafile ./ca-cert.pem
```


### General Options

#### Dependency Management

### `-p, --production`

Type: `boolean`
Don't install devDependencies

### `--omit`

Type: `string`
Exclude dependency types: `dev`, `optional`, or `peer`

### `-f, --force`

Type: `boolean`
Always request the latest versions from the registry & reinstall all dependencies

#### Script Control

### `--ignore-scripts`

Type: `boolean`
Skip lifecycle scripts during packing and publishing

### `--trust`

Type: `boolean`
Add packages to trustedDependencies and run their scripts

> Note
**Lifecycle Scripts** — When you publish a pre-built tarball, Bun does not run lifecycle scripts such as
`prepublishOnly` and `prepack`; they only run when Bun packs the package itself.

#### File Management

### `--no-save`

Type: `boolean`
Don't update package.json or lockfile

### `--frozen-lockfile`

Type: `boolean`
Disallow changes to lockfile

### `--yarn`

Type: `boolean`
Generate yarn.lock file (yarn v1 compatible)

#### Performance

### `--backend`

Type: `string`
Platform optimizations: `clonefile` (default on macOS), `hardlink` (default on Linux and Windows), `symlink`, or
`copyfile`

### `--network-concurrency`

Type: `number`; Default: `48`
Maximum concurrent network requests

### `--concurrent-scripts`

Type: `number`
Maximum concurrent lifecycle scripts (default: 2x CPU cores)

#### Output Control

### `--silent`

Type: `boolean`
Suppress all output

### `--verbose`

Type: `boolean`
Show detailed logging

### `--no-progress`

Type: `boolean`
Hide progress bar

### `--no-summary`

Type: `boolean`
Don't print publish summary

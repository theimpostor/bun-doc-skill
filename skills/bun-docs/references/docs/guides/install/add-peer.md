# Add a peer dependency
Source: https://bun.com/docs/guides/install/add-peer


To add an npm package as a peer dependency, use the `--peer` flag.

```sh
bun add @types/bun --peer
```

***

This adds the package to `peerDependencies` in `package.json`.

**File:** `package.json`
```json
{
  "peerDependencies": {
    "@types/bun": "^1.3.3"
  }
}
```

***

`bun install` installs peer dependencies by default, unless they are marked optional in `peerDependenciesMeta`.

**File:** `package.json`
```json
{
  "peerDependencies": {
    "@types/bun": "^1.3.3"
  },
  "peerDependenciesMeta": {
    "@types/bun": {
      "optional": true
    }
  }
}
```

***

See [`bun install`](/docs/pm/cli/install).

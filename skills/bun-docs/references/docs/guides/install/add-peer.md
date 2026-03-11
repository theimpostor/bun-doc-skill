# Add a peer dependency
Source: https://bun.com/docs/guides/install/add-peer


To add an npm package as a peer dependency, use the `--peer` flag.

```sh
bun add @types/bun --peer
```

***

This will add the package to `peerDependencies` in `package.json`.

**File:** `package.json`
```json
{
  "peerDependencies": {
    "@types/bun": "^1.3.3"
  }
}
```

***

Running `bun install` will install peer dependencies by default, unless marked optional in `peerDependenciesMeta`.

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

See [Docs > Package manager](/pm/cli/install) for complete documentation of Bun's package manager.

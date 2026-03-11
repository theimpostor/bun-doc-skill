# Add an optional dependency
Source: https://bun.com/docs/guides/install/add-optional


To add an npm package as an optional dependency, use the `--optional` flag.

```sh
bun add zod --optional
```

***

This will add the package to `optionalDependencies` in `package.json`.

**File:** `package.json`
```json
{
  "optionalDependencies": {
    "zod": "^3.0.0"
  }
}
```

***

See [Docs > Package manager](/pm/cli/install) for complete documentation of Bun's package manager.

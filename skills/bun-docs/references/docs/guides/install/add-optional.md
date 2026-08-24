# Add an optional dependency
Source: https://bun.com/docs/guides/install/add-optional


To add an npm package as an optional dependency, use the `--optional` flag.

```sh
bun add zod --optional
```

***

This adds the package to `optionalDependencies` in `package.json`.

**File:** `package.json`
```json
{
  "optionalDependencies": {
    "zod": "^4.0.0"
  }
}
```

***

See [`bun install`](/docs/pm/cli/install).

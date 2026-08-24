# Add a dependency
Source: https://bun.com/docs/guides/install/add


To add an npm package as a dependency, use `bun add`.

```sh
bun add zod
```

***

This adds the package to `dependencies` in `package.json`. By default, Bun uses the `^` range specifier, which accepts future minor and patch versions.

**File:** `package.json`
```json
{
  "dependencies": {
    "zod": "^4.0.0"
  }
}
```

***

To pin your project to the exact version you installed, use `--exact`. This adds the package to `dependencies` without the `^`.

```sh
bun add zod --exact
```

***

To specify an exact version or a tag:

```sh
bun add zod@3.0.0
bun add zod@next
```

***

See [`bun install`](/docs/pm/cli/install).

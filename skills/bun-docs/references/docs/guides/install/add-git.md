# Add a Git dependency
Source: https://bun.com/docs/guides/install/add-git


Bun supports directly adding GitHub repositories as dependencies of your project.

```sh
bun add github:lodash/lodash
```

***

This adds the following line to your `package.json`:

**File:** `package.json`
```json
{
  "dependencies": {
    "lodash": "github:lodash/lodash"
  }
}
```

***

Bun supports several protocols for specifying Git dependencies.

```sh
bun add git+https://github.com/lodash/lodash.git
bun add git+ssh://github.com/lodash/lodash.git#4.17.21
bun add git@github.com:lodash/lodash.git
bun add github:lodash/lodash#4.17.21
```

When possible, Bun downloads GitHub dependencies as HTTP tarballs, which is faster.

***

See [`bun install`](/docs/pm/cli/install).

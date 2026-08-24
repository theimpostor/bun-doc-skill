# Add a development dependency
Source: https://bun.com/docs/guides/install/add-dev


To add an npm package as a development dependency, use `bun add --development`.

```sh
bun add zod --dev
bun add zod -d # shorthand
```

***

This adds the package to `devDependencies` in `package.json`.

```json
{
  "devDependencies": {
    "zod": "^4.0.0"
  }
}
```

***

See [`bun install`](/docs/pm/cli/install).

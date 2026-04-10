# Read environment variables
Source: https://bun.com/docs/guides/runtime/read-env


The current environment variables can be accessed via `process.env`.

**File:** `index.ts`
```ts
process.env.API_TOKEN; // => "secret"
```

***

Bun also exposes these variables via `Bun.env`, which is an alias of `process.env`.

**File:** `index.ts`
```ts
Bun.env.API_TOKEN; // => "secret"
```

***

To print all currently-set environment variables to the command line, run `bun --print process.env`. This is useful for debugging.

```sh
bun --print process.env
```

```txt
BAZ=stuff
FOOBAR=aaaaaa
<lots more lines>
```

***

See [Docs > Runtime > Environment variables](/runtime/environment-variables) for more information on using environment variables with Bun.

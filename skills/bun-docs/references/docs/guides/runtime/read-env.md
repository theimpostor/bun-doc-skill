# Read environment variables
Source: https://bun.com/docs/guides/runtime/read-env


Access the current environment variables with `process.env`.

**File:** `index.ts`
```ts
process.env.API_TOKEN; // => "secret"
```

***

Bun also exposes these variables as `Bun.env`, an alias of `process.env`.

**File:** `index.ts`
```ts
Bun.env.API_TOKEN; // => "secret"
```

***

To print all currently-set environment variables, run `bun --print process.env`.

```sh
bun --print process.env
```

```txt
ProcessEnv {
  BAZ: "stuff",
  FOOBAR: "aaaaaa",
  <lots more lines>
}
```

***

See [Environment variables](/docs/runtime/environment-variables).

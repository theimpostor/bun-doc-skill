# Get the path to an executable bin file
Source: https://bun.com/docs/guides/util/which-path-to-executable-bin


`Bun.which` finds the absolute path of an executable file, like the `which` command on Unix-like systems.

**File:** `foo.ts`
```ts
Bun.which("sh"); // => "/bin/sh"
Bun.which("notfound"); // => null
Bun.which("bun"); // => "/home/user/.bun/bin/bun"
```

***

See [`Bun.which`](/docs/runtime/utils#bun-which).

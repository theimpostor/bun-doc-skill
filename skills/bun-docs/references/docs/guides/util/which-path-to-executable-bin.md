# Get the path to an executable bin file
Source: https://bun.com/docs/guides/util/which-path-to-executable-bin


`Bun.which` is a utility function to find the absolute path of an executable file. It is similar to the `which` command in Unix-like systems.

**File:** `foo.ts`
```ts
Bun.which("sh"); // => "/bin/sh"
Bun.which("notfound"); // => null
Bun.which("bun"); // => "/home/user/.bun/bin/bun"
```

***

See [Docs > API > Utils](/runtime/utils#bun-which) for complete documentation.

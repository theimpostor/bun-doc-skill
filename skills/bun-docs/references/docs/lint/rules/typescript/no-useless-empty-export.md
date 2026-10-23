# @typescript-eslint/no-useless-empty-export
Source: https://bun.com/docs/lint/rules/typescript/no-useless-empty-export

Disallow `export {}` in a file that is already a module


`export {}` exports nothing. Its only use is to turn a file without any `import` or `export` into a module, so that its top-level names stay out of the global scope. In a file that already has an `import` or another `export`, it does nothing.

`.d.ts` files aren't checked.

`--fix` removes the empty export.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-useless-empty-export" = "error" # or "warn"
```


## Examples

Reported:

```ts
export const port = 3000;
export {};
```

```ts
import { serve } from "bun";

serve({ fetch: () => new Response("ok") });

export {};
```

Not reported:

```ts
export const port = 3000;
```

Here `export {}` is what makes the file a module:

```ts
const port = 3000;
console.log(port);

export {};
```

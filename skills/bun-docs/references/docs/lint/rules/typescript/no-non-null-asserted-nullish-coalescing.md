# @typescript-eslint/no-non-null-asserted-nullish-coalescing
Source: https://bun.com/docs/lint/rules/typescript/no-non-null-asserted-nullish-coalescing

Disallow `!` on the left side of `??`


`??` gives a fallback for when the left side is `null` or `undefined`. A `!` on that side says it never is. If that's true, the fallback is dead code. If it isn't, the `!` is wrong. `??` handles both cases without it, so remove the `!`.

A `!` on the right side is allowed.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-non-null-asserted-nullish-coalescing" = "error"
```


## Examples

Reported:

```ts
declare const settings: { theme?: string };
declare function findUser(id: string): { name: string } | null;

const theme = settings.theme! ?? "light";
const user = findUser("42")! ?? { name: "guest" };
```

Not reported:

```ts
declare const settings: { theme?: string };
declare function findUser(id: string): { name: string } | null;

const theme = settings.theme ?? "light";
const user = findUser("42") ?? { name: "guest" };
```

Here the `!` is what lets you read `label` before it's assigned, so it's allowed:

```ts
let label: string;

const text = label! ?? "untitled";
```

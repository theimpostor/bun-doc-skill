# @typescript-eslint/no-unsafe-return
Source: https://bun.com/docs/lint/rules/typescript/no-unsafe-return

Disallow returning a value of type `any` from a function


A function that returns `any` hands it to every caller. TypeScript stops checking whatever they do with the result, and nothing at the call site tells you.

The rule reports a returned `any` or `any[]`, a `Promise<any>` returned from an `async` function, and an `any` inside a generic type, such as a `Set<any>` returned as a `Set<string>`.

`bun lint --type-aware` turns this rule on in TypeScript files.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unsafe-return" = "error" # or "warn"
```


## Examples

Reported:

```ts
function loadConfig(text: string) {
  return JSON.parse(text);
}
```

```ts
async function fetchUser(url: string) {
  const response = await fetch(url);
  return response.json();
}
```

```ts
function uniqueNames(): Set<string> {
  return new Set<any>();
}
```

Not reported:

```ts
interface Config {
  port: number;
}

function loadConfig(text: string) {
  return JSON.parse(text) as Config;
}
```

A function with the return type `unknown` can return `any`, because callers need to check the value before they use it. A return type of `any` that you wrote yourself is allowed too:

```ts
function parse(text: string): unknown {
  return JSON.parse(text);
}

function parseUnchecked(text: string): any {
  return JSON.parse(text);
}
```

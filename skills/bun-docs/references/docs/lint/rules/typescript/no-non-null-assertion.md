# @typescript-eslint/no-non-null-assertion
Source: https://bun.com/docs/lint/rules/typescript/no-non-null-assertion

Disallow the non-null assertion `value!`


`value!` tells TypeScript that `value` isn't `null` or `undefined`. Nothing checks that when the code runs. If you're wrong, or the code around it changes, `value!.name` throws a `TypeError`, which is the error strict null checks are meant to prevent.

Check the value, or use `?.` or `??`, which do their work at runtime.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-non-null-assertion" = "error" # or "warn"
```


## Examples

Reported:

```ts
const users = new Map<string, { name: string }>();

function greet(id: string) {
  const form = document.querySelector("form")!;
  form.title = users.get(id)!.name;
}
```

Not reported:

```ts
const users = new Map<string, { name: string }>();

function greet(id: string) {
  const form = document.querySelector("form");
  if (!form) {
    throw new Error("The page has no form");
  }
  form.title = users.get(id)?.name ?? "guest";
}
```

## When not to use it

Sometimes you know more than the type checker, for example right after `map.has(key)`. If your code has many places like that and you trust them, this rule is noise.

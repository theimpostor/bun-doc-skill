# @typescript-eslint/no-extra-non-null-assertion
Source: https://bun.com/docs/lint/rules/typescript/no-extra-non-null-assertion

Disallow a non-null assertion that has no effect


`!` after an expression tells TypeScript that the value isn't `null` or `undefined`. Writing it twice, as in `user!!`, doesn't add anything. Writing it right before `?.` contradicts itself, because `user!?.name` first claims that `user` is there and then checks whether it is.

`--fix` removes the extra `!`.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-extra-non-null-assertion" = "off" # or "error"
```


## Examples

Reported:

```ts
function nameOf(user?: { name: string }) {
  return user!!.name;
}

function lengthOf(items?: string[]) {
  return items!?.length;
}
```

Not reported:

```ts
function nameOf(user?: { name: string }) {
  return user!.name;
}

function lengthOf(items?: string[]) {
  return items?.length;
}
```

# @typescript-eslint/non-nullable-type-assertion-style
Source: https://bun.com/docs/lint/rules/typescript/non-nullable-type-assertion-style

Require `value!` instead of `value as T` when the assertion only removes `null` and `undefined`


If `name` is a `string | undefined`, then `name as string` and `name!` do the same thing. The `!` is shorter, and it says exactly what you're claiming, which is that the value is there. It also doesn't repeat the type, so there's nothing to update when the type changes.

`--fix` rewrites the assertion to `!`.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/non-nullable-type-assertion-style" = "error" # or "warn"
```


## Examples

Reported:

```ts
function nameOf(names: Map<string, string>, id: string) {
  return names.get(id) as string;
}
```

Not reported:

```ts
function nameOf(names: Map<string, string>, id: string) {
  return names.get(id)!;
}
```

An assertion that does more than remove `null` and `undefined` can't be written with `!`, so it's allowed:

```ts
function toText(value: string | number | null) {
  return value as string;
}
```

## When not to use it

`@typescript-eslint/no-non-null-assertion` reports every `!`. Don't turn on both.

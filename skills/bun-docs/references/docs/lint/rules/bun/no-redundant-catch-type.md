# bun/no-redundant-catch-type
Source: https://bun.com/docs/lint/rules/bun/no-redundant-catch-type

Disallow `: unknown` on the variable of a `catch` clause


With `strict` or `useUnknownInCatchVariables` in `tsconfig.json`, a `catch` clause's variable is already `unknown`. Writing `: unknown` adds nothing.

`--fix` removes the annotation.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/no-redundant-catch-type" = "error" # or "warn"
```


## Examples

Reported:

```ts
try {
  await save(draft);
} catch (error: unknown) {
  report(error);
}
```

Not reported:

```ts
try {
  await save(draft);
} catch (error) {
  report(error);
}
```

## When not to use it

The rule doesn't read your `tsconfig.json`. Without `strict` or `useUnknownInCatchVariables`, the variable is `any`, and `: unknown` is what makes it safe. Leave the rule off in a project like that.

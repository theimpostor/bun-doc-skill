# @typescript-eslint/no-unnecessary-boolean-literal-compare
Source: https://bun.com/docs/lint/rules/typescript/no-unnecessary-boolean-literal-compare

Disallow comparing a boolean with `true` or `false`


If a value is a `boolean`, `value === true` is the same as `value`, and `value === false` is the same as `!value`. The comparison adds nothing.

A `boolean | undefined` is allowed by default, because there `=== true` also decides what happens with `undefined`. A `boolean | string` is never reported.

`--fix` replaces the comparison with the value or its negation.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unnecessary-boolean-literal-compare" = "error"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unnecessary-boolean-literal-compare" = ["error", {
  allowComparingNullableBooleansToTrue = true,
  allowComparingNullableBooleansToFalse = true,
  allowRuleToRunWithoutStrictNullChecksIKnowWhatIAmDoing = false,
}]
```


## Examples

Reported:

```ts
function canEdit(isOwner: boolean, isLocked: boolean) {
  return isOwner === true && isLocked === false;
}
```

Not reported:

```ts
function canEdit(isOwner: boolean, isLocked: boolean) {
  return isOwner && !isLocked;
}

function isPinned(pinned?: boolean, mode?: boolean | string) {
  return pinned === true || mode === true;
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowComparingNullableBooleansToTrue` | `true` | Allow `value === true` where `value` can also be `null` or `undefined`. |
| `allowComparingNullableBooleansToFalse` | `true` | Allow `value === false` where `value` can also be `null` or `undefined`. |
| `allowRuleToRunWithoutStrictNullChecksIKnowWhatIAmDoing` | `false` | Without `strictNullChecks` in `tsconfig.json`, the rule can't tell what can be `null`, and it reports that once for each file. Set this to `true` to turn that report off. |

With `allowComparingNullableBooleansToTrue` off, write `if (isPinned)` instead:

```ts
function pin(isPinned?: boolean) {
  if (isPinned === true) {
    console.log("pinned");
  }
}
```

With `allowComparingNullableBooleansToFalse` off, write `!(isPinned ?? true)` instead, which says what `undefined` counts as:

```ts
function pin(isPinned?: boolean) {
  if (isPinned === false) {
    console.log("not pinned");
  }
}
```

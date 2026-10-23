# @typescript-eslint/prefer-reduce-type-parameter
Source: https://bun.com/docs/lint/rules/typescript/prefer-reduce-type-parameter

Require a type argument on `reduce` instead of a type assertion on the initial value


`reduce` takes its result type from the initial value, and `{}` or `[]` alone gives you a type that's too narrow. `{} as Record<string, number>` fixes that, but an assertion also accepts a value that doesn't fit the type. `reduce<Record<string, number>>(..., {})` gives you the same result type, and TypeScript still checks the initial value against it.

Only arrays and tuples are checked. If the value can't be assigned to the asserted type, you need the assertion and the call is left alone.

`--fix` moves the type from the assertion to the call.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/prefer-reduce-type-parameter" = "error" # or "warn"
```


## Examples

Reported:

```ts
function count(words: string[]) {
  return words.reduce((counts, word) => {
    counts[word] = (counts[word] ?? 0) + 1;
    return counts;
  }, {} as Record<string, number>);
}

function lengths(words: string[]) {
  return words.reduce((result, word) => result.concat(word.length), [] as number[]);
}
```

Not reported:

```ts
function count(words: string[]) {
  return words.reduce<Record<string, number>>((counts, word) => {
    counts[word] = (counts[word] ?? 0) + 1;
    return counts;
  }, {});
}

function lengths(words: string[]) {
  return words.reduce<number[]>((result, word) => result.concat(word.length), []);
}
```

Here `{}` isn't a valid `Summary`, so moving the type would be a type error:

```ts
interface Summary {
  longest: string;
}

function summarize(words: string[]) {
  return words.reduce((summary, word) => {
    summary.longest = word;
    return summary;
  }, {} as Summary);
}
```

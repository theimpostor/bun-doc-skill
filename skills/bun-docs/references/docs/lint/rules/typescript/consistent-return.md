# @typescript-eslint/consistent-return
Source: https://bun.com/docs/lint/rules/typescript/consistent-return

Require every `return` in a function to return a value, or none of them


A function that returns a value on one path and nothing on another gives its caller `undefined` some of the time. Often that's a path someone forgot.

This is `consistent-return` with types. A function with the return type `void`, or an async function that returns `Promise<void>`, can mix `return;` with `return value;`.

With `bunfig.toml`, turning this rule on runs it in TypeScript files and `consistent-return` in JavaScript files, so nothing is reported twice. With an ESLint config, turn the other rule off when you use this one.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/consistent-return" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/consistent-return" = ["error", {
  treatUndefinedAsUnspecified = false,
}]
```


## Examples

Reported:

```ts
function findUser(id: number) {
  if (id < 0) {
    return;
  }
  return { id };
}
```

The end of the function counts as a `return` without a value:

```ts
function label(count: number) {
  if (count > 0) {
    return `${count} items`;
  }
}
```

Not reported:

```ts
function findUser(id: number) {
  if (id < 0) {
    return undefined;
  }
  return { id };
}
```

```ts
function log(message: string): void {
  if (!message) {
    return;
  }
  return console.log(message);
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `treatUndefinedAsUnspecified` | `false` | Treat `return undefined`, and the return of any expression of type `undefined`, like `return;`. |

```ts
function findUser(id: number) {
  if (id < 0) {
    return undefined;
  }
  return { id };
}
```

## When not to use it

TypeScript's `noImplicitReturns` option catches the forgotten path too. If it's on, you may not need this rule.

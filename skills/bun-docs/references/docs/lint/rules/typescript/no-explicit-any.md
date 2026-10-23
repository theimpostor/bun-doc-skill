# @typescript-eslint/no-explicit-any
Source: https://bun.com/docs/lint/rules/typescript/no-explicit-any

Disallow the `any` type


`any` turns type checking off for a value, and for everything computed from it. You can call it, read any property of it and pass it anywhere, and a typo only shows up when the code runs. `unknown` also accepts every value, but you have to narrow it before you use it.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-explicit-any" = "off" # or "error"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-explicit-any" = ["warn", {
  fixToUnknown = false,
  ignoreRestArgs = false,
}]
```


## Examples

Reported:

```ts
function parse(text: string): any {
  return JSON.parse(text);
}

parse("{}").user.nmae; // no type error
```

Not reported:

```ts
function parse(text: string): unknown {
  return JSON.parse(text);
}

const result = parse("{}");
if (typeof result === "string") {
  console.log(result.length);
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `fixToUnknown` | `false` | Let `--fix` rewrite `any` to `unknown`, and `keyof any` to `PropertyKey`. The code may stop compiling until you narrow the values. |
| `ignoreRestArgs` | `false` | Allow `any[]`, `Array<any>` and their `readonly` forms as the type of a rest parameter. |

```ts
function log(...args: any[]) {
  console.log(...args);
}
```

Every other `any` is still reported:

```ts
function log(message: any) {
  console.log(message);
}
```

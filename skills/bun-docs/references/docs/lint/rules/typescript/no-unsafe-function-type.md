# @typescript-eslint/no-unsafe-function-type
Source: https://bun.com/docs/lint/rules/typescript/no-unsafe-function-type

Disallow the built-in `Function` type


You can call a value of type `Function` with any arguments, and the result is `any`, so TypeScript checks nothing about the call. `Function` also accepts classes, which throw when you call them without `new`.

Write the parameters and the return type instead.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unsafe-function-type" = "off" # or "error"
```


## Examples

Reported:

```ts
function onChange(listener: Function) {
  listener("name", 1, 2, 3);
}
```

Not reported:

```ts
function onChange(listener: (field: string) => void) {
  listener("name");
}
```

An interface that extends `Function` is reported too:

```ts
interface Handler extends Function {
  priority: number;
}
```

To accept any function at all, use a signature that every function matches:

```ts
function nameOf(task: (...args: never[]) => unknown) {
  return task.name;
}
```

Your own type named `Function` isn't reported:

```ts
import type { Function } from "./ast";

export function visit(node: Function) {}
```

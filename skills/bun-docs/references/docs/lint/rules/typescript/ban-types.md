# @typescript-eslint/ban-types
Source: https://bun.com/docs/lint/rules/typescript/ban-types

Disallow `String`, `Number`, `Object`, `Function`, `{}` and similar types


Some built-in types don't mean what they look like:

- `String`, `Number`, `Boolean`, `Symbol`, and `BigInt` are the wrapper objects. You almost always want the lowercase `string`, `number`, `boolean`, `symbol`, or `bigint`.
- `Function` accepts any function, and calling it returns `any`, so arguments and results aren't checked.
- `Object` and `{}` accept every value except `null` and `undefined`, including `0` and `""`.

Names that a class `implements` or an interface `extends` aren't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/ban-types" = "error" # or "warn"
```


## Examples

Reported:

```ts
function greet(name: String, onDone: Function) {
  onDone(`Hello, ${name}`);
}
```

```ts
let settings: {} = 0;
let extra: Object = "";
```

Not reported:

```ts
function greet(name: string, onDone: (message: string) => void) {
  onDone(`Hello, ${name}`);
}

let settings: Record<string, unknown> = {};
let extra: object = {};

interface Handler extends Function {
  priority: number;
}
```

## When not to use it

Three newer rules split up the same checks, so you can turn each one on separately: `@typescript-eslint/no-wrapper-object-types`, `@typescript-eslint/no-unsafe-function-type`, and `@typescript-eslint/no-empty-object-type`.

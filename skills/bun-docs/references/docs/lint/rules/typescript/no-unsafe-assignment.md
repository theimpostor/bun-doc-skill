# @typescript-eslint/no-unsafe-assignment
Source: https://bun.com/docs/lint/rules/typescript/no-unsafe-assignment

Disallow assigning a value of type `any` to a variable or a property


When you assign an `any` to a variable, the variable becomes `any` too, or it claims a type that nobody checked. From there, every property read, call and argument goes unchecked as well, far from where the `any` came in.

The rule checks variable declarations, assignments, default values, class properties, object properties, JSX attributes, destructuring and array spreads. It also reports `any` inside a generic type, such as a `Set<any>` assigned to a `Set<string>`.

`bun lint --type-aware` turns this rule on in TypeScript files.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unsafe-assignment" = "error" # or "warn"
```


## Examples

Reported:

```ts
const config = JSON.parse("{}");
const port: number = JSON.parse("8080");
const { host } = JSON.parse("{}") as { host: any };
const tags: Set<string> = new Set<any>();
```

Not reported:

```ts
interface Config {
  host: string;
  port: number;
}

const config = JSON.parse("{}") as Config;
const { host } = config;
const tags: Set<string> = new Set<string>();
```

Assigning an `any` to something declared as `unknown` is allowed. That's the safe way to receive a value you know nothing about:

```ts
const data: unknown = JSON.parse("{}");

if (typeof data === "string") {
  console.log(data.length);
}
```

## When not to use it

In a codebase that's still moving from JavaScript to TypeScript, `any` is everywhere and the reports drown out everything else. Turn the rule on once most values have real types.

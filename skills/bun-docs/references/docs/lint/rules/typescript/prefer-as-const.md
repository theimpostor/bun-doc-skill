# @typescript-eslint/prefer-as-const
Source: https://bun.com/docs/lint/rules/typescript/prefer-as-const

Require `as const` instead of repeating a literal as its own type


`"dark" as "dark"` and `let theme: "dark" = "dark"` write the same literal twice, and you need to change both every time. `as const` gives you the same narrow type and takes it from the value.

The rule checks every `as` assertion, and the type annotations on variables and class fields. It only reports a type that's the same literal as the value.

`--fix` rewrites `"dark" as "dark"` to `"dark" as const`. A type annotation is reported but not fixed.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/prefer-as-const" = "off" # or "error"
```


## Examples

Reported:

```ts
let theme = "dark" as "dark";
let retries: 3 = 3;

class Request {
  method: "GET" = "GET";
}
```

Not reported:

```ts
let theme = "dark" as const;
let retries = 3 as const;

class Request {
  method = "GET" as const;
}

let mode: "dark" | "light" = "dark";
let size = "small" as "small" | "large";
```

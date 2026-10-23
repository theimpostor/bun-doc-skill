# no-unassigned-vars
Source: https://bun.com/docs/lint/rules/eslint/no-unassigned-vars

Disallow `let` and `var` variables that are read but never assigned


A `let` or `var` that's declared without a value and never assigned is `undefined` everywhere you read it. Usually someone forgot the assignment, or a refactor removed it.

`no-unused-vars` handles variables that are never read.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-unassigned-vars" = "off" # or "error"
```


## Examples

Reported:

```js
let status;

if (status === "ready") {
  start();
}
```

Not reported:

```js
let status;

if (isReady()) {
  status = "ready";
}

if (status === "ready") {
  start();
}
```

In TypeScript, `declare` says that the value comes from somewhere else:

```ts
declare let version: string;

console.log(version);
```

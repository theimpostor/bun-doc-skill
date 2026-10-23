# no-const-assign
Source: https://bun.com/docs/lint/rules/eslint/no-const-assign

Disallow reassigning `const`, `using` and `await using` variables


Assigning to a variable declared with `const`, `using` or `await using` throws a `TypeError` when that line runs. The rule catches it earlier, including in branches your tests never reach.

`=`, compound assignments such as `+=`, `++` and `--` all count.

This rule is on by default in JavaScript files. It's off in TypeScript files, where TypeScript reports the same mistake.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-const-assign" = "off" # or "warn"
```


## Examples

Reported:

```js
const retries = 0;

function onFailure() {
  retries += 1;
}

function reset() {
  retries = 0;
}
```

Not reported:

```js
let retries = 0;

function onFailure() {
  retries += 1;
}
```

`const` protects the variable, not the value it holds. Changing a property is fine:

```js
const settings = { theme: "light" };
settings.theme = "dark";
```

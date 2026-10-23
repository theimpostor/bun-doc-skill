# bun/no-useless-spread-fallback
Source: https://bun.com/docs/lint/rules/bun/no-useless-spread-fallback

Disallow an empty object as the fallback in `...(condition ? value : {})`


Spreading `false`, `null` or `undefined` into an object does nothing. So the `{}` in `...(condition ? { a } : {})` isn't needed, and `...(condition && { a })` does the same thing with less code.

The rule checks spreads in object literals and in JSX attributes.

`--fix-suggestions` rewrites `condition ? value : {}` to `condition && value`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/no-useless-spread-fallback" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun/no-useless-spread-fallback" = ["error", {
  ignoreConditionsThatCall = [], # list of strings
}]
```


## Examples

Reported:

```js
const headers = {
  accept: "application/json",
  ...(apiKey ? { "x-api-key": apiKey } : {}),
};
```

```jsx
const link = <a href={url} {...(external ? { target: "_blank" } : {})}>{label}</a>;
```

Not reported:

```js
const headers = {
  accept: "application/json",
  ...(apiKey && { "x-api-key": apiKey }),
};
```

An empty object in the first branch is reported too, without a suggestion:

```js
const query = { page, ...(showAll ? {} : { limit: 20 }) };
```

```js
const query = { page, ...(!showAll && { limit: 20 }) };
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreConditionsThatCall` | `[]` | Names of functions. A conditional isn't reported if its condition calls one of them. |

Use it for a function that a build tool only understands as the condition of `? :`, such as a feature flag:

```js
const routes = {
  home,
  ...(feature("ADMIN") ? { admin } : {}),
};
```

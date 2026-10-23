# no-unreachable-loop
Source: https://bun.com/docs/lint/rules/eslint/no-unreachable-loop

Disallow loops with a body that can only run once


If every path through a loop's body ends in `break`, `return`, or `throw`, the loop never gets to a second pass. Usually a condition is missing around the exit, or you meant `continue`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-unreachable-loop" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-unreachable-loop" = ["error", {
  ignore = [], # list of strings
}]
```


## Examples

Reported. The loop only ever looks at the first result:

```js
function firstError(results) {
  for (const result of results) {
    if (result.ok) {
      return null;
    } else {
      return result.error;
    }
  }
}
```

Not reported:

```js
function firstError(results) {
  for (const result of results) {
    if (!result.ok) {
      return result.error;
    }
  }
  return null;
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignore` | `[]` | Kinds of loops to skip: `"WhileStatement"`, `"DoWhileStatement"`, `"ForStatement"`, `"ForInStatement"`, `"ForOfStatement"`. |

A `for...of` loop that returns right away is a short way to get an iterable's first item. By default it's reported:

```js
function first(items) {
  for (const item of items) {
    return item;
  }
}
```

```js
function first(items) {
  for (const item of items) {
    return item;
  }
}
```

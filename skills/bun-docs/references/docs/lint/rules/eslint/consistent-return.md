# consistent-return
Source: https://bun.com/docs/lint/rules/eslint/consistent-return

Require every `return` in a function to have a value, or none of them


A function that returns a value on one path and nothing on another sometimes gives its caller `undefined`. That can be on purpose, but often someone forgot a value, or the function runs off the end by accident.

The function's first `return` sets the expectation. Every `return` that differs from it is reported, and so is a function that returns a value but can also run off the end.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"consistent-return" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"consistent-return" = ["error", {
  treatUndefinedAsUnspecified = false,
}]
```


## Examples

Reported:

```js
function findUser(id) {
  if (!id) {
    return;
  }
  return users.get(id);
}
```

```js
function discount(order) {
  if (order.total > 100) {
    return 10;
  }
}
```

Not reported:

```js
function findUser(id) {
  if (!id) {
    return undefined;
  }
  return users.get(id);
}

function discount(order) {
  if (order.total > 100) {
    return 10;
  }
  return 0;
}

function log(message) {
  if (!enabled) {
    return;
  }
  console.log(message);
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `treatUndefinedAsUnspecified` | `false` | Treat `return undefined;` and `return void 0;` the same as `return;`. |

```js
function findUser(id) {
  if (!id) {
    return undefined;
  }
  return users.get(id);
}
```

## When not to use it

In TypeScript, the compiler option `noImplicitReturns` finds the same mistakes and knows the function's return type.

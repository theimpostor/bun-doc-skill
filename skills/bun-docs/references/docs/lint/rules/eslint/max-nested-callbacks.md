# max-nested-callbacks
Source: https://bun.com/docs/lint/rules/eslint/max-nested-callbacks

Enforce a maximum depth that callbacks can be nested


Callbacks inside callbacks push the code to the right, and each level needs its own error handling. This rule reports any callback nested deeper than the maximum, which is 10 by default.

A callback is a function expression or an arrow function that's passed as an argument to a call.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"max-nested-callbacks" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"max-nested-callbacks" = ["error", {
  max = 10,
  checkConstructorCallCallbacks = false,
  # maximum = <number>,
}]
```


## Examples

With a maximum of 2, the third callback is reported:

```js
readConfig((config) => {
  connect(config, (db) => {
    db.query("select 1", (rows) => {
      console.log(rows);
    });
  });
});
```

Not reported:

```js
const config = await readConfig();
const db = await connect(config);
const rows = await db.query("select 1");
console.log(rows);
```

## Options

**File:** `bunfig.toml`
```toml
[lint.rules]
max-nested-callbacks = ["error", 3]
```

| Option | Default | What it does |
| --- | --- | --- |
| `max` | `10` | The deepest level allowed. `maximum` is an older name for it. |
| `checkConstructorCallCallbacks` | `false` | Also count a function passed to `new`, as in `new Promise(() => {})`. |

A number alone is short for `{ "max": number }`.

By default the function passed to `new Promise` doesn't count as a level:

```js
button.addEventListener("click", () => {
  return new Promise((resolve) => {
    setTimeout(resolve, 100);
  });
});
```

With `checkConstructorCallCallbacks` it's the second level:

```js
button.addEventListener("click", () => {
  return new Promise((resolve) => {
    setTimeout(resolve, 100);
  });
});
```

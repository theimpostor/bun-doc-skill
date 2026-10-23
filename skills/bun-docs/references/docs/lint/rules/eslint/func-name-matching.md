# func-name-matching
Source: https://bun.com/docs/lint/rules/eslint/func-name-matching

Require a function expression's name to match the variable or property it is assigned to


A function expression can have a name that's different from the variable or property that holds it. Stack traces then show one name while the rest of the code calls the other, so if you search for the name from the trace, you won't find any callers.

Only named function expressions are checked. Arrow functions and `function () {}` are never reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"func-name-matching" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"func-name-matching" = [
  "error",
  "always", # "always" or "never"
  {
    considerPropertyDescriptor = false,
    includeCommonJSModuleExports = false,
  },
]
```


## Examples

Reported:

```js
const loadUser = function fetchUser(id) {
  return db.users.get(id);
};

api.remove = function destroy(id) {};

const handlers = {
  onSave: function save() {},
};
```

Not reported:

```js
const loadUser = function loadUser(id) {
  return db.users.get(id);
};

api.remove = function remove(id) {};

const handlers = {
  onSave: function onSave() {},
  onClose: function () {},
};
```

## Options

**File:** `bunfig.toml`
```toml
[lint.rules]
func-name-matching = ["error", "always", { considerPropertyDescriptor = true }]
```

The first option is a string. You can leave it out and pass only the object.

| Option | What it does |
| --- | --- |
| `"always"` (default) | The two names must be the same. |
| `"never"` | The two names must be different. |

| Option | Default | What it does |
| --- | --- | --- |
| `considerPropertyDescriptor` | `false` | In a property descriptor, compare the `value` function's name with the property being defined. |
| `includeCommonJSModuleExports` | `false` | Also check `module.exports = function name() {}`. The property is `exports`, so that's the name it's compared with. |

```js
const loadUser = function loadUser(id) {};
```

### `considerPropertyDescriptor`

This applies to `Object.defineProperty`, `Reflect.defineProperty`, `Object.defineProperties` and `Object.create`. Without the option, the function below is compared with its key, `value`, and reported:

```js
Object.defineProperty(user, "save", {
  value: function save() {},
});
```

```js
Object.defineProperty(user, "save", {
  value: function save() {},
});
```

### `includeCommonJSModuleExports`

```js
module.exports = function createServer() {};
```

```js
module.exports = function createServer() {};
```

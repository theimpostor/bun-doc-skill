# no-param-reassign
Source: https://bun.com/docs/lint/rules/eslint/no-param-reassign

Disallow assigning to function parameters


After `price = price * 1.2`, the name `price` no longer holds what the caller passed, and anyone reading further down the function has to notice that. In a function that isn't in strict mode, the assignment also changes `arguments[0]`.

Use a new variable for the new value.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-param-reassign" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-param-reassign" = ["error", {
  props = false,
  # ignorePropertyModificationsFor = [], # list of strings
  # ignorePropertyModificationsForRegex = [], # list of strings
}]
```


## Examples

Reported:

```js
function total(price, count) {
  price = price * 1.2;
  count++;
  return price * count;
}
```

Not reported:

```js
function total(price, count) {
  const withTax = price * 1.2;
  return withTax * (count + 1);
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `props` | `false` | Also report a change to a parameter's property: an assignment, `++`, `--`, `delete`, or use as the variable of a `for...in` or `for...of` loop. |
| `ignorePropertyModificationsFor` | `[]` | With `props`: names of parameters whose properties can be changed. |
| `ignorePropertyModificationsForRegex` | `[]` | With `props`: the same, as regular expressions. |

By default, changing a property is allowed:

```js
function activate(user) {
  user.active = true;
}
```

With `{ props: true }`, it's reported, because the caller's object changes:

```js
function activate(user) {
  user.active = true;
  delete user.pending;
}
```

The two lists make exceptions for parameters that exist to be changed. With `{ props: true, ignorePropertyModificationsFor: ["res"], ignorePropertyModificationsForRegex: ["^draft"] }`:

```js
function notFound(req, res) {
  res.statusCode = 404;
}

function rename(draftUser, name) {
  draftUser.name = name;
}
```

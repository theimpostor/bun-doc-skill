# max-classes-per-file
Source: https://bun.com/docs/lint/rules/eslint/max-classes-per-file

Enforce a maximum number of classes per file


When a file holds several classes, its name can only describe one of them, and the others are hard to find.

Class declarations and class expressions both count. The default maximum is 1.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"max-classes-per-file" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"max-classes-per-file" = ["error", {
  max = 1,
  ignoreExpressions = false,
}]
```


## Examples

Reported:

```js
class User {}

class Session {}
```

Not reported:

```js
class User {}
```

## Options

**File:** `bunfig.toml`
```toml
[lint.rules]
max-classes-per-file = ["error", { max = 2, ignoreExpressions = true }]
```

The option is either a number (the maximum) or an object:

| Option | Default | What it does |
| --- | --- | --- |
| `max` | `1` | The number of classes a file can have. |
| `ignoreExpressions` | `false` | Don't count class expressions. |

```js
class User {}

class Session {}
```

```js
class User {}

class Session {}

class Token {}
```

### `ignoreExpressions`

```js
class User {}

const Guest = class extends User {};
```

```js
class User {}

const Guest = class extends User {};
```

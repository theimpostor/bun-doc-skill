# logical-assignment-operators
Source: https://bun.com/docs/lint/rules/eslint/logical-assignment-operators

Require or disallow the logical assignment operators `||=`, `&&=` and `??=`


`options = options || {}` names the variable twice, and it assigns even when `options` keeps its value. `options ||= {}` says the same thing with one name and only assigns when it needs to.

`--fix` rewrites the code when the target is a plain variable. A property can have a getter or a setter, and the rewrite can change how often they run, so `user.name = user.name || "guest"` gets a suggestion instead of a fix.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"logical-assignment-operators" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"logical-assignment-operators" = [
  "error",
  "always", # "always" or "never"
  {
    enforceForIfStatements = false,
  },
]
```


## Examples

Reported:

```js
options = options || {};
cache = cache ?? new Map();
enabled = enabled && isReady();
title || (title = "Untitled");
user.name = user.name || "guest";
```

Not reported:

```js
options ||= {};
cache ??= new Map();
enabled &&= isReady();
title ||= "Untitled";
user.name ||= "guest";
```

## Options

**File:** `bunfig.toml`
```toml
[lint.rules]
logical-assignment-operators = ["error", "always", {
  enforceForIfStatements = true,
}]
```

| Option | What it does |
| --- | --- |
| `"always"` (default) | Report code that could use a logical assignment operator. |
| `"never"` | Report every logical assignment operator. |

| Option | Default | What it does |
| --- | --- | --- |
| `enforceForIfStatements` | `false` | With `"always"`, also report an `if` that only assigns to the value it tests. |

```js
options ||= {};
```

```js
options = options || {};
```

### `enforceForIfStatements`

```js
if (!title) {
  title = "Untitled";
}

if (cache == null) cache = new Map();
```

```js
if (!title) {
  title = "Untitled";
}

if (cache == null) cache = new Map();
```

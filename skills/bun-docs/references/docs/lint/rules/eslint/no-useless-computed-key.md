# no-useless-computed-key
Source: https://bun.com/docs/lint/rules/eslint/no-useless-computed-key

Disallow brackets around a property key that is a plain string or number


`{ ["name"]: value }` is the same as `{ "name": value }`. The brackets are for keys that are computed when the code runs. Around a string or a number they do nothing.

`--fix` removes the brackets.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-useless-computed-key" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-useless-computed-key" = ["error", {
  enforceForClassMembers = true,
}]
```


## Examples

Reported:

```js
const headers = { ["content-type"]: "text/plain", [0]: "first" };

const { ["content-type"]: type } = headers;

class Cache {
  ["clear"]() {}
}
```

Not reported:

```js
const headers = { "content-type": "text/plain", 0: "first", [name]: value };

const { "content-type": type } = headers;

class Cache {
  clear() {}
}
```

The brackets are allowed where they change the meaning. `{ "__proto__": base }` sets the prototype and `{ ["__proto__"]: base }` adds a normal property. In a class, `["constructor"]() {}` is a normal method, and `static prototype() {}` without brackets is a syntax error.

```js
const settings = { ["__proto__"]: base };

class Cache {
  ["constructor"]() {}
  static ["prototype"]() {}
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `enforceForClassMembers` | `true` | Also check class methods and fields. |

```js
class Cache {
  ["clear"]() {}
}
```

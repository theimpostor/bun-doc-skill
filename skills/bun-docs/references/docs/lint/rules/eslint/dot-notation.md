# dot-notation
Source: https://bun.com/docs/lint/rules/eslint/dot-notation

Require `user.name` instead of `user["name"]`


`user["name"]` and `user.name` read the same property. The dot form is shorter, and it leaves brackets for the cases that need them: a key in a variable, or a name that isn't a valid identifier.

`--fix` rewrites the brackets to a dot.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"dot-notation" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"dot-notation" = ["error", {
  allowKeywords = true,
  allowPattern = "", # string
}]
```


## Examples

Reported:

```js
const name = user["name"];
```

Not reported:

```js
const name = user.name;
const value = user[key];
const header = headers["content-type"];
const first = items[0];
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowKeywords` | `true` | With `false`, reserved words go in brackets, so `node.class` is reported and `node["class"]` is allowed. Only engines older than ES5 need this. |
| `allowPattern` | `""` | A regular expression. Property names that match it can be written in brackets. |

```js
const kind = node.class;
```

```js
const kind = node["class"];
```

To allow brackets for names that have an underscore:

```js
const firstName = row["first_name"];
```

```js
const firstName = row["name"];
```

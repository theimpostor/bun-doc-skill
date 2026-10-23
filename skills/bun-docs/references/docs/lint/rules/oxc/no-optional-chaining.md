# oxc/no-optional-chaining
Source: https://bun.com/docs/lint/rules/oxc/no-optional-chaining

Disallow optional chaining (`?.`)


Engines older than ES2020 can't parse `?.`, so a file that uses it fails to load there. If a compiler lowers it for a target like that, each `?.` turns into temporary variables and `null` and `undefined` checks, which makes the output larger.

The rule reports each chain once, no matter how many `?.` it has.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/no-optional-chaining" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/no-optional-chaining" = ["error", {
  message = "", # string
}]
```


## Examples

Reported:

```js
const city = user?.address?.city;
```

```js
const first = items?.[0];
onSave?.(first);
```

Not reported:

```js
const city = user && user.address && user.address.city;

if (onSave) {
  onSave(city);
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `message` | `""` | Text to show as help under the report, for example why your project doesn't allow `?.`. |

```js
const city = user?.address;
```

## When not to use it

Every current browser and runtime supports `?.`. Only use this rule if your code has to run on older ones.

# unicorn/no-null
Source: https://bun.com/docs/lint/rules/unicorn/no-null

Disallow the `null` literal in favor of `undefined`


JavaScript has two values for "nothing". If you only use `undefined`, you need one check instead of two. Default parameters and destructuring defaults also apply to `undefined` but not to `null`.

Strict comparisons such as `x === null` are allowed by default, because you often need to check what an API returned.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-null" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-null" = ["error", {
  checkStrictEquality = false,
  checkArguments = true,
}]
```


## Examples

Reported:

```js
let selected = null;
```

Not reported:

```js
let selected;

if (document.querySelector("dialog") === null) {
  selected = undefined;
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `checkStrictEquality` | `false` | Also report `x === null` and `x !== null`. |
| `checkArguments` | `true` | Report `null` that's passed to a function or a constructor. |

```js
if (selected === null) {
  selected = first();
}
```

```js
save(user, null);
```

## When not to use it

Many APIs return or expect `null`, like the DOM, JSON and databases. If your code talks to them a lot, this rule gets in the way.

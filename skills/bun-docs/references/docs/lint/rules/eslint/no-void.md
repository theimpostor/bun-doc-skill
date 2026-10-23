# no-void
Source: https://bun.com/docs/lint/rules/eslint/no-void

Disallow the `void` operator


`void expression` runs the expression and returns `undefined`. Few people know the operator, and `undefined` says the same thing in a word everybody can read.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-void" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-void" = ["error", {
  allowAsStatement = false,
}]
```


## Examples

Reported:

```js
let selected = void 0;

button.onclick = () => void save();
```

Not reported:

```js
let selected = undefined;

button.onclick = () => {
  save();
};
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowAsStatement` | `false` | Allow `void` when it's the whole statement. |

`void` at the start of a statement is how you tell `@typescript-eslint/no-floating-promises` that you're ignoring a promise on purpose. Turn this option on if you use both rules.

```js
void save();
```

Anywhere else, `void` is still reported:

```js
const result = void save();
```

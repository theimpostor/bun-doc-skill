# no-implicit-coercion
Source: https://bun.com/docs/lint/rules/eslint/no-implicit-coercion

Require `Boolean()`, `Number()` and `String()` instead of operator tricks like `!!x` and `+x`


`!!value`, `+value` and `"" + value` convert a value as a side effect of an operator. You have to know the trick to see that a conversion happens. `Boolean(value)`, `Number(value)` and `String(value)` say it by name.

`--fix` rewrites `!!value` to `Boolean(value)`. For the conversions to a number or a string, the rewrite is offered as a suggestion. Neither is offered where a comment would be lost, as in `!!(value /* or null */)`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-implicit-coercion" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-implicit-coercion" = ["error", {
  boolean = true,
  number = true,
  string = true,
  disallowTemplateShorthand = false,
  allow = [], # list of "~", "!!", "+", "- -", "-" or "*"
}]
```


## Examples

Reported:

```js
const hasItems = !!items.length;
const isMember = ~names.indexOf(user.name);
const quantity = +input.value;
const price = 1 * row.price;
const id = "" + user.id;
label += "";
```

Not reported:

```js
const hasItems = Boolean(items.length);
const isMember = names.indexOf(user.name) !== -1;
const quantity = Number(input.value);
const price = Number(row.price);
const id = String(user.id);
label = String(label);
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `boolean` | `true` | Report `!!value` and `~list.indexOf(value)`. |
| `number` | `true` | Report `+value`, `- -value`, `1 * value` and `value - 0`. |
| `string` | `true` | Report `"" + value` and `value += ""`. |
| `disallowTemplateShorthand` | `false` | Also report a template that holds one expression and nothing else. |
| `allow` | `[]` | Operators to leave alone: any of `"~"`, `"!!"`, `"+"`, `"- -"`, `"-"`, `"*"`. |

```js
const id = `${user.id}`;
```

`allow` keeps one trick while the rest of its group is still reported:

```js
const hasItems = !!items.length;
```

```js
const isMember = ~names.indexOf(user.name);
```

`"+"` stands for both `+value` and `"" + value`:

```js
const quantity = +input.value;
const id = "" + user.id;
```

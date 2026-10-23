# jsx-a11y/autocomplete-valid
Source: https://bun.com/docs/lint/rules/jsx-a11y/autocomplete-valid

Require `autoComplete` on an `input` to be a value that browsers know


Browsers and password managers use a field's `autocomplete` value to fill it in. With a value they don't know, such as `"mail"`, they guess or do nothing, and people who rely on autofill have to type everything.

The rule only checks values written as a string. An address field can have `billing` or `shipping` in front, as in `"shipping postal-code"`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/autocomplete-valid" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/autocomplete-valid" = ["error", {
  inputComponents = ["input"],
}]
```


## Examples

Reported:

```jsx
const email = <input type="email" autoComplete="mail" />;
const password = <input type="password" autoComplete="password" />;
```

Not reported:

```jsx
const email = <input type="email" autoComplete="email" />;
const password = <input type="password" autoComplete="current-password" />;
const zip = <input type="text" autoComplete="shipping postal-code" />;
const other = <input type="text" autoComplete={field.hint} />;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `inputComponents` | `["input"]` | The elements and components to check. Your list replaces the default, so keep `"input"` in it. |

```jsx
const email = <TextField autoComplete="mail" />;
const phone = <input autoComplete="phone" />;
```

```jsx
const phone = <input autoComplete="phone" />;
```

## When not to use it

The rule doesn't know every value that HTML allows. It reports the parts of a name, such as `given-name` and `family-name`, and the prefixes `home`, `work`, `mobile` and `section-`. If your forms use them, turn the rule off.

```jsx
const first = <input autoComplete="given-name" />;
const last = <input autoComplete="family-name" />;
const phone = <input autoComplete="mobile tel" />;
const zip = <input autoComplete="section-gift shipping postal-code" />;
```

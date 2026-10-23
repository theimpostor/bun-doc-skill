# jsx-a11y/no-autofocus
Source: https://bun.com/docs/lint/rules/jsx-a11y/no-autofocus

Disallow the `autoFocus` attribute


`autoFocus` moves focus as soon as the element renders. A screen reader starts reading at that element, so the user misses everything before it. On a phone, the keyboard opens and the page scrolls by itself.

`autoFocus={false}` isn't reported. Neither is `autoFocus` inside a `<dialog>`, an element with `role="dialog"`, or an element with a `popover` attribute, because opening one of those is supposed to move focus.

`--fix-suggestions` removes the attribute.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/no-autofocus" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/no-autofocus" = ["error", {
  ignoreNonDOM = false,
}]
```


## Examples

Reported:

```jsx
const search = <input type="search" autoFocus />;
```

Not reported:

```jsx
const search = <input type="search" />;

const rename = (
  <dialog open>
    <input type="text" autoFocus />
  </dialog>
);
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreNonDOM` | `false` | Only check HTML elements, not components. |

```jsx
const search = <SearchBox autoFocus />;
```

```jsx
const search = <SearchBox autoFocus />;
```

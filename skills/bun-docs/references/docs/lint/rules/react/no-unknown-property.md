# react/no-unknown-property
Source: https://bun.com/docs/lint/rules/react/no-unknown-property

Disallow attributes on DOM elements that React does not know


React has its own names for DOM attributes: `className` instead of `class`, `htmlFor` instead of `for`, `tabIndex` instead of `tabindex`, `strokeWidth` instead of `stroke-width`. Markup pasted from an HTML or SVG file has the other spelling, and React warns about it in the console when the page runs.

The rule checks elements with a lowercase name and reports three things:

- A name that React spells differently.
- A name that isn't a DOM attribute at all.
- An attribute on an element it doesn't belong to, such as `checked` on a `<div>`.

The rule doesn't check your own components, custom elements (a hyphen in the name, or an `is` attribute), or `data-*` attributes.

`--fix` renames an attribute when React has another spelling for it.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-unknown-property" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-unknown-property" = ["error", {
  ignore = [], # list of strings
  requireDataLowercase = false,
}]
```


## Examples

Reported:

```jsx
const field = (
  <label class="field" for="email">
    Email <input id="email" tabindex="1" />
  </label>
);
```

```jsx
const box = <div checked tooltip="Saved" />;
```

Not reported:

```jsx
const field = (
  <label className="field" htmlFor="email">
    Email <input id="email" tabIndex="1" data-testid="email" />
  </label>
);

const card = <Card class="wide" tooltip="Saved" />;
const player = <video-player autostart="yes" />;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignore` | `[]` | Attribute names to accept as they are. |
| `requireDataLowercase` | `false` | Report a `data-*` attribute with an uppercase letter in its name, on any element. |

Use `ignore` for attributes that a library adds, such as Emotion's `css` prop:

```jsx
const box = <div css={{ display: "flex" }} />;
```

```jsx
const button = <button data-testID="save">Save</button>;
```

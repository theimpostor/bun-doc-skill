# react/forbid-elements
Source: https://bun.com/docs/lint/rules/react/forbid-elements

Disallow the elements and components you choose


If your project has its own `<Button>`, a plain `<button>` skips its styles, its loading state, and its tracking. This rule reports the elements you list, so everyone uses the replacement.

The rule does nothing until you add entries to `forbid`. It checks both JSX and `React.createElement()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/forbid-elements" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/forbid-elements" = ["error", {
  # forbid = <list of strings or objects>,
}]
```


## Examples

Reported:

```jsx
<button onClick={save}>Save</button>;
```

```js
React.createElement("button", { onClick: save }, "Save");
```

Not reported:

```jsx
<Button onClick={save}>Save</Button>;
```

## Options

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/forbid-elements" = ["error", {
  forbid = [
    "marquee",
    { element = "button", message = "use our Button component" },
  ],
}]
```

`forbid` is the only option. It's a list of element names or objects, and it's empty by default:

| Key | What it does |
| --- | --- |
| `element` | The name, as it's written in the tag: `"button"`, `"Modal"`, `"legacy.Modal"`. |
| `message` | Added to the report: `<button> is forbidden, use our Button component`. |

```jsx
<legacy.Modal>
  <button>Close</button>
</legacy.Modal>;
```

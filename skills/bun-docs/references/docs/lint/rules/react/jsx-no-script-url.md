# react/jsx-no-script-url
Source: https://bun.com/docs/lint/rules/react/jsx-no-script-url

Disallow `javascript:` URLs in links


A `javascript:` URL runs its text as code when someone follows the link. That's a common way to inject a script into a page, and React 19 blocks these URLs. Use an event handler instead.

By default the rule looks at the `href` of `<a>`. It only sees URLs written as a plain string, not values in braces.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-no-script-url" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-no-script-url" = ["error", {
  includeFromSettings = false,
}]
```


## Examples

Reported:

```jsx
const close = <a href="javascript:closeDialog()">Close</a>;
```

Not reported:

```jsx
const close = <button onClick={closeDialog}>Close</button>;

const home = <a href="/home">Home</a>;
```

## Options

The first option is a list of your own link components and the props that hold a URL:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-no-script-url" = ["error", [{ name = "Link", props = ["to"] }]]
```

```jsx
const close = <Link to="javascript:closeDialog()">Close</Link>;
```

You can pass an object after the list, or instead of it:

| Option | Default | What it does |
| --- | --- | --- |
| `includeFromSettings` | `false` | Also check the components listed under `linkComponents` in your settings (`[lint.settings]` in `bunfig.toml`, or `settings` in an ESLint config). |

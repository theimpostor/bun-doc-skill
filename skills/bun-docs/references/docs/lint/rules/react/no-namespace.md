# react/no-namespace
Source: https://bun.com/docs/lint/rules/react/no-namespace

Disallow namespaced element names such as `<svg:circle>`


JSX syntax allows a name with a colon in it, such as `<svg:circle>`, but React doesn't support namespaced elements. The same goes for a name with a colon passed to `React.createElement`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-namespace" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const dot = <svg:circle r="4" />;

const line = React.createElement("svg:line");
```

Not reported:

```jsx
const dot = <circle r="4" />;

const line = React.createElement("line");
```

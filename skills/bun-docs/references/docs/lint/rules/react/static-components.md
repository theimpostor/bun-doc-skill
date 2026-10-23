# react-hooks/static-components
Source: https://bun.com/docs/lint/rules/react/static-components

Disallow components that are created while another component renders


React decides whether an element is the same one as last time by comparing the component function. A component created inside another component is a new function on every render. React then throws the old subtree away and mounts a new one, so it loses its state, its DOM nodes are rebuilt, and any input in it loses focus.

The rule reports a JSX tag that's a local variable holding a function written in the component, the result of a call, or the result of `new`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react-hooks/static-components" = "error" # or "warn"
```


## Examples

Reported:

```jsx
function Form({ label }) {
  const Field = () => <input placeholder={label} />;
  return <Field />;
}
```

```jsx
function Page({ theme }) {
  const Panel = createPanel(theme);
  return <Panel />;
}
```

Not reported:

```jsx
function Field({ label }) {
  return <input placeholder={label} />;
}

function Form({ label }) {
  return <Field label={label} />;
}
```

Choosing between components that already exist is fine:

```jsx
function Heading({ large, children }) {
  const Tag = large ? BigTitle : SmallTitle;
  return <Tag>{children}</Tag>;
}
```

# react-hooks/syntax
Source: https://bun.com/docs/lint/rules/react/syntax

Disallow invalid JavaScript in components and hooks, such as assigning to a `const`


Some mistakes parse fine and only fail when the code runs. The one you're likely to see here is an assignment to a `const` variable, which throws a `TypeError` when that line runs. The React Compiler catches it when it analyzes the component.

It also reports `delete` on something that isn't an object property, with a suggestion that removes the line.

The rule only looks at components and hooks. `no-const-assign` reports the same mistake in all code.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react-hooks/syntax" = "error" # or "warn"
```


## Examples

Reported:

```jsx
function Total({ items }) {
  const total = 0;
  total = items.length;
  return <span>{total}</span>;
}
```

The assignment can also be in a nested function:

```jsx
function Total({ items }) {
  const total = 0;
  const update = () => {
    total = items.length;
  };
  return <span onClick={update}>{total}</span>;
}
```

Not reported:

```jsx
function Total({ items }) {
  const total = items.length;
  return <span>{total}</span>;
}
```

This function is neither a component nor a hook, so the rule skips it:

```jsx
function countItems(items) {
  const total = 0;
  total = items.length;
  return total;
}
```

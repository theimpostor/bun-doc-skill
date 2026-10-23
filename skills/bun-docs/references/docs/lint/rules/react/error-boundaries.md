# react-hooks/error-boundaries
Source: https://bun.com/docs/lint/rules/react/error-boundaries

Disallow JSX inside a `try` block, where `catch` cannot see rendering errors


`<Chart />` doesn't call `Chart`. It only describes what to render, and React calls the component later, after your function has returned. So if `Chart` throws while rendering, the `try` around the JSX is long over and its `catch` never runs.

To handle a rendering error, wrap the component in an error boundary.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react-hooks/error-boundaries" = "error" # or "warn"
```


## Examples

Reported:

```jsx
function Dashboard({ data }) {
  try {
    return <Chart data={data} />;
  } catch {
    return <p>Could not draw the chart.</p>;
  }
}
```

Not reported:

```jsx
function Dashboard({ data }) {
  return (
    <ErrorBoundary fallback={<p>Could not draw the chart.</p>}>
      <Chart data={data} />
    </ErrorBoundary>
  );
}
```

A `try` around code that runs right away is fine, and so is JSX in the `catch` block:

```jsx
function Dashboard({ json }) {
  let data;
  try {
    data = JSON.parse(json);
  } catch {
    return <p>Could not read the data.</p>;
  }
  return <Chart data={data} />;
}
```

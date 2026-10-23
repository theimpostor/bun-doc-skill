# react-hooks/invariant
Source: https://bun.com/docs/lint/rules/react/invariant

Report code that makes the React Compiler fail one of its internal checks


The React Compiler checks its own work while it analyzes a component. When one of these checks fails, it gives up on that component or hook and leaves it unoptimized. The code still runs as written.

A report from this rule doesn't mean your code breaks one of React's rules. It means the compiler can't handle the way it's written. Writing it another way usually gets the component compiled again.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react-hooks/invariant" = "error" # or "warn"
```


## Examples

Reported, because one destructuring assignment writes to a variable that a function captures and to one that no function captures:

```jsx
function Results(props) {
  let rows = [];
  let total = 0;
  ({ rows, total } = props.load());
  const logRows = () => console.log(rows);
  return <div onClick={logRows}>{total}</div>;
}
```

Not reported:

```jsx
function Results(props) {
  const { rows, total } = props.load();
  const logRows = () => console.log(rows);
  return <div onClick={logRows}>{total}</div>;
}
```

## When not to use it

If you don't build with the React Compiler, you lose nothing when it gives up on a component.

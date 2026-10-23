# react-hooks/unsupported-syntax
Source: https://bun.com/docs/lint/rules/react/unsupported-syntax

Disallow syntax that the React Compiler cannot compile, such as `eval()`


The React Compiler needs to know everything a component reads and writes. `eval()` runs code it can't see, so it skips the whole component. The component still works, but it gets no automatic memoization.

The rule only looks at components and hooks, including the functions nested in them.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react-hooks/unsupported-syntax" = "error" # or "warn"
```


## Examples

Reported:

```jsx
function Calculator({ formula }) {
  const result = eval(formula);
  return <output>{result}</output>;
}
```

```jsx
function Calculator({ formula, onResult }) {
  return <button onClick={() => onResult(eval(formula))}>Run</button>;
}
```

Not reported:

```jsx
function Calculator({ formula }) {
  const result = evaluate(parse(formula));
  return <output>{result}</output>;
}
```

This function is neither a component nor a hook, so the compiler never sees it:

```jsx
function run(formula) {
  return eval(formula);
}
```

## When not to use it

If you don't use the React Compiler, a skipped component costs you nothing.

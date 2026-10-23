# react/no-adjacent-inline-elements
Source: https://bun.com/docs/lint/rules/react/no-adjacent-inline-elements

Disallow inline elements that touch each other without whitespace between them


Two inline elements such as `<a>` or `` that touch in the source render with nothing between them, so their text runs together on the page, like "Log inSign up".

The rule knows HTML's inline elements, including `a`, `b`, `button`, `code`, `em`, `i`, `img`, `input`, `label`, `select`, `small`, `span`, `strong` and `textarea`. It also checks an array of children passed to `React.createElement`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/no-adjacent-inline-elements" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const nav = (
  <div>
    <a href="/login">Log in</a><a href="/signup">Sign up</a>
  </div>
);
```

```jsx
const nav = React.createElement("div", undefined, [
  React.createElement("a", { href: "/login" }, "Log in"),
  React.createElement("a", { href: "/signup" }, "Sign up"),
]);
```

Not reported:

```jsx
const nav = (
  <div>
    <a href="/login">Log in</a> <a href="/signup">Sign up</a>
  </div>
);
```

Elements on separate lines aren't reported, even though JSX drops the line break and renders nothing between them. Write `{" "}` at the end of the line if you want a space there:

```jsx
const joined = (
  <div>
    <a href="/login">Log in</a>
    <a href="/signup">Sign up</a>
  </div>
);

const spaced = (
  <div>
    <a href="/login">Log in</a>{" "}
    <a href="/signup">Sign up</a>
  </div>
);
```

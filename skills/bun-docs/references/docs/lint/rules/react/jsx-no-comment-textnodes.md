# react/jsx-no-comment-textnodes
Source: https://bun.com/docs/lint/rules/react/jsx-no-comment-textnodes

Disallow `//` and `/* */` comments written as text between JSX tags


Between JSX tags, `//` and `/* */` don't start a comment. They're text, and your users see it on the page. A comment there must be inside braces.

The rule reports text that has a line starting with `//` or `/*`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-no-comment-textnodes" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const header = (
  <header>
    // TODO: add the logo
    <h1>Welcome</h1>
    /* the subtitle goes here */
  </header>
);
```

Not reported:

```jsx
const header = (
  <header>
    {/* TODO: add the logo */}
    <h1>Welcome</h1>
    <a href="https://bun.com">See https://bun.com</a>
  </header>
);
```

To show text like that on purpose, write it as a string in braces:

```jsx
const hint = <code>{"// a comment in JavaScript"}</code>;
```

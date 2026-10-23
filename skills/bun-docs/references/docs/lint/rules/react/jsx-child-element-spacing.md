# react/jsx-child-element-spacing
Source: https://bun.com/docs/lint/rules/react/jsx-child-element-spacing

Disallow a line break between text and an inline element in JSX, where a space may be lost


JSX removes a line break between text and an element, along with the indentation around it. HTML would show a space there. So the first example below renders as "Read thedocs", and nothing in the code says whether that was on purpose.

The rule reports a line break between text and an inline element such as `a`, `b`, `code`, `em`, `span`, or `strong`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-child-element-spacing" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const help = (
  <p>
    Read the
    <a href="/docs">docs</a>
  </p>
);
```

```jsx
const help = (
  <p>
    <strong>Note:</strong>
    this cannot be undone
  </p>
);
```

Not reported:

```jsx
const help = (
  <p>
    Read the{" "}
    <a href="/docs">docs</a>
  </p>
);

const short = <p>Read the <a href="/docs">docs</a></p>;
```

To show that you don't want a space, put a comment in between:

```jsx
const price = (
  <p>
    $
    {/* no space */}
    <b>20</b>
  </p>
);
```

The rule doesn't check block elements, `br`, or your own components:

```jsx
const address = (
  <div>
    Ship to
    <p>1 Main Street</p>
    Springfield
    <br />
    USA
    <Badge />
  </div>
);
```

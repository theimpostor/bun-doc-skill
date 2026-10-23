# jsx-a11y/heading-has-content
Source: https://bun.com/docs/lint/rules/jsx-a11y/heading-has-content

Require headings to have content that a screen reader can read


People who use a screen reader move through a page by its headings. An empty `h1` to `h6`, or one with only hidden content, is a stop in that list with nothing to read.

Text, an expression and a visible element count as content. So do the `children` and `dangerouslySetInnerHTML` props. A heading that's hidden itself with `aria-hidden` isn't checked.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/heading-has-content" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/heading-has-content" = ["error", {
  components = [], # list of strings
}]
```


## Examples

Reported:

```jsx
const title = <h1 className="hero" />;
const section = <h2><span aria-hidden>Pricing</span></h2>;
```

Not reported:

```jsx
const title = <h1 className="hero">{page.title}</h1>;
const section = <h2><span>Pricing</span></h2>;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `components` | `[]` | Components to check like `h1` to `h6`. |

```jsx
const title = <Heading level={1} />;
```

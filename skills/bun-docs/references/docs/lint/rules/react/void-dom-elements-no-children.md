# react/void-dom-elements-no-children
Source: https://bun.com/docs/lint/rules/react/void-dom-elements-no-children

Disallow children on void DOM elements such as `<img />` and `<br>`


Some HTML elements can never have content: `<img>`, `<br>`, `<hr>`, `<input>`, `<link>`, `<meta>` and a few more. React throws when it renders one of them with children.

The rule reports children between the tags, a `children` prop and a `dangerouslySetInnerHTML` prop, in JSX and in `React.createElement()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/void-dom-elements-no-children" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const field = <input name="email">Email</input>;

const photo = <img src={url} children="A photo" />;

const rule = <hr dangerouslySetInnerHTML={{ __html: "Section" }} />;

const lineBreak = React.createElement("br", {}, "Next line");
```

Not reported:

```jsx
const field = (
  <label>
    Email
    <input name="email" />
  </label>
);

const photo = <img src={url} alt="A photo" />;

const lineBreak = React.createElement("br");
```

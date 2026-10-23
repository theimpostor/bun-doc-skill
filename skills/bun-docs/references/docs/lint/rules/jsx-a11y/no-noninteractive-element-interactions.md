# jsx-a11y/no-noninteractive-element-interactions
Source: https://bun.com/docs/lint/rules/jsx-a11y/no-noninteractive-element-interactions

Disallow mouse and keyboard handlers on non-interactive elements


Elements such as `<li>`, `<p>`, `<img>`, `<h1>` and `<main>` describe content. A screen reader doesn't announce them as something you can press, and the Tab key skips them, so a click handler on one only works with a mouse.

An element with a non-interactive role, such as `<div role="article">`, is treated the same way. For `<div>` and `` without a role, see `jsx-a11y/no-static-element-interactions`.

Not reported:

- components
- elements with an interactive role, `role="presentation"` or `role="none"`
- elements with `aria-hidden` or `contentEditable="true"`
- handlers set to `null` or `undefined`


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/no-noninteractive-element-interactions" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const item = <li onClick={() => select(user)}>{user.name}</li>;
const card = <div role="article" onKeyDown={openCard} />;
```

Not reported:

```jsx
const item = (
  <li>
    <button onClick={() => select(user)}>{user.name}</button>
  </li>
);

const option = <li role="option" tabIndex={0} onClick={() => select(user)} />;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `handlers` | mouse, drag and keyboard handlers, `onFocus`, `onBlur`, `onLoad`, `onError` | The handlers to report. Your list replaces the default. |
| an element name | see below | Handlers that are allowed on that element. |

By default `onLoad` and `onError` are allowed on `<body>`, `<iframe>` and `<img>`, and `onKeyUp`, `onKeyDown` and `onKeyPress` are allowed on `<dialog>`. Setting any option drops these defaults, so repeat the ones you want to keep.

```jsx
const photo = <img src={url} alt="" onLoad={fadeIn} />;
```

```jsx
const photo = <img src={url} alt="" onLoad={fadeIn} />;
```

```jsx
const photo = <img src={url} alt="" onLoad={fadeIn} />;
```

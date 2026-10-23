# react/jsx-props-no-spreading
Source: https://bun.com/docs/lint/rules/react/jsx-props-no-spreading

Disallow `{...props}` in JSX


`{...props}` passes on everything in the object, including props the element doesn't know. You can't tell from the tag what it receives, and on an HTML element the extras end up as unknown attributes in the page. Naming each prop shows what's passed.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-props-no-spreading" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-props-no-spreading" = ["error", {
  html = "enforce", # "enforce" or "ignore"
  custom = "enforce", # "enforce" or "ignore"
  explicitSpread = "enforce", # "enforce" or "ignore"
  exceptions = [], # list of strings
}]
```


## Examples

Reported:

```jsx
function Avatar(props) {
  return <img {...props} />;
}
```

Not reported:

```jsx
function Avatar({ src, alt }) {
  return <img src={src} alt={alt} />;
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `html` | `"enforce"` | `"ignore"` allows spreading on HTML elements such as `<img>`. |
| `custom` | `"enforce"` | `"ignore"` allows spreading on components such as `<Avatar>`. |
| `explicitSpread` | `"enforce"` | `"ignore"` allows spreading an object written in place, where every prop is named. |
| `exceptions` | `[]` | Tag names that get the opposite of what `html` or `custom` says for them. |

```jsx
const field = <input {...inputProps} />;
```

```jsx
const field = <TextField {...inputProps} />;
```

```jsx
const field = <TextField {...inputProps} />;
```

```jsx
const avatar = <Avatar {...{ src, alt }} />;
```

An exception allows a tag that's otherwise checked:

```jsx
const field = <TextField {...inputProps} />;
```

And it checks a tag that's otherwise ignored:

```jsx
const field = <TextField {...inputProps} />;
```

## When not to use it

Wrapper components that pass the rest of their props to one element, as in `<button {...rest}>`, are a common and reasonable pattern. If you write many of them, turn the rule off or list them in `exceptions`.

# react/jsx-props-no-spread-multi
Source: https://bun.com/docs/lint/rules/react/jsx-props-no-spread-multi

Disallow spreading the same variable twice in one JSX element


Spreading the same object a second time adds nothing new, and it overwrites every prop written between the two. In `<Button {...props} disabled {...props} />`, `disabled` is lost if `props` also has a `disabled`. It's almost always a leftover from a merge or a copy.

`--fix` removes every spread of the variable except the last. With an ESLint config there's no fix, same as in `eslint-plugin-react`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-props-no-spread-multi" = "error" # or "warn"
```


## Examples

Reported:

```jsx
function SaveButton(props) {
  return <Button {...props} type="submit" {...props} />;
}
```

Not reported:

```jsx
function SaveButton(props) {
  return <Button {...props} type="submit" />;
}

function Field({ input, meta }) {
  return <Input {...input} {...meta} />;
}
```

# react/jsx-props-no-multi-spaces
Source: https://bun.com/docs/lint/rules/react/jsx-props-no-multi-spaces

Disallow more than one space, or an empty line, between JSX props


Extra spaces between props, or an empty line between props that are each on their own line, are usually left over from an edit.

`--fix` replaces the extra spaces with one. It doesn't remove empty lines.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"react/jsx-props-no-multi-spaces" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const button = <Button  type="submit"   disabled />;
```

```jsx
const button = (
  <Button
    type="submit"

    disabled
  />
);
```

Not reported:

```jsx
const button = <Button type="submit" disabled />;

const link = (
  <Link
    to="/settings"
    replace
  />
);
```

## When not to use it

A formatter such as `bun fmt` or Prettier already fixes this spacing.

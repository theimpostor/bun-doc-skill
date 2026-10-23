# jsx-a11y/no-access-key
Source: https://bun.com/docs/lint/rules/jsx-a11y/no-access-key

Disallow the `accessKey` attribute


`accessKey` adds a keyboard shortcut to an element. Screen readers and browsers already use many key combinations, and they differ from one to the next, so your shortcut can take over a command that a keyboard user depends on.

The attribute is reported on any element or component, no matter how it's capitalized.

`--fix-suggestions` removes the attribute.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jsx-a11y/no-access-key" = "error" # or "warn"
```


## Examples

Reported:

```jsx
const save = <button accessKey="s">Save</button>;
const open = <MenuItem accesskey="o" />;
```

Not reported:

```jsx
const save = <button>Save</button>;
const open = <MenuItem />;
```

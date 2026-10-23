# import/no-default-export
Source: https://bun.com/docs/lint/rules/import/no-default-export

Disallow default exports


A default export doesn't have a name, so every file that imports it makes one up. The same component ends up as `Button` here and `Btn` there, a search for its name misses some of its uses, and renaming it doesn't rename the imports. A named export has one name everywhere.

`export { name as default }` is reported too.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-default-export" = "error" # or "warn"
```


## Examples

Reported:

```js
export default function formatPrice(cents) {
  return `$${(cents / 100).toFixed(2)}`;
}
```

```js
const formatPrice = cents => `$${(cents / 100).toFixed(2)}`;

export { formatPrice as default };
```

Not reported:

```js
export function formatPrice(cents) {
  return `$${(cents / 100).toFixed(2)}`;
}
```

## When not to use it

Some tools need a default export, like framework pages and layouts, config files and stories. Turn the rule off for those files.

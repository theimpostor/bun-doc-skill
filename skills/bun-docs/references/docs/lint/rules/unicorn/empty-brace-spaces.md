# unicorn/empty-brace-spaces
Source: https://bun.com/docs/lint/rules/unicorn/empty-brace-spaces

Disallow spaces and line breaks inside empty braces


You can write an empty pair of braces as `{}`, `{ }` or over two lines. This rule keeps `{}`, so empty objects, blocks, function bodies and class bodies look the same everywhere.

Braces with a comment in them aren't empty, so they're left alone.

`--fix` removes the whitespace.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/empty-brace-spaces" = "error" # or "warn"
```


## Examples

Reported:

```js
const cache = { };

function noop() {
}

class Store { }
```

Not reported:

```js
const cache = {};

function noop() {}

class Store {}

try {
  cache.clear();
} catch {
  // Nothing to clean up.
}
```

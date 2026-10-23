# import/exports-last
Source: https://bun.com/docs/lint/rules/import/exports-last

Require all exports to come after every other statement in the file


When exports are spread through a file, you have to read all of it to learn what it offers. With every export at the bottom, the last lines of the file are its public interface.

An export is reported if any statement that isn't an export comes after it. This applies to every kind: `export const`, `export function`, `export default`, `export { }` and `export * from`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/exports-last" = "error" # or "warn"
```


## Examples

Reported:

```js
export const retries = 3;

function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

export { wait };
```

Not reported:

```js
const retries = 3;

function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

export { retries, wait };
```

```js
const cache = new Map();

export const retries = 3;
export function clear() {
  cache.clear();
}
export default cache;
```

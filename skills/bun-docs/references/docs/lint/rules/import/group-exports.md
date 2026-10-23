# import/group-exports
Source: https://bun.com/docs/lint/rules/import/group-exports

Require all named exports to be in a single `export` declaration


When `export` is written on many declarations, you have to scan the whole file to learn what it exports. One `export { }` list, or one assignment to `module.exports`, shows it in one place.

As soon as there are two exports, each of them is reported. Values, types (`export type`) and re-exports from each module (`export { } from`) are counted separately. A default export doesn't count.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/group-exports" = "error" # or "warn"
```


## Examples

Reported:

```js
export const retries = 3;

export function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```

```js
export { parse } from "./json.js";
export { stringify } from "./json.js";
```

```js
exports.retries = 3;
module.exports.wait = ms => new Promise(resolve => setTimeout(resolve, ms));
```

Not reported:

```js
const retries = 3;

function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

export { retries, wait };
export default wait;
```

```js
export { parse, stringify } from "./json.js";
export { encode } from "./base64.js";
```

```js
const retries = 3;
const wait = ms => new Promise(resolve => setTimeout(resolve, ms));

module.exports = { retries, wait };
```

```ts
interface Options {
  retries: number;
}
const defaults: Options = { retries: 3 };

export { defaults };
export type { Options };
```

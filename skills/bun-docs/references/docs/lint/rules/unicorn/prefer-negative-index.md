# unicorn/prefer-negative-index
Source: https://bun.com/docs/lint/rules/unicorn/prefer-negative-index

Require a negative index instead of `.length - index`


`slice`, `at`, `splice`, `toSpliced` and `subarray` count a negative index from the end, so `items.slice(items.length - 2)` can be `items.slice(-2)`.

The rule only looks at the index arguments. That's the first two for `slice` and `subarray`, and the first for the others.

`--fix` removes the `.length` part.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-negative-index" = "error" # or "warn"
```


## Examples

Reported:

```js
const lastTwo = items.slice(items.length - 2);
const last = items.at(items.length - 1);
queue.splice(queue.length - 1, 1);
const rest = Array.prototype.slice.call(list, list.length - 2);
```

Not reported:

```js
const lastTwo = items.slice(-2);
const last = items.at(-1);
queue.splice(-1, 1);
const rest = Array.prototype.slice.call(list, -2);
```

The length must come from the same object, minus a number literal. Bracket access isn't reported, because `items[-1]` is `undefined`:

```js
const rest = items.slice(other.length - 2);
const tail = items.slice(items.length - count); // slice(-count) is the whole array when count is 0
const last = items[items.length - 1];
```

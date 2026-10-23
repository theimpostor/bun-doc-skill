# unicorn/no-unreadable-array-destructuring
Source: https://bun.com/docs/lint/rules/unicorn/no-unreadable-array-destructuring

Disallow array destructuring that skips two or more values in a row


In `const [,,, year] = parts`, you have to count commas to know which element you get, and it's easy to miss one comma too many or too few. Read the element by its index instead.

Skipping one value at a time is fine.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-unreadable-array-destructuring" = "error" # or "warn"
```


## Examples

Reported:

```js
const [, , , year] = match;

function area([, , width, height]) {
  return width * height;
}
```

Not reported:

```js
const year = match[3];

function area(box) {
  return box[2] * box[3];
}

const [, month] = match;
const [first, , third] = match;
```

# unicorn/no-new-buffer
Source: https://bun.com/docs/lint/rules/unicorn/no-new-buffer

Require `Buffer.from()` or `Buffer.alloc()` instead of the deprecated `new Buffer()`


`new Buffer(value)` allocates that many bytes if `value` is a number, and copies `value` if it's a string or an array. If user input turns out to be a number where you expected a string, the call allocates memory instead of copying text. Node.js deprecated the constructor for this reason. `Buffer.alloc()` and `Buffer.from()` each do one thing.

`--fix-suggestions` picks `Buffer.alloc()` when the first argument is a number literal, and `Buffer.from()` when it's a string, a template literal, or an array literal. It leaves other calls alone.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-new-buffer" = "error" # or "warn"
```


## Examples

Reported:

```js
const header = new Buffer(16);
const name = new Buffer("Ada", "utf8");
```

Not reported:

```js
const header = Buffer.alloc(16);
const name = Buffer.from("Ada", "utf8");
```

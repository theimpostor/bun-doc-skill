# unicorn/no-confusing-array-with
Source: https://bun.com/docs/lint/rules/unicorn/no-confusing-array-with

Disallow a negative index and `.length` as the index of `Array#with()`


`array.with(index, value)` returns a copy of the array with one element replaced. A negative index counts from the end, and a reader who doesn't know that can't tell which element changes. Passing the array's `.length` as the index looks like a way to append, but `with()` never makes the array longer. It throws a `RangeError`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-confusing-array-with" = "error" # or "warn"
```


## Examples

Reported:

```js
const updated = scores.with(-1, 100);
```

```js
const longer = scores.with(scores.length, 100); // throws a RangeError
```

Not reported:

```js
const updated = scores.with(scores.length - 1, 100);
```

```js
const longer = [...scores, 100];
```

The rule only sees a number written directly in the call. It doesn't check an index stored in a variable:

```js
const last = -1;
const updated = scores.with(last, 100);
```

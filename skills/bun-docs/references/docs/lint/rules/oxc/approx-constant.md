# oxc/approx-constant
Source: https://bun.com/docs/lint/rules/oxc/approx-constant

Disallow numbers that approximate a constant of the `Math` object


Typing `3.14159` by hand is less precise than `Math.PI`, and readers have to recognize the digits to know what it is.

The rule reports a number with at least three decimals that's a cut off or rounded `Math.E`, `Math.LN10`, `Math.LN2`, `Math.LOG2E`, `Math.LOG10E`, `Math.PI`, `Math.SQRT1_2` or `Math.SQRT2`. `3.14` is too short to count.

`--fix-suggestions` replaces the number with the constant.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/approx-constant" = "error" # or "warn"
```


## Examples

Reported:

```js
function circleArea(radius) {
  return 3.14159 * radius * radius;
}

const diagonal = side * 1.4142;
```

Not reported:

```js
function circleArea(radius) {
  return Math.PI * radius * radius;
}

const diagonal = side * Math.SQRT2;
const price = 3.14;
```

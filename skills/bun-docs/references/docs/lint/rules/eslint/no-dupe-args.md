# no-dupe-args
Source: https://bun.com/docs/lint/rules/eslint/no-dupe-args

Disallow two parameters with the same name in a function


When two parameters have the same name, the name refers to the last one. You can only reach the argument passed for the first one through `arguments`. It's nearly always a typo or a copy-paste mistake.

In strict mode, in modules and in arrow functions this is already a syntax error. The rule catches it in the scripts where it isn't, such as a `.cjs` file without `"use strict"`.

This rule is on by default in JavaScript files. It's off in TypeScript files, where TypeScript reports the same mistake.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-dupe-args" = "off" # or "warn"
```


## Examples

Reported, in a `.cjs` file:

```js
function resize(width, height, width) {
  return width * height;
}
```

Not reported:

```js
function resize(width, height, depth) {
  return width * height * depth;
}
```

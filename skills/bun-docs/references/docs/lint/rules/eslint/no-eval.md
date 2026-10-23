# no-eval
Source: https://bun.com/docs/lint/rules/eslint/no-eval

Disallow `eval()`


`eval()` runs a string as code, with access to the variables around the call. If any part of that string comes from outside your program, the person who controls it can run anything your program can.

Most uses have a direct replacement: `JSON.parse()` for data, `object[key]` for a property chosen by name.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-eval" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-eval" = ["error", {
  allowIndirect = false,
}]
```


## Examples

Reported:

```js
const settings = eval("(" + text + ")");
```

Reaching `eval` another way is reported too:

```js
const run = eval;
globalThis.eval(code);
(0, eval)(code);
```

Not reported:

```js
const settings = JSON.parse(text);
const value = user[field];
```

A method named `eval` on your own object is fine:

```js
const result = sandbox.eval(code);
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowIndirect` | `false` | Allow indirect calls to `eval`. |

An indirect call runs the code in the global scope, so it can't read or change the local variables around the call:

```js
(0, eval)(code);
globalThis.eval(code);
eval?.(code);
```

A direct call is still reported:

```js
eval(code);
```

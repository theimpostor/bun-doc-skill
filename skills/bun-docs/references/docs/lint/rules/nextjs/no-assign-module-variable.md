# @next/next/no-assign-module-variable
Source: https://bun.com/docs/lint/rules/nextjs/no-assign-module-variable

Disallow declaring a variable named `module`


The bundler gives every file a `module` object, and the code Next.js adds for hot reloading uses it. If you declare a variable named `module`, it hides that object, which can break the build or hot reloading.

The rule reports `var`, `let`, `const` and `using` declarations of `module`, anywhere in the file. It doesn't report parameters, destructuring, or an assignment to the existing `module`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@next/next/no-assign-module-variable" = "error" # or "warn"
```


## Examples

Reported:

```js
const module = await import("./charts.js");
module.render();
```

Not reported:

```js
const charts = await import("./charts.js");
charts.render();
```

```js
module.exports = { reactStrictMode: true };

function describe(module) {
  return module.id;
}
```

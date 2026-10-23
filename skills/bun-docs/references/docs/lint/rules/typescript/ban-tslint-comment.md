# @typescript-eslint/ban-tslint-comment
Source: https://bun.com/docs/lint/rules/typescript/ban-tslint-comment

Disallow `// tslint:disable` and `// tslint:enable` comments


TSLint is no longer maintained. Once a project has moved off it, its `tslint:disable` and `tslint:enable` comments do nothing, but they look like they still turn something off.

`--fix` removes the comment.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/ban-tslint-comment" = "error" # or "warn"
```


## Examples

Reported:

```ts
/* tslint:disable */
const port = 3000;
console.log(port); // tslint:disable-line:no-console
```

Not reported:

```ts
const port = 3000;
console.log(port); // the tslint config is gone
```

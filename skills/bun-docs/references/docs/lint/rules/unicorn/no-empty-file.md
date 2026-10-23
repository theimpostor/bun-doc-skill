# unicorn/no-empty-file
Source: https://bun.com/docs/lint/rules/unicorn/no-empty-file

Disallow files that contain no code


A file without code does nothing. It's usually left over from a refactor, or someone created it and never filled it in. It still shows up in searches and in the file tree, and importing it works but gives you nothing.

A file counts as empty if it only has whitespace, comments, directives such as `"use strict"`, lone semicolons, or empty blocks.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-empty-file" = "error" # or "warn"
```


## Examples

Reported:

```js
// TODO: move the date helpers here
```

```js
"use strict";
```

Not reported:

```js
export function formatDate(date) {
  return date.toISOString().slice(0, 10);
}
```

A file with a `///` comment isn't reported, because `/// <reference>` does something in TypeScript:

```ts
/// <reference types="bun" />
```

`export {}` is code. It makes the file a module:

```ts
export {};
```

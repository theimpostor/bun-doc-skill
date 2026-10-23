# @typescript-eslint/prefer-namespace-keyword
Source: https://bun.com/docs/lint/rules/typescript/prefer-namespace-keyword

Require `namespace` instead of `module` to declare a namespace


`module Shapes {}` declares a namespace. It has nothing to do with modules in the usual sense, which are files with `import` and `export`. `namespace Shapes {}` means the same thing and can't be confused with them.

`declare module "name"` with the name in quotes describes a package or a file. There's no other way to write it, so it's left alone.

`--fix` replaces the keyword.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/prefer-namespace-keyword" = "off" # or "error"
```


## Examples

Reported:

```ts
module Shapes {
  export const sides = 4;
}

declare module Vendor {
  function init(): void;
}
```

Not reported:

```ts
namespace Shapes {
  export const sides = 4;
}

declare namespace Vendor {
  function init(): void;
}

declare module "vendor-package" {
  export function init(): void;
}
```

# oxc/no-const-enum
Source: https://bun.com/docs/lint/rules/oxc/no-const-enum

Disallow TypeScript `const enum`


A `const enum` doesn't exist at runtime. TypeScript replaces each use with the member's value, and to do that it has to read the file that declares the enum. A tool that compiles one file at a time can't do that for an imported enum. If the enum is in a published `.d.ts` file, its values are copied into every package compiled against it, and they go stale when the enum changes.

`--fix` removes `const`, which makes it a regular enum.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"oxc/no-const-enum" = "error" # or "warn"
```


## Examples

Reported:

```ts
export const enum Status {
  Active,
  Archived,
}
```

Not reported:

```ts
export enum Status {
  Active,
  Archived,
}
```

An object with `as const` gives you plain values without an enum:

```ts
export const Status = {
  Active: 0,
  Archived: 1,
} as const;
```

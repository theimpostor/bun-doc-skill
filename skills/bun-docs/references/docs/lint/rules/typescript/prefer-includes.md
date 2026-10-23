# @typescript-eslint/prefer-includes
Source: https://bun.com/docs/lint/rules/typescript/prefer-includes

Require `.includes()` instead of comparing `.indexOf()` with `-1`


`tags.indexOf("draft") !== -1` gets a position and compares it with a magic number, only to find out if the value is there. It's easy to write `> 0` instead of `>= 0` and miss the first element. `tags.includes("draft")` asks the question directly.

The rule works for strings, arrays, and any of your own types that has an `includes` method with the same parameters as its `indexOf`. It also reports `.test()` on a regular expression that only matches one fixed string, such as `/admin/`.

`--fix` rewrites both forms. `tags?.indexOf("draft") !== -1` is reported but not fixed.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/prefer-includes" = "error" # or "warn"
```


## Examples

Reported:

```ts
function check(tags: string[], path: string) {
  if (tags.indexOf("draft") !== -1) return false;
  if (path.indexOf("/private/") >= 0) return false;
  return /admin/.test(path);
}
```

Not reported:

```ts
function check(tags: string[], path: string) {
  if (tags.includes("draft")) return false;
  if (path.includes("/private/")) return false;
  return path.includes("admin");
}
```

Code that uses the position, or a regular expression that does more than match a fixed string, is left alone:

```ts
function slice(path: string) {
  const start = path.indexOf("/private/");
  if (/^admin/.test(path) || /admin/i.test(path)) return "";
  return path.slice(start);
}
```

A type that has no `includes` method is left alone too:

```ts
interface Playlist {
  indexOf(song: string): number;
}

function has(playlist: Playlist, song: string) {
  return playlist.indexOf(song) !== -1;
}
```

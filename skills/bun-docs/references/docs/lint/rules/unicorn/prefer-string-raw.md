# unicorn/prefer-string-raw
Source: https://bun.com/docs/lint/rules/unicorn/prefer-string-raw

Require `String.raw` for strings that escape backslashes


In a normal string you write every backslash twice, which makes a Windows path or a regex source hard to read and easy to get wrong. In a `String.raw` template you write it once.

The rule skips a string that has another escape such as `\n`, ends with a backslash, or contains a backtick or `${`. `String.raw` can't express those.

`--fix` rewrites the string to a `String.raw` template. It leaves a string with a non-ASCII character such as `é` alone, because Bun's runtime currently gives `String.raw` the escaped form `\u00E9`, which is another string.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-string-raw" = "error" # or "warn"
```


## Examples

Reported:

```js
const logs = "C:\\Users\\ada\\logs";
const version = new RegExp("\\d+\\.\\d+");
```

Not reported:

```js
const logs = String.raw`C:\Users\ada\logs`;
const version = new RegExp(String.raw`\d+\.\d+`);

const lines = "C:\\logs\n"; // has another escape
const folder = "C:\\logs\\"; // ends with a backslash
```

# unicorn/prefer-string-starts-ends-with
Source: https://bun.com/docs/lint/rules/unicorn/prefer-string-starts-ends-with

Require `startsWith()` and `endsWith()` instead of a regex with `^` or `$`


`/^https:/.test(url)` asks whether a string starts with some fixed text. `url.startsWith("https:")` asks the same thing in plain words, and you don't need to escape the text for a regex.

The rule reports `.test()` on a regex literal that's only `^` followed by plain characters, or plain characters followed by `$`. A regex with the `m` flag, or with the `i` flag and letters, isn't reported.

`--fix` rewrites the call if the file shows that the argument is a string: a literal, a template, `String(value)`, a variable that's declared with one of these and never assigned again, or one declared as `string`. `test()` turns `undefined` or a number into a string, and `startsWith()` isn't a method of those. `--fix-dangerously` also rewrites the call when the argument is another name, a property access or a call.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-string-starts-ends-with" = "error" # or "warn"
```


## Examples

Reported:

```js
const secure = /^https:/.test(url);
const isScript = /\.js$/.test(file);
```

Not reported:

```js
const secure = url.startsWith("https:");
const isScript = file.endsWith(".js");

const isImage = /\.(png|jpg)$/.test(file);
const isHeader = /^x-/i.test(name);
```

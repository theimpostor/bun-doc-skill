# no-regex-spaces
Source: https://bun.com/docs/lint/rules/eslint/no-regex-spaces

Disallow several spaces in a row in a regular expression


In `/error   code/` you can't tell at a glance whether there are two, three or four spaces. ` {3}` spells it out.

The rule checks regular expression literals and strings passed to `RegExp`. Spaces inside a character class such as `[  ]` aren't reported.

`--fix` replaces the spaces with one space and a count.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-regex-spaces" = "off" # or "error"
```


## Examples

Reported:

```js
const line = /error   code/;
const header = new RegExp("name  value");
```

Not reported:

```js
const line = /error {3}code/;
const header = new RegExp("name {2}value");
const anyGap = /name +value/;
```

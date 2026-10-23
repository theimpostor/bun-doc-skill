# no-useless-backreference
Source: https://bun.com/docs/lint/rules/eslint/no-useless-backreference

Disallow regular expression backreferences that always match the empty string


A backreference such as `\1` or `\k<quote>` matches the text that a group captured. If the group can't have captured anything by the time the backreference is reached, the backreference matches the empty string, and the pattern accepts more than it seems to.

That happens when the group comes later in the pattern, when the backreference is inside the group, when the group is in another alternative of a `|`, or when the group is in a negative lookaround.

Patterns passed as a string to `RegExp` are checked too.

This rule is on by default.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-useless-backreference" = "off" # or "error"
```


## Examples

Reported:

```js
const quoted = /\1.*?(["'])/;
const either = /(a)|\1b/;
const doubled = new RegExp("(\\w\\1)");
const notQuoted = /(?!(["']))\w+\1/;
```

Not reported:

```js
const quoted = /(["']).*?\1/;
const either = /(a)\1|b/;
const doubled = new RegExp("(\\w)\\1");
```

# no-template-curly-in-string
Source: https://bun.com/docs/lint/rules/eslint/no-template-curly-in-string

Disallow `${}` placeholders in strings with ordinary quotes


`${name}` is only replaced inside backticks. In `"Hello, ${name}"` it stays as it is, and the user sees the text `${name}`. This happens when you type the wrong quotes, or add a placeholder to a string that was fine with quotes before.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-template-curly-in-string" = "error" # or "warn"
```


## Examples

Reported:

```js
const greeting = "Hello, ${user.name}!";
```

Not reported:

```js
const greeting = `Hello, ${user.name}!`;
const price = "$5";
```

## When not to use it

Some strings are meant for another tool that uses the same syntax, such as a shell command with `"${HOME}/bin"`. If you have many of them, turn the rule off for those files.

# unicorn/no-abusive-eslint-disable
Source: https://bun.com/docs/lint/rules/unicorn/no-abusive-eslint-disable

Require `eslint-disable` comments to name the rules they turn off


An `eslint-disable` comment without a rule name turns off every rule. You add it to silence one report, and it also hides every other problem on that line or in that file, now and later.

The rule checks `eslint-disable`, `eslint-disable-line`, and `eslint-disable-next-line`, and the same comments that start with `oxlint-`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-abusive-eslint-disable" = "error" # or "warn"
```


## Examples

Reported:

```js
console.log(user.name); // eslint-disable-line

// oxlint-disable-next-line
console.log(user.email);

/* eslint-disable */
console.log(user.id);
/* eslint-enable */
```

A reason after `--` isn't a rule name:

```js
console.log(user.name); // eslint-disable-line -- needed for debugging
```

Not reported:

```js
console.log(user.name); // eslint-disable-line no-console

// oxlint-disable-next-line no-console, no-undef
console.log(user.email);

/* eslint-disable no-console */
console.log(user.id);
/* eslint-enable no-console */
```

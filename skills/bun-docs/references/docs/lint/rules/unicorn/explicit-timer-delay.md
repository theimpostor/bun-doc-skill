# unicorn/explicit-timer-delay
Source: https://bun.com/docs/lint/rules/unicorn/explicit-timer-delay

Require or disallow an explicit delay for `setTimeout()` and `setInterval()`


`setTimeout(callback)` runs the callback as soon as it can, as if the delay were `0`. The reader can't tell whether that's on purpose or you forgot the delay. For `setInterval()` a forgotten delay means a callback that runs over and over without a pause. Writing `0` shows that you meant it.

The rule also checks the timers on `window`, `globalThis`, `self` and `global`.

`--fix` adds `, 0`. With `"never"`, it removes the `0`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/explicit-timer-delay" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/explicit-timer-delay" = ["error", "always"] # "always" or "never"
```


## Examples

Reported:

```js
setTimeout(() => input.focus());

window.setInterval(poll);
```

Not reported:

```js
setTimeout(() => input.focus(), 0);

window.setInterval(poll, 1000);
```

## Options

| Option | What it does |
| --- | --- |
| `"always"` (default) | Report a timer without a delay. |
| `"never"` | Report a delay of `0`, which is the same as no delay. Other delays are fine. |

```js
setTimeout(() => input.focus(), 0);
```

```js
setTimeout(() => input.focus());

setTimeout(() => input.blur(), 200);
```

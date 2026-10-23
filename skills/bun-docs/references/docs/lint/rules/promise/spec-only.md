# promise/spec-only
Source: https://bun.com/docs/lint/rules/promise/spec-only

Disallow `Promise` static methods that are not part of the language


Libraries such as Bluebird add methods like `Promise.map` and `Promise.props`. The built-in `Promise` doesn't have them, so the call throws a `TypeError` wherever the library's `Promise` isn't the one in scope.

The rule allows `all`, `allSettled`, `any`, `race`, `reject`, `resolve`, `try` and `withResolvers`. It reports every other property read from `Promise`, called or not. That includes `Promise.prototype`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"promise/spec-only" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"promise/spec-only" = ["error", {
  allowedMethods = [], # list of strings
}]
```


## Examples

Reported:

```js
const pages = await Promise.map(urls, url => fetch(url));
```

```js
const then = Promise.prototype.then;
```

Not reported:

```js
const pages = await Promise.all(urls.map(url => fetch(url)));
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowedMethods` | `[]` | More names to allow, for example from a polyfill. Names are case-sensitive. |

```js
const pages = await Promise.map(urls, url => fetch(url));
const then = Promise.prototype.then;
```

```js
const user = await Promise.props({ profile: loadProfile(), orders: loadOrders() });
```

# no-constructor-return
Source: https://bun.com/docs/lint/rules/eslint/no-constructor-return

Disallow returning a value from a constructor


If a constructor returns an object, `new` gives the caller that object instead of the new instance, so the result may not be an instance of the class. Returning a primitive such as a number is ignored, or throws a `TypeError` if the class extends another one.

A bare `return;` is allowed, so you can leave the constructor early.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-constructor-return" = "error" # or "warn"
```


## Examples

Reported:

```js
class Connection {
  constructor(url) {
    if (cache.has(url)) {
      return cache.get(url);
    }
    this.url = url;
  }
}
```

Not reported:

```js
class Connection {
  constructor(url) {
    this.url = url;
  }

  static open(url) {
    if (!cache.has(url)) {
      cache.set(url, new Connection(url));
    }
    return cache.get(url);
  }
}
```

```js
class Timer {
  constructor(delay) {
    this.delay = delay;
    if (delay === 0) {
      return;
    }
    this.start();
  }
}
```

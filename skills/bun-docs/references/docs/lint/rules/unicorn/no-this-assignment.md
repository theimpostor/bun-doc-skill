# unicorn/no-this-assignment
Source: https://bun.com/docs/lint/rules/unicorn/no-this-assignment

Disallow assigning `this` to a variable


`const self = this` exists to reach the outer `this` from a nested `function`. An arrow function keeps the `this` from the surrounding code, so you don't need the extra variable.

Only a plain variable is reported. Destructuring (`const { name } = this`) and assigning to a property (`cache.owner = this`) are fine.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-this-assignment" = "error" # or "warn"
```


## Examples

Reported:

```js
class Timer {
  start() {
    const self = this;
    setInterval(function () {
      self.tick();
    }, 1000);
  }
}
```

Not reported:

```js
class Timer {
  start() {
    setInterval(() => {
      this.tick();
    }, 1000);
  }
}
```

```js
class Timer {
  start() {
    const { interval } = this;
    registry.current = this;
    setInterval(tick, interval);
  }
}
```

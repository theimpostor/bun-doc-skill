# @typescript-eslint/no-this-alias
Source: https://bun.com/docs/lint/rules/typescript/no-this-alias

Disallow storing `this` in a variable


`const self = this` is a way to reach the outer `this` from a `function` callback, which has its own `this`. An arrow function doesn't, so inside it `this` is still the outer one. With an arrow function you don't need the extra variable, and nobody can mix up `self` and `this`.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-this-alias" = "off" # or "error"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-this-alias" = ["warn", {
  allowDestructuring = true,
  allowedNames = [], # list of strings
}]
```


## Examples

Reported:

```ts
class Timer {
  seconds = 0;

  start() {
    const self = this;
    setInterval(function () {
      self.seconds++;
    }, 1000);
  }
}
```

Not reported:

```ts
class Timer {
  seconds = 0;

  start() {
    setInterval(() => {
      this.seconds++;
    }, 1000);
  }
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowDestructuring` | `true` | Allow taking properties out of `this`: `const { seconds } = this`. |
| `allowedNames` | `[]` | Names of variables that may hold `this`. |

Reported with `allowDestructuring: false`:

```ts
class Timer {
  seconds = 0;

  report() {
    const { seconds } = this;
    return `${seconds}s`;
  }
}
```

With `allowedNames: ["self"]`, only `that` is reported:

```ts
class Timer {
  start() {
    const self = this;
    const that = this;
    return [self, that];
  }
}
```

# no-invalid-this
Source: https://bun.com/docs/lint/rules/eslint/no-invalid-this

Disallow `this` where its value is `undefined`


In strict mode, `this` is `undefined` at the top level of a module and in a plain function that's called without an object. Reading a property from it throws a `TypeError`. The usual cause is a callback written with `function` inside a method, which doesn't get the method's `this`.

`this` is fine in methods, constructors, class fields, and arrow functions inside any of them. It's also fine in a function that's given its `this`:

- with `.bind()`, `.call()` or `.apply()`
- with the last argument of `forEach()` and similar methods
- by being assigned to a property

If `this` comes from somewhere the rule can't see, say so with a `@this` tag in the function's doc comment or, in TypeScript, a `this` parameter.

Code outside strict mode isn't reported. There, `this` falls back to the global object.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-invalid-this" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-invalid-this" = ["error", {
  capIsConstructor = true,
}]
```


## Examples

Reported:

```js
export const root = this;

function describe() {
  return this.name;
}

class Cart {
  total = 0;

  add(items) {
    items.forEach(function (item) {
      this.total += item.price;
    });
  }
}
```

Not reported:

```js
const user = {
  name: "Ada",
  describe() {
    return this.name;
  },
};

class Cart {
  total = 0;

  add(items) {
    items.forEach((item) => {
      this.total += item.price;
    });
  }

  remove(items) {
    items.forEach(function (item) {
      this.total -= item.price;
    }, this);
  }
}
```

```js
const redraw = function () {
  this.clear();
}.bind(chart);

chart.reset = function () {
  this.points = [];
};

/** @this {HTMLButtonElement} */
function onClick() {
  this.disabled = true;
}
```

```ts
function onClick(this: HTMLButtonElement) {
  this.disabled = true;
}
```

Not reported in a CommonJS file without `"use strict"`:

```js
function describe() {
  return this.name;
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `capIsConstructor` | `true` | Treat a function with a capitalized name as a constructor, and allow `this` in it. |

```js
export function User(name) {
  this.name = name;
}
```

```js
export function User(name) {
  this.name = name;
}
```

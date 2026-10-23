# no-extend-native
Source: https://bun.com/docs/lint/rules/eslint/no-extend-native

Disallow adding properties to the prototypes of built-in objects


A property added to `Array.prototype` or `Object.prototype` shows up on every array or object in the program, including the ones inside libraries. It appears in their `for...in` loops, and it breaks when a library or a later version of JavaScript defines the same name with a different meaning.

Both plain assignment and `Object.defineProperty()` / `Object.defineProperties()` are reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-extend-native" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-extend-native" = ["error", {
  exceptions = [], # list of strings
}]
```


## Examples

Reported:

```js
Array.prototype.last = function () {
  return this[this.length - 1];
};

Object.defineProperty(String.prototype, "shout", {
  value() {
    return this.toUpperCase() + "!";
  },
});
```

Not reported:

```js
function last(items) {
  return items[items.length - 1];
}

class Stack extends Array {
  last() {
    return this[this.length - 1];
  }
}

Stack.prototype.peek = Stack.prototype.last;
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `exceptions` | `[]` | Names of built-in objects that you can extend. |

```js
Array.prototype.last = function () {
  return this[this.length - 1];
};
```

```js
String.prototype.shout = function () {
  return this.toUpperCase() + "!";
};
```

## When not to use it

A polyfill needs to add to built-in prototypes. List what it extends in `exceptions`, or turn the rule off for that file.

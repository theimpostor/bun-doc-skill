# unicorn/no-thenable
Source: https://bun.com/docs/lint/rules/unicorn/no-thenable

Disallow a `then` property on objects, classes, and module exports


`await` and `Promise.resolve()` treat any object with a `then` method as a promise and call that method. If an object has `then` for another reason, awaiting it hangs or gives the wrong value. A module that exports `then` does the same to `await import()`.

The rule reports `then` in an object literal, in a class, in an assignment such as `response.then = ...`, as a named export, and as the key passed to `Object.defineProperty()`, `Reflect.defineProperty()` or `Object.fromEntries()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-thenable" = "error" # or "warn"
```


## Examples

Reported:

```js
const step = {
  then(next) {
    return next;
  },
};

await step; // never finishes: `next` is not called
```

```js
class Query {
  then() {}
}

export function then() {}
```

```js
response.then = () => {};

Object.defineProperty(response, "then", { value: 1 });
```

Not reported:

```js
const step = {
  andThen(next) {
    return next;
  },
};

fetch(url).then(response => response.json());
```

## When not to use it

Turn it off where you implement a promise-like object on purpose, such as a lazy query builder that runs when it's awaited.

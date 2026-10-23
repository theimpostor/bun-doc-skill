# @typescript-eslint/no-unused-private-class-members
Source: https://bun.com/docs/lint/rules/typescript/no-unused-private-class-members

Disallow private class members that are never used


Only the class itself can use its private members. If it never uses one, that member is dead code, often left behind after a refactor.

The rule checks `#private` members, members marked `private`, and `private` parameter properties. A field that's only assigned to, or only changed with `+=` or `++`, counts as unused, because nothing ever reads the value.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unused-private-class-members" = "error" # or "warn"
```


## Examples

Reported:

```ts
class Cache {
  #size = 0;
  private hits = 0;

  constructor(private limit: number) {}

  add() {
    this.hits += 1;
  }
}
```

Not reported:

```ts
class Cache {
  #size = 0;
  private hits = 0;

  constructor(private limit: number) {}

  add() {
    this.hits += 1;
    return this.#size < this.limit ? this.hits : 0;
  }
}
```

A private setter can run code, so assigning to it counts as a use:

```ts
class Cache {
  set #limit(value: number) {
    console.log("limit is now", value);
  }

  reset() {
    this.#limit = 0;
  }
}
```

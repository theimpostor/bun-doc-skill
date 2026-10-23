# @typescript-eslint/related-getter-setter-pairs
Source: https://bun.com/docs/lint/rules/typescript/related-getter-setter-pairs

Require the type of a getter to be assignable to the type of its setter


TypeScript lets a property's getter and setter have different types. If the getter can return something the setter doesn't accept, then `field.value = field.value` is a type error, which nobody expects from a property.

The other direction is fine, so a setter can accept more than the getter returns. A getter without a return type annotation isn't checked.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/related-getter-setter-pairs" = "error" # or "warn"
```


## Examples

Reported:

```ts
interface Field {
  get value(): string | undefined;
  set value(next: string);
}
```

Not reported:

```ts
interface Field {
  get value(): string;
  set value(next: string | undefined);
}

class Width {
  #px = 0;
  get size(): number {
    return this.#px;
  }
  set size(next: number | string) {
    this.#px = Number(next);
  }
}
```

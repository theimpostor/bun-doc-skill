# @typescript-eslint/adjacent-overload-signatures
Source: https://bun.com/docs/lint/rules/typescript/adjacent-overload-signatures

Require the overloads of a function to be next to each other


When a function's overloads are spread across a file, a reader who finds the first group thinks they've seen every way to call it, and misses the one further down.

The rule looks at functions in a file, block, or namespace, and at the members of classes, interfaces, and object types. A static method and an instance method with the same name are different methods.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/adjacent-overload-signatures" = "error" # or "warn"
```


## Examples

Reported:

```ts
interface Storage {
  get(key: string): string;
  clear(): void;
  get(key: string, fallback: string): string;
}
```

```ts
declare function parse(input: string): number;
declare function format(value: number): string;
declare function parse(input: Uint8Array): number;
```

Not reported:

```ts
interface Storage {
  get(key: string): string;
  get(key: string, fallback: string): string;
  clear(): void;
}
```

```ts
class Cache {
  static create(): Cache {
    return new Cache();
  }
  size = 0;
  create(): void {}
}
```

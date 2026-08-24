# Check if two objects are deeply equal
Source: https://bun.com/docs/guides/util/deep-equals


`Bun.deepEquals()` checks if two objects are deeply equal. `expect().toEqual()` in Bun's [test runner](/docs/test/writing-tests) uses it internally.

**File:** `index.ts`
```ts
const a = { a: 1, b: 2, c: { d: 3 } };
const b = { a: 1, b: 2, c: { d: 3 } };

Bun.deepEquals(a, b); // true
```

***

Pass `true` as a third argument to enable strict mode. `expect().toStrictEqual()` uses strict mode.

The following examples return `true` in non-strict mode but `false` in strict mode.

**File:** `index.ts`
```ts
// undefined values
Bun.deepEquals({}, { a: undefined }, true); // false

// undefined in arrays
Bun.deepEquals(["asdf"], ["asdf", undefined], true); // false

// sparse arrays
Bun.deepEquals([, 1], [undefined, 1], true); // false

// object literals vs instances w/ same properties
class Foo {
  a = 1;
}
Bun.deepEquals(new Foo(), { a: 1 }, true); // false
```

***

See [Utils](/docs/runtime/utils).

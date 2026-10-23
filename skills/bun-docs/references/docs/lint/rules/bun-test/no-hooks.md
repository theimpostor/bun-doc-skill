# bun:test/no-hooks
Source: https://bun.com/docs/lint/rules/bun-test/no-hooks

Disallow `beforeAll`, `beforeEach`, `afterEach` and `afterAll`


A hook usually sets a variable that every test in the block shares. To understand one test you have to find the hooks above it, and a test that changes the shared value can break the next one. When a test calls a setup function itself, you can see everything it depends on.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/no-hooks" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"bun:test/no-hooks" = ["error", {
  allow = [], # list of "beforeAll", "beforeEach", "afterAll" or "afterEach"
}]
```


## Examples

Reported:

```ts
import { beforeEach, expect, test } from "bun:test";

let cart;

beforeEach(() => {
  cart = createCart();
});

test("starts empty", () => {
  expect(cart.items).toEqual([]);
});
```

Not reported:

```ts
import { expect, test } from "bun:test";

test("starts empty", () => {
  const cart = createCart();
  expect(cart.items).toEqual([]);
});
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allow` | `[]` | Names of hooks to allow. |

With `{ "allow": ["afterEach"] }`, only `beforeAll` is reported here:

```ts
import { afterEach, beforeAll, mock } from "bun:test";

afterEach(() => {
  mock.restore();
});

beforeAll(() => {
  server.listen();
});
```

## When not to use it

Hooks are the usual way to start something slow once per file, such as a server or a database, and to stop it afterwards. If your tests do that, allow those hooks or leave the rule off.

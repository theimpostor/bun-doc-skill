# Migrate from Jest to Bun's test runner
Source: https://bun.com/docs/guides/test/migrate-from-jest


In many cases, Bun's test runner can run Jest test suites with no code changes. Just run `bun test` instead of `npx jest`, `yarn test`, etc.

```sh
npx jest
yarn test
bun test
```

***

There's often no need for code changes.

* Bun internally re-writes imports from `@jest/globals` to use the `bun:test` equivalents.
* If you're relying on Jest to inject `test`, `expect`, etc. as globals, Bun does that too.

But if you'd rather switch to the `bun:test` imports, you can do that too.

**File:** `test.ts`
```ts
import { test, expect } from "@jest/globals";
import { test, expect } from "bun:test";
```

***

Since Bun v1.2.19, you can enable **TypeScript support** for global test functions with a single triple-slash directive. This makes migrating from Jest even easier since you only need to add the directive once in your entire project:

Add this directive to *just one file* in your project, such as:

* A `global.d.ts` file in your project root
* Your test `preload.ts` setup file (if using `preload` in bunfig.toml)
* Any single `.ts` file that TypeScript includes in your compilation

**File:** `global.d.ts`
```ts
/// <reference types="bun-types/test-globals" />
```

***

Once added, all test files in your project automatically get TypeScript support for Jest globals:

**File:** `math.test.ts`
```ts
describe("my test suite", () => {
  test("should work", () => {
    expect(1 + 1).toBe(2);
  });

  beforeAll(() => {
    // setup code
  });

  afterEach(() => {
    // cleanup code
  });
});
```

***

Bun implements the vast majority of Jest's matchers, but compatibility isn't 100% yet. Refer to the full compatibility table at [Docs > Test runner > Writing tests](/test/writing-tests#matchers).

Some notable missing features:

* `expect().toHaveReturned()`

***

If you're using `testEnvironment: "jsdom"` to run your tests in a browser-like environment, you should follow the [DOM testing with Bun and happy-dom](/guides/test/happy-dom) guide to inject browser APIs into the global scope. This guide relies on [`happy-dom`](https://github.com/capricorn86/happy-dom), which is a leaner and faster alternative to [`jsdom`](https://github.com/jsdom/jsdom).

At the moment jsdom does not work in Bun due to its internal use of V8 APIs. Track support for it [here](https://github.com/oven-sh/bun/issues/3554).

**File:** `bunfig.toml`
```toml
[test]
preload = ["./happy-dom.ts"]
```

***

Replace `bail` in your Jest config with the `--bail` CLI flag.

```sh
bun test --bail=3
```

***

Replace `collectCoverage` with the `--coverage` CLI flag.

```sh
bun test --coverage
```

***

Replace `testTimeout` with the `--test-timeout` CLI flag.

```sh
bun test --timeout 10000
```

***

Many other flags become irrelevant or obsolete when using `bun test`.

* `transform` — Bun supports TypeScript & JSX. Other file types can be configured with [Plugins](/runtime/plugins).
* `extensionsToTreatAsEsm`
* `haste` — Bun uses it's own internal source maps
* `watchman`, `watchPlugins`, `watchPathIgnorePatterns` — use `--watch` to run tests in watch mode
* `verbose` — set `logLevel: "debug"` in [`bunfig.toml`](/runtime/bunfig#loglevel)

***

Settings that aren't mentioned here are not supported or have no equivalent. Please [file a feature request](https://github.com/oven-sh/bun) if something important is missing.

***

See also:

* [Mark a test as a todo](/guides/test/todo-tests)
* [Docs > Test runner > Writing tests](/test/writing-tests)

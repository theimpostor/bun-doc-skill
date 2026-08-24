# Spy on methods in `bun test`
Source: https://bun.com/docs/guides/test/spy-on


Use the `spyOn` utility to track method calls with Bun's test runner.

```ts
import { test, expect, spyOn } from "bun:test";

const leo = {
  name: "Leonardo",
  sayHi(thing: string) {
    console.log(`Sup I'm ${this.name} and I like ${thing}`);
  },
};

const spy = spyOn(leo, "sayHi");
```

***

Once you've created the spy, use it in `expect` assertions about method calls.

```ts
import { test, expect, spyOn } from "bun:test";

const leo = {
  name: "Leonardo",
  sayHi(thing: string) {
    console.log(`Sup I'm ${this.name} and I like ${thing}`);
  },
};

const spy = spyOn(leo, "sayHi");

test("turtles", () => {
  expect(spy).toHaveBeenCalledTimes(0);
  leo.sayHi("pizza");
  expect(spy).toHaveBeenCalledTimes(1);
  expect(spy.mock.calls).toEqual([["pizza"]]);
});
```

***

See [Mocks](/docs/test/mocks).

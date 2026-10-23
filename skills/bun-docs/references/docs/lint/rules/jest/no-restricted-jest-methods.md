# jest/no-restricted-jest-methods
Source: https://bun.com/docs/lint/rules/jest/no-restricted-jest-methods

Disallow the `jest` methods that you list


Some teams agree not to use parts of the `jest` object, like module mocks, fake timers or spies. This rule reports the methods you list, with your own message if you give one, so the agreement doesn't depend on review.

The rule does nothing until you give it a list.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/no-restricted-jest-methods" = "error" # or "warn"
```


## Examples

These examples restrict `advanceTimersByTime` and `spyOn`.

Reported:

```ts
import { expect, jest, test } from "@jest/globals";

test("retries after a second", () => {
  const send = jest.spyOn(mailer, "send");
  retry(send);
  jest.advanceTimersByTime(1000);
  expect(send).toHaveBeenCalledTimes(2);
});
```

Not reported:

```ts
import { expect, jest, test } from "@jest/globals";

test("retries once", () => {
  const send = jest.fn();
  retry(send);
  expect(send).toHaveBeenCalledTimes(2);
});
```

## Options

The rule takes one object. Each key is a method name. The value is the message to report, or `null` for the default message: ``Use of `spyOn` is not allowed``.

**File:** `.oxlintrc.json`
```json
{
  "plugins": ["jest"],
  "rules": {
    "jest/no-restricted-jest-methods": [
      "error",
      {
        "advanceTimersByTime": null,
        "spyOn": "Pass the dependency in instead of spying on it"
      }
    ]
  }
}
```

# jest/prefer-jest-mocked
Source: https://bun.com/docs/lint/rules/jest/prefer-jest-mocked

Require `jest.mocked(fn)` instead of `fn as jest.Mock`


`fetchUser as jest.Mock` replaces the function's type with a mock of anything, so `mockReturnValue` accepts a value that the real function can never return. `jest.mocked(fetchUser)` keeps the parameters and the return type, so a mock value with the wrong shape is a type error.

The rule reports a cast to `jest.Mock`, `jest.MockedFunction`, `jest.MockedClass` or `jest.MockedObject`, with or without type arguments.

`--fix` rewrites the cast to `jest.mocked()`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"jest/prefer-jest-mocked" = "error" # or "warn"
```


## Examples

Reported:

```ts
import { jest } from "@jest/globals";
import { fetchUser, saveUser } from "./api";

jest.mock("./api");

(fetchUser as jest.Mock).mockReturnValue({ name: "Ada" });
const mockSaveUser = saveUser as jest.MockedFunction<typeof saveUser>;
```

Not reported:

```ts
import { jest } from "@jest/globals";
import { fetchUser, saveUser } from "./api";

jest.mock("./api");

jest.mocked(fetchUser).mockReturnValue({ name: "Ada" });
const mockSaveUser = jest.mocked(saveUser);
```

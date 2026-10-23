# @typescript-eslint/no-unsafe-member-access
Source: https://bun.com/docs/lint/rules/typescript/no-unsafe-member-access

Disallow reading a property of a value of type `any`


TypeScript doesn't check a property that you read from an `any` value. A typo in the name, or a missing object in the middle of a chain, only shows up when the code runs. The result is `any` again, so the code that uses it isn't checked either.

In a chain such as `response.user.name`, only the first unsafe step is reported.

`bun lint --type-aware` turns this rule on in TypeScript files.


## Configure

Off by default. This rule needs types, so turning it on makes `bun lint` type check your code first.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unsafe-member-access" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unsafe-member-access" = ["error", {
  allowOptionalChaining = false,
}]
```


## Examples

Reported:

```ts
function readName(response: any) {
  return response.user.name;
}
```

Not reported:

```ts
interface UserResponse {
  user: { name: string };
}

function readName(response: UserResponse) {
  return response.user.name;
}
```

An `any` value used as the key is reported too, because the result can be any property of the object:

```ts
function pick(prices: number[], key: any) {
  return prices[key];
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowOptionalChaining` | `false` | Allow `?.` on an `any` value. |

```ts
function readUser(response: any) {
  return response?.user;
}
```

Each step needs its own `?.`. Here `.name` is still reported:

```ts
function readName(response: any) {
  return response?.user.name;
}
```

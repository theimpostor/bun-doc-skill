# @typescript-eslint/no-confusing-non-null-assertion
Source: https://bun.com/docs/lint/rules/typescript/no-confusing-non-null-assertion

Disallow a non-null assertion `!` right before `=`, `==`, `===`, `in` or `instanceof`


`user! == other` asserts that `user` isn't null and then tests for equality. It reads like `user !== other`, which means the opposite. In the same way, `count! = 1` looks like `count != 1`, and `key! in cache` looks like `!(key in cache)`.

The report comes with a suggestion to remove the `!`, or to put the left side in parentheses.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-confusing-non-null-assertion" = "error" # or "warn"
```


## Examples

Reported:

```ts
declare let user: string | undefined;
declare const cache: Record<string, number>;

const isSame = user! == "ada";
user! = "grace";
const isCached = user! in cache;
```

Not reported:

```ts
declare let user: string | undefined;
declare const cache: Record<string, number>;

const isSame = user == "ada";
user = "grace";
const isCached = (user!) in cache;
const isOther = "ada" == user!;
```

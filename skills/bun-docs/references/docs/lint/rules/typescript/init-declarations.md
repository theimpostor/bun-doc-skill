# @typescript-eslint/init-declarations
Source: https://bun.com/docs/lint/rules/typescript/init-declarations

Require or disallow a value in variable declarations


A variable declared without a value is `undefined` until a later line assigns it. If one branch skips the assignment, the code after it reads `undefined`. `"always"` requires a value in every declaration. `"never"` requires the opposite style: declare first, assign later.

It's the TypeScript version of `init-declarations`. A `declare let` and the variables in a `declare namespace` can't have a value, so `"always"` doesn't report them.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/init-declarations" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
# "always" or "never"
"@typescript-eslint/init-declarations" = ["error", "always"]
```


## Examples

Reported:

```ts
let discount: number;

if (isMember) {
  discount = 10;
}
```

Not reported:

```ts
let discount = 0;

if (isMember) {
  discount = 10;
}

declare let isMember: boolean;
```

## Options

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/init-declarations" = ["error", "always"]
```

| Option | What it does |
| --- | --- |
| `"always"` | Report a `var` or `let` that has no value. |
| `"never"` | Report a `var` or `let` that has a value. `const` and `using` need one, so they're allowed. |

The default is `"always"`:

```ts
let discount: number;
```

With `"never"`:

```ts
let discount = 0;
```

```ts
let discount: number;
const rate = 0.2;

discount = 100 * rate;
```

With `"never"`, a second option `{ "ignoreForLoopInit": true }` allows the variable in the head of a `for` loop. It's `false` by default.

```ts
for (let i = 0; i < 3; i++) {
  console.log(i);
}
```

```ts
for (let i = 0; i < 3; i++) {
  console.log(i);
}
```

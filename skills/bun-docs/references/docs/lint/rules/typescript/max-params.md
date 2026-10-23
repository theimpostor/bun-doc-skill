# @typescript-eslint/max-params
Source: https://bun.com/docs/lint/rules/typescript/max-params

Enforce a maximum number of parameters in function definitions


A call like `createUser("Ada", "ada@example.com", true, false)` says nothing about what each argument means, and you can swap two arguments of the same type without getting an error. Past three parameters, one object with named properties is easier to read and to extend.

It's the TypeScript version of `max-params`. It checks function types too, and it doesn't count a `this: void` parameter.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/max-params" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/max-params" = ["error", {
  max = 3,
  # maximum = <number>,
  countVoidThis = false,
}]
```


## Examples

Reported:

```ts
function createUser(name: string, email: string, isAdmin: boolean, isActive: boolean) {
  return { name, email, isAdmin, isActive };
}
```

Not reported:

```ts
interface NewUser {
  name: string;
  email: string;
  isAdmin: boolean;
  isActive: boolean;
}

function createUser(user: NewUser) {
  return { ...user };
}

function move(this: void, x: number, y: number, z: number) {}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `max` | `3` | The number of parameters a function can have. |
| `maximum` | | An older name for `max`. |
| `countVoidThis` | `false` | Count a `this: void` parameter like any other. |

```ts
type Add = (left: number, right: number) => number;
```

```ts
function move(this: void, x: number, y: number, z: number) {}
```

A `this` parameter of any other type is always counted:

```ts
function move(this: Window, x: number, y: number, z: number) {}
```

# @typescript-eslint/no-empty-object-type
Source: https://bun.com/docs/lint/rules/typescript/no-empty-object-type

Disallow the `{}` type and empty interfaces


`{}` doesn't mean "an object with no properties". It accepts every value except `null` and `undefined`, so `0`, `""` and `[]` all pass. An interface with no members behaves the same way. Use `object` for "any object", `unknown` for "any value", and `Record<string, never>` for an object that has no properties.

An empty interface that extends one other type is reported too, because it's only a second name for that type.

`{}` in an intersection, such as `T & {}`, isn't reported. There it's a way to remove `null` and `undefined` from `T`.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-empty-object-type" = "off" # or "error"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-empty-object-type" = ["warn", {
  allowInterfaces = "never", # "always", "never" or "with-single-extends"
  allowObjectTypes = "never", # "always" or "never"
  # allowWithName = <string>,
}]
```


## Examples

Reported:

```ts
let settings: {} = 42; // no type error

interface Props {}
```

Not reported:

```ts
let settings: object = { theme: "dark" };
let payload: unknown = 42;
let nothing: Record<string, never> = {};

type Defined<T> = T & {};
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowInterfaces` | `"never"` | `"always"` allows every empty interface. `"with-single-extends"` allows one that extends one type. |
| `allowObjectTypes` | `"never"` | `"always"` allows the `{}` type. |
| `allowWithName` | none | A regular expression. An empty interface, or a type alias for `{}`, is allowed if its name matches. |

```ts
interface User {
  name: string;
}

interface Admin extends User {}
```

With `allowWithName`, you can allow a component's empty props and nothing else:

```ts
interface HeaderProps {}

type FooterProps = {};
```

```ts
interface HeaderState {}
```

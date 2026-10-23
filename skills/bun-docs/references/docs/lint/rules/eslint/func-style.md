# func-style
Source: https://bun.com/docs/lint/rules/eslint/func-style

Enforce one way to define functions: declarations, or expressions assigned to variables


A function declaration can be called above the line that defines it. A function assigned to a variable only exists after that line has run. If a project mixes both, you have to check how each function is written to know where it can be called.

This rule makes you pick one. By default it asks for expressions.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"func-style" = "error" # or "warn"
```

Every option, set to its default. The ones that are commented out are unset by default.

**File:** `bunfig.toml`
```toml
[lint.rules]
"func-style" = [
  "error",
  "expression", # "declaration" or "expression"
  {
    allowArrowFunctions = false,
    allowTypeAnnotation = false,
    overrides = {
      # namedExports = <"declaration", "expression" or "ignore">,
    },
  },
]
```


## Examples

Reported:

```js
function formatName(user) {
  return `${user.first} ${user.last}`;
}
```

Not reported:

```js
const formatName = function (user) {
  return `${user.first} ${user.last}`;
};

const initials = (user) => user.first[0] + user.last[0];
```

`export default function` is never reported, and neither is a TypeScript function that has overload signatures:

```ts
export default function main() {}

function parse(input: string): string;
function parse(input: number): number;
function parse(input: string | number) {
  return input;
}
```

## Options

**File:** `bunfig.toml`
```toml
[lint.rules]
func-style = ["error", "declaration", { allowArrowFunctions = true }]
```

| Option | What it does |
| --- | --- |
| `"expression"` (default) | Report function declarations. |
| `"declaration"` | Report functions assigned to a variable where it's declared. |

| Option | Default | What it does |
| --- | --- | --- |
| `allowArrowFunctions` | `false` | With `"declaration"`, allow arrow functions. |
| `allowTypeAnnotation` | `false` | With `"declaration"`, allow a function if its variable has a type annotation. |
| `overrides.namedExports` | not set | The style for `export function` and `export const`: `"declaration"`, `"expression"`, or `"ignore"` for either. |

### `"declaration"`

```js
const formatName = function (user) {
  return `${user.first} ${user.last}`;
};

const initials = (user) => user.first[0] + user.last[0];
```

```js
function formatName(user) {
  return `${user.first} ${user.last}`;
}
```

An arrow function that uses `this` isn't reported, because `this` would mean something else in a declaration:

```js
function Timer() {
  const tick = () => {
    this.seconds++;
  };
  setInterval(tick, 1000);
}
```

### `allowArrowFunctions`

```js
const initials = (user) => user.first[0] + user.last[0];
```

### `allowTypeAnnotation`

You can't give a declaration a function type as a whole, so this option lets those functions stay expressions:

```ts
type Handler = (event: Event) => void;

const onClick: Handler = (event) => {
  event.preventDefault();
};
```

### `overrides.namedExports`

```js
export function formatName(user) {
  return user.name;
}

const trim = function (text) {
  return text.trim();
};
```

```js
export const formatName = function (user) {
  return user.name;
};
```

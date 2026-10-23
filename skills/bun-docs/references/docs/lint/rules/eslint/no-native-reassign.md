# no-native-reassign
Source: https://bun.com/docs/lint/rules/eslint/no-native-reassign

Disallow assignments to built-in and other read-only global variables


Nothing stops you from writing `Object = null`. Every piece of code that runs afterwards, including libraries, sees the new value and breaks far from the assignment. Most of the time it's a typo or a missing `const`.

The rule reports every write to a global that's marked as read-only, including writes with `+=`, `++` or destructuring. Your own variable with the same name is fine.

ESLint has deprecated this rule. `no-global-assign` is its current name and does the same thing.

## Examples

Reported:

```js
Promise = require("bluebird");
```

```js
[Map, Set] = polyfills;
```

Not reported:

```js
const Promise = require("bluebird");
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `exceptions` | `[]` | Names of globals that can be assigned to. |

```js
Promise = require("bluebird");
```

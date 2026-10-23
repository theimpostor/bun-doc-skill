# unicorn/no-anonymous-default-export
Source: https://bun.com/docs/lint/rules/unicorn/no-anonymous-default-export

Require a name for a function or class that is the default export


A default export without a name gives you nothing to search for, and every file that imports it makes up its own name. Stack traces show it as `default` or `<anonymous>`.

The rule looks at functions and classes, in `export default` and in `module.exports =`. Other values, such as objects and numbers, aren't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/no-anonymous-default-export" = "error" # or "warn"
```


## Examples

Reported:

```js
export default function (user) {
  return `${user.first} ${user.last}`;
}
```

```js
export default (user) => `${user.first} ${user.last}`;
```

```js
module.exports = class {
  items = [];
};
```

Not reported:

```js
export default function fullName(user) {
  return `${user.first} ${user.last}`;
}
```

An arrow function doesn't have a name. Give it one with a variable:

```js
const fullName = (user) => `${user.first} ${user.last}`;

export default fullName;
```

```js
module.exports = class Cart {
  items = [];
};
```

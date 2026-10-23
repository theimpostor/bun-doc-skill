# no-catch-shadow
Source: https://bun.com/docs/lint/rules/eslint/no-catch-shadow

Disallow a `catch` parameter with the name of a variable in the scope around it


In Internet Explorer 8 and earlier, a `catch` clause's parameter leaks into the surrounding scope. If a variable there has the same name, the caught error overwrites it.

The rule reports a `catch` parameter that has the same name as a variable, function, class or global that's visible at the `try` statement.

ESLint has deprecated this rule. Use `no-shadow` instead.

## Examples

Reported:

```js
const error = loadLastError();

try {
  save();
} catch (error) {
  console.log(error);
}
```

Not reported:

```js
const error = loadLastError();

try {
  save();
} catch (saveError) {
  console.log(saveError);
}
```

## When not to use it

Every current browser and runtime keeps the parameter inside the `catch` clause, so this rule only matters for Internet Explorer 8. It's deprecated. To stop names from hiding each other, use `no-shadow`.

# no-new-object
Source: https://bun.com/docs/lint/rules/eslint/no-new-object

Disallow `new Object()` in favor of `{}`


`new Object()` creates the same empty object as `{}`. The literal is shorter and lets you list the properties in place.

ESLint has deprecated this rule. Use `no-object-constructor` instead, which also reports `Object()` without `new`.

## Examples

Reported:

```js
const headers = new Object();
headers.accept = "text/html";
```

Not reported:

```js
const headers = { accept: "text/html" };
```

# prefer-reflect
Source: https://bun.com/docs/lint/rules/eslint/prefer-reflect

Require `Reflect` methods instead of their older `Object` and `Function` forms


`Reflect` puts the low-level object operations in one place, as plain functions. For example, `Reflect.defineProperty()` returns `false` where `Object.defineProperty()` throws.

The rule reports `delete` on a property, and every call to a method with one of these names on anything but `Reflect`: `apply`, `call`, `defineProperty`, `getOwnPropertyDescriptor`, `getPrototypeOf`, `setPrototypeOf`, `isExtensible`, `getOwnPropertyNames`, `preventExtensions`.

## Examples

Reported:

```js
save.apply(user, args);
save.call(user, "draft");
Object.defineProperty(user, "id", { value: 1 });
delete user.email;
```

Not reported:

```js
Reflect.apply(save, user, args);
Reflect.apply(save, user, ["draft"]);
Reflect.defineProperty(user, "id", { value: 1 });
Reflect.deleteProperty(user, "email");
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `exceptions` | `[]` | Names to allow: any of the method names above, or `"delete"`. |

```js
delete user.email;
save.call(user, "draft");
```

```js
save.apply(user, args);
```

## When not to use it

ESLint has deprecated this rule, and the older forms aren't going away. The rule only goes by the method's name, so `phone.call(number)` is reported. For `Object.getOwnPropertyNames` it points you to `Reflect.getOwnPropertyNames`, which doesn't exist.

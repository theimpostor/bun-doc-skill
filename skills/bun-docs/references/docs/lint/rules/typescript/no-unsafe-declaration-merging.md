# @typescript-eslint/no-unsafe-declaration-merging
Source: https://bun.com/docs/lint/rules/typescript/no-unsafe-declaration-merging

Disallow a class and an interface with the same name


A class and an interface with the same name in the same scope merge into one type. The compiler then believes that every instance has the interface's properties, but it never checks that the class sets them. Reading one gives you `undefined` where the type promises a value.

Both declarations are reported.

This rule is on by default in TypeScript files.


## Configure

On by default as a warning. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-unsafe-declaration-merging" = "off" # or "error"
```


## Examples

Reported:

```ts
interface User {
  name: string;
}

class User {}

// No compile error, but it throws when it runs.
console.log(new User().name.length);
```

Not reported:

```ts
interface Named {
  name: string;
}

class User implements Named {
  name = "anonymous";
}

console.log(new User().name.length);
```

Other kinds of merging aren't reported:

```ts
interface Options {
  verbose: boolean;
}

interface Options {
  color: boolean;
}

class Logger {}

namespace Logger {
  export const level = "info";
}
```

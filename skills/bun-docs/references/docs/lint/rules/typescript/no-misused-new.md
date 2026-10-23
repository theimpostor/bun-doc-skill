# @typescript-eslint/no-misused-new
Source: https://bun.com/docs/lint/rules/typescript/no-misused-new

Disallow `new` in a class and `constructor` in an interface


A class declares its constructor with `constructor`. An interface describes one with `new ()`. Swap them and you get an ordinary method. `new(): Client` in a class is a method named `new`, and `constructor(): void` in an interface is a method named `constructor`.

An interface with a `new ()` that returns the interface itself is reported too. It says that you call `new` on an instance to get another instance, which is rarely what you mean. The `new ()` belongs in the type of the class.

A method named `new` that has a body, or that returns some other type, isn't reported.

This rule is on by default in TypeScript files.


## Configure

On by default as an error. To turn it off:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-misused-new" = "off" # or "warn"
```


## Examples

Reported:

```ts
declare class Client {
  new(): Client;
}

interface Session {
  new (): Session;
  constructor(): void;
}
```

Not reported:

```ts
declare class Client {
  constructor();
}

interface Session {
  id: string;
}

interface SessionConstructor {
  new (): Session;
}

class Factory {
  new() {
    return new Client();
  }
}
```

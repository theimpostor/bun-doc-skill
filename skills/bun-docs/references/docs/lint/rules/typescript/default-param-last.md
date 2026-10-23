# @typescript-eslint/default-param-last
Source: https://bun.com/docs/lint/rules/typescript/default-param-last

Require parameters with a default value, and optional parameters, to come last


A default value only applies when the argument is left out or is `undefined`. If a required parameter follows, the caller can't leave the first one out and has to pass `undefined` to get the default.

Optional parameters (`label?: string`) are treated like parameters with a default.

It's the TypeScript version of `default-param-last` and reports the same code.

With `bunfig.toml` you can set either name. `bun lint` runs this rule in TypeScript files and `default-param-last` in JavaScript files, so nothing is reported twice. With an ESLint config, turn on only one of the two.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/default-param-last" = "error" # or "warn"
```


## Examples

Reported:

```ts
function connect(port = 3000, host: string) {}

connect(undefined, "localhost");
```

```ts
function connect(port?: number, host: string) {}
```

```ts
class Client {
  constructor(private retries = 3, private url: string) {}
}
```

Not reported:

```ts
function connect(host: string, port = 3000) {}

connect("localhost");
```

```ts
function request(url: string, retries = 3, label?: string, ...headers: string[]) {}
```

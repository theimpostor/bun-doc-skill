# import/no-named-as-default-member
Source: https://bun.com/docs/lint/rules/import/no-named-as-default-member

Disallow reading a property of a default import that is also a named export of the module


After `import config from "./config"`, `config.load` is a property of the default export. It isn't the module's named export `load`. If the default export doesn't have that property, you get `undefined`. If it does, a named import says the same thing more directly and lets bundlers drop the exports you don't use.

The rule reads the imported module and reports `config.load` and `const { load } = config` if the module has a named export `load`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-named-as-default-member" = "error" # or "warn"
```


## Examples

Reported:

**File:** `config.js`
```js
export function load(path) {
  return JSON.parse(read(path));
}

export default { port: 3000 };
```

```js
import config from "./config";

config.load("./app.json");
const { load } = config;
```

Not reported:

**File:** `config.js`
```js
export function load(path) {
  return JSON.parse(read(path));
}

export default { port: 3000 };
```

```js
import config, { load } from "./config";

load("./app.json");
listen(config.port);
```

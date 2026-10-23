# import/default
Source: https://bun.com/docs/lint/rules/import/default

Require a default import to match a default export in the imported file


`import save from "./storage"` asks for the default export of `./storage`. If that file only has named exports, the import fails when the module loads, or a bundler gives you `undefined`. The usual cause is missing braces.

The rule reads the imported file. It doesn't report anything if the file can't be found, or if it has no `import` or `export` at all, like a CommonJS module.

It reads JavaScript and TypeScript files, including JSX. With an ESLint config it only reads `.js`, `.mjs` and `.cjs` files, unless `settings["import/extensions"]` lists others.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/default" = "error" # or "warn"
```


## Examples

Reported:

```js
export function save(item) {
  localStorage.setItem(item.id, JSON.stringify(item));
}
```

```js
import save from "./storage.js";

save({ id: "draft" });
```

Not reported:

```js
export function save(item) {
  localStorage.setItem(item.id, JSON.stringify(item));
}
```

```js
import { save } from "./storage.js";

save({ id: "draft" });
```

```js
export default function save(item) {
  localStorage.setItem(item.id, JSON.stringify(item));
}
```

```js
import save from "./storage.js";

save({ id: "draft" });
```

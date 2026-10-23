# no-useless-rename
Source: https://bun.com/docs/lint/rules/eslint/no-useless-rename

Disallow renaming an import, export, or destructured value to the same name


`import { user as user }` and `const { id: id } = user` rename something to the name it already has. The short form means the same thing.

`--fix` removes the rename.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-useless-rename" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"no-useless-rename" = ["error", {
  ignoreImport = false,
  ignoreExport = false,
  ignoreDestructuring = false,
}]
```


## Examples

Reported:

```js
import { load as load } from "./store.js";

const { id: id } = load();

export { id as id };
```

Not reported:

```js
import { load } from "./store.js";
import { save as saveUser } from "./users.js";

const { id, name: userName } = load();

export { id, userName as name };
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `ignoreImport` | `false` | Don't check imports. |
| `ignoreExport` | `false` | Don't check exports. |
| `ignoreDestructuring` | `false` | Don't check destructuring. |

```js
const { id: id } = user;
```

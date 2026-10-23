# import/no-deprecated
Source: https://bun.com/docs/lint/rules/import/no-deprecated

Disallow importing and using names that are marked `@deprecated`


A `@deprecated` tag in a doc comment says that an export is going away, but nothing stops new code from importing it. This rule reads the module you import from and reports the import and each use of a deprecated name. The message repeats the text after the tag, which usually says what to use instead.

A member of a namespace import, such as `api.fetchUser` after `import * as api`, is checked as well.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-deprecated" = "error" # or "warn"
```


## Examples

Reported, once at the import and once at the call:

**File:** `api.js`
```js
/** @deprecated Use loadUser() instead. */
export const fetchUser = id => loadUser(id);

export const loadUser = id => fetch(`/users/${id}`);
```

```js
import { fetchUser } from "./api";

fetchUser(1);
```

With the same `api.js`, this is reported at `fetchUser`:

**File:** `api.js`
```js
/** @deprecated Use loadUser() instead. */
export const fetchUser = id => loadUser(id);

export const loadUser = id => fetch(`/users/${id}`);
```

```js
import * as api from "./api";

api.fetchUser(1);
```

Not reported:

**File:** `api.js`
```js
/** @deprecated Use loadUser() instead. */
export const fetchUser = id => loadUser(id);

export const loadUser = id => fetch(`/users/${id}`);
```

```js
import { loadUser } from "./api";

loadUser(1);
```

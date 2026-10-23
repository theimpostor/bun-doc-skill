# import/no-empty-named-blocks
Source: https://bun.com/docs/lint/rules/import/no-empty-named-blocks

Disallow `import {} from` with nothing between the braces


Empty braces in an import are usually left over after someone deleted the last name. The import still loads and runs the module, but it doesn't say whether that's on purpose.

`--fix` removes the braces if the import also has a default import. An import that has nothing but `{}` isn't fixed, because deleting it would stop the module from being loaded. It comes with two suggestions instead: delete the import, or keep it as `import "./setup"`.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-empty-named-blocks" = "error" # or "warn"
```


## Examples

Reported:

```js
import {} from "./setup";
```

```js
import React, {} from "react";
```

```ts
import type {} from "./types";
```

Not reported:

```js
import "./setup";
import React from "react";
import { useState } from "react";
```

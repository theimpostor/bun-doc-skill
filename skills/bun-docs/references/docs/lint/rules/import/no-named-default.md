# import/no-named-default
Source: https://bun.com/docs/lint/rules/import/no-named-default

Disallow `import { default as name }` in favor of `import name`


`import { default as React } from "react"` and `import React from "react"` do the same thing. The second is shorter, and it's the form readers expect.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"import/no-named-default" = "error" # or "warn"
```


## Examples

Reported:

```js
import { default as React, useState } from "react";
```

```ts
import type { default as User } from "./user";
```

Not reported:

```js
import React, { useState } from "react";
```

```ts
import type User from "./user";
```

A name marked with `type` inside the braces isn't reported either:

```ts
import { type default as User, loadUser } from "./user";
```

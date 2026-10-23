# @typescript-eslint/no-var-requires
Source: https://bun.com/docs/lint/rules/typescript/no-var-requires

Disallow `const x = require()` in favor of `import`


In a TypeScript file, `require()` returns `any`, so `const fs = require("node:fs")` loses all the module's types. An `import` keeps them.

The rule reports `require()` in a variable declaration, and where its result is called, passed to a function, read from with `.` or `[]`, or given a type with `as`. A bare `require("./setup");` and `import fs = require("fs")` are allowed, and so is your own function named `require`.

This rule is deprecated. Use `@typescript-eslint/no-require-imports` instead.

## Examples

Reported:

```ts
const fs = require("node:fs");
const join = require("node:path").join;
register(require("./plugin"));
```

Not reported:

```ts
import fs from "node:fs";
import { join } from "node:path";
import legacy = require("./legacy");

require("./setup");
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allow` | `[]` | Regular expressions. A `require()` of a path that matches one of them is allowed. |

```ts
const pkg = require("../package.json");
```

```ts
const data = require("../data.json");
```

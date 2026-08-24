# Add a tarball dependency
Source: https://bun.com/docs/guides/install/add-tarball


Bun's package manager can install any publicly available tarball URL as a dependency of your project.

```sh
bun add zod@https://registry.npmjs.org/zod/-/zod-3.21.4.tgz
```

***

This command downloads, extracts, and installs the tarball into your project's `node_modules` directory, and adds the following line to your `package.json`:

**File:** `package.json`
```json
{
  "dependencies": {
    "zod": "https://registry.npmjs.org/zod/-/zod-3.21.4.tgz"
  }
}
```

***

You can now import `zod` as usual.

```ts
import { z } from "zod";
```

***

See [`bun install`](/docs/pm/cli/install).

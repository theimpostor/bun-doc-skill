# Install a package under a different name
Source: https://bun.com/docs/guides/install/npm-alias


To install an npm package under an alias:

```sh
bun add my-custom-name@npm:zod
```

***

You can now import the `zod` package as `my-custom-name`.

**File:** `index.ts`
```ts
import { z } from "my-custom-name";

z.string();
```

***

See [`bun install`](/docs/pm/cli/install).

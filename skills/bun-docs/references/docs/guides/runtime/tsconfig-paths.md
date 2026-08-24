# Re-map import paths
Source: https://bun.com/docs/guides/runtime/tsconfig-paths


Bun reads the `paths` field in your `tsconfig.json` to re-write import paths. This is useful for aliasing package names or avoiding long relative paths.

**File:** `tsconfig.json`
```json
{
  "compilerOptions": {
    "paths": {
      "my-custom-name": ["./node_modules/zod"],
      "@components/*": ["./src/components/*"]
    }
  }
}
```

***

With this `tsconfig.json`, Bun re-writes the following imports:

**File:** `tsconfig.ts`
```ts
import { z } from "my-custom-name"; // imports from "zod"
import { Button } from "@components/Button"; // imports from "./src/components/Button"
```

***

See [TypeScript](/docs/runtime/typescript).

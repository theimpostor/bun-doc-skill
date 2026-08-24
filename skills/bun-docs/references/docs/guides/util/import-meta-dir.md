# Get the directory of the current file
Source: https://bun.com/docs/guides/util/import-meta-dir


Bun provides a handful of module-specific utilities on the [`import.meta`](/docs/runtime/module-resolution#import-meta) object. Use `import.meta.dir` to retrieve the absolute path to the directory containing the current file.

**File:** `/a/b/c.ts`
```ts
import.meta.dir; // => "/a/b"
```

***

See [`import.meta`](/docs/runtime/module-resolution#import-meta).

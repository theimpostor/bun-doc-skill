# Inspect memory usage using V8 heap snapshots
Source: https://bun.com/docs/guides/runtime/heap-snapshot


Bun implements V8's heap snapshot API, which allows you to create snapshots of the heap at runtime. This helps debug memory leaks in your JavaScript/TypeScript application.

**File:** `snapshot.ts`
```ts
import v8 from "node:v8";

// Creates a heap snapshot file with an auto-generated name
const snapshotPath = v8.writeHeapSnapshot();
console.log(`Heap snapshot written to: ${snapshotPath}`);
```

***

## Inspect memory in Chrome DevTools

To view V8 heap snapshots in Chrome DevTools:

1. Open Chrome DevTools (F12 or right-click and select "Inspect")
2. Go to the "Memory" tab
3. Click the "Load" button (folder icon)
4. Select your `.heapsnapshot` file

<img alt="Chrome DevTools Memory Tab" />

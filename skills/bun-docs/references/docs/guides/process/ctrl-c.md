# Listen for CTRL+C
Source: https://bun.com/docs/guides/process/ctrl-c


The `ctrl+c` shortcut sends an *interrupt signal* to the running process. This signal can be intercepted by listening for the `SIGINT` event. If you want to close the process, you must explicitly call `process.exit()`.

**File:** `process.ts`
```ts
process.on("SIGINT", () => {
  console.log("Ctrl-C was pressed");
  process.exit();
});
```

***

See [Docs > API > Utils](/runtime/utils) for more useful utilities.

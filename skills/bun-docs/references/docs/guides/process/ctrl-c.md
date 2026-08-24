# Listen for CTRL+C
Source: https://bun.com/docs/guides/process/ctrl-c


The `ctrl+c` shortcut sends an *interrupt signal* to the running process. Intercept it by listening for the `SIGINT` event. To close the process, you must explicitly call `process.exit()`.

**File:** `process.ts`
```ts
process.on("SIGINT", () => {
  console.log("Ctrl-C was pressed");
  process.exit();
});
```

***

See [Utils](/docs/runtime/utils) for more utilities.

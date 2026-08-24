# Spawn a child process and communicate using IPC
Source: https://bun.com/docs/guides/process/ipc


Use [`Bun.spawn()`](/docs/runtime/child-process) to spawn a child process. When spawning a second `bun` process, you can open a direct inter-process communication (IPC) channel between the two processes.

> Note
To communicate with a Node.js process, set `serialization: "json"` in `Bun.spawn`. Use `process.execPath` to get a
path to the currently running `bun` executable.

**File:** `parent.ts`
```ts
const child = Bun.spawn(["bun", "child.ts"], {
  ipc(message) {
    /**
     * The message received from the sub process
     **/
  },
});
```

***

The parent process sends messages to the subprocess with the `.send()` method on the returned `Subprocess` instance. The `ipc` handler also receives the subprocess as its second argument.

**File:** `parent.ts`
```ts
const childProc = Bun.spawn(["bun", "child.ts"], {
  ipc(message, childProc) {
    /**
     * The message received from the sub process
     **/
    childProc.send("Respond to child");
  },
});

childProc.send("I am your father"); // The parent can send messages to the child as well
```

***

The child process sends messages to its parent with `process.send()` and receives messages with `process.on("message")`. This is the same API used for `child_process.fork()` in Node.js.

**File:** `child.ts`
```ts
process.send("Hello from child as string");
process.send({ message: "Hello from child as object" });

process.on("message", message => {
  // print message from parent
  console.log(message);
});
```

***

By default, Bun serializes messages with the JSC `serialize` API. This API supports everything [`structuredClone` supports](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm), including strings, typed arrays, and objects. The API does not support transferring ownership of objects.

**File:** `child.ts`
```ts
// send a string
process.send("Hello from child as string");

// send an object
process.send({ message: "Hello from child as object" });
```

***

See [Child processes](/docs/runtime/child-process).

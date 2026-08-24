# Hot reload an HTTP server
Source: https://bun.com/docs/guides/http/hot


The [`--hot`](/docs/runtime/watch-mode#hot-mode) flag runs a file with hot reloading enabled. When any module or file changes, Bun re-runs the file.

```sh
bun --hot run index.ts
```

***

Bun detects when you are running an HTTP server with `Bun.serve()`. It reloads your fetch handler when source files change, *without* restarting the `bun` process. This makes hot reloads nearly instantaneous.

> Note
Hot reloading doesn't reload the page in your browser.

**File:** `index.ts`
```ts
Bun.serve({
  port: 3000,
  fetch(req) {
    return new Response("Hello world");
  },
});
```

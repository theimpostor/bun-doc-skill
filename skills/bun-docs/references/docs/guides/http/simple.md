# Write a simple HTTP server
Source: https://bun.com/docs/guides/http/simple


This code starts an HTTP server listening on port `3000`. It responds to every request with a `200` status and the body `"Welcome to Bun!"`.

See [`Bun.serve`](/docs/runtime/http/server) for details.

**File:** `server.ts`
```ts
const server = Bun.serve({
  port: 3000,
  fetch(request) {
    return new Response("Welcome to Bun!");
  },
});

console.log(`Listening on ${server.url}`);
```

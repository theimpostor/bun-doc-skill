# Error Handling
Source: https://bun.com/docs/runtime/http/error-handling

Learn how to handle errors in Bun's development server

To activate development mode, set `development: true`.

**File:** `server.ts`
```ts
Bun.serve({
  development: true,
  fetch(req) {
    throw new Error("woops!");
  },
});
```

In development mode, Bun will surface errors in-browser with a built-in error page.

<img alt="Bun's built-in 500 page" />

### `error` callback

To handle server-side errors, implement an `error` handler. This function should return a `Response` to serve to the client when an error occurs. This response will supersede Bun's default error page in `development` mode.

```ts
Bun.serve({
  fetch(req) {
    throw new Error("woops!");
  },
  error(error) {
    return new Response(`<pre>${error}\n${error.stack}</pre>`, {
      headers: {
        "Content-Type": "text/html",
      },
    });
  },
});
```

> Info: [Learn more about debugging in Bun](/runtime/debugger)

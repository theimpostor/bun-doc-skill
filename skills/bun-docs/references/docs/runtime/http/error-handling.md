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

In development mode, Bun surfaces errors in-browser with a built-in error page.

<img alt="Bun's built-in 500 page" />

### `error` callback

To handle server-side errors, implement an `error` handler. Return a `Response` to serve to the client when an error occurs. In `development` mode, this response replaces Bun's default error page.

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

> Info: [Learn more about debugging in Bun](/docs/runtime/debugger)

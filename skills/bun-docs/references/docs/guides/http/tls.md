# Configure TLS on an HTTP server
Source: https://bun.com/docs/guides/http/tls


Set the `tls` key to configure TLS. Both `key` and `cert` are required: `key` is the contents of your private key and `cert` is the contents of your issued certificate. Use [`Bun.file()`](/docs/runtime/file-io#reading-files-bun-file) to read them.

**File:** `server.ts`
```ts
const server = Bun.serve({
  fetch: request => new Response("Welcome to Bun!"),
  tls: {
    cert: Bun.file("cert.pem"),
    key: Bun.file("key.pem"),
  },
});
```

***

By default, Bun trusts the Mozilla-curated list of well-known root CAs. To override this list, pass an array of certificates as `ca`. On a server, Bun uses this list to verify *client* certificates, so also set `requestCert: true`.

**File:** `server.ts`
```ts
const server = Bun.serve({
  fetch: request => new Response("Welcome to Bun!"),
  tls: {
    cert: Bun.file("cert.pem"),
    key: Bun.file("key.pem"),
    ca: [Bun.file("ca1.pem"), Bun.file("ca2.pem")],
    requestCert: true,
  },
});
```

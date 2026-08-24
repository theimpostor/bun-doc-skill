# Build an HTTP server using Express and Bun
Source: https://bun.com/docs/guides/ecosystem/express


Express and other major Node.js HTTP libraries should work in Bun without changes. Bun implements the [`node:http`](https://nodejs.org/api/http.html) and [`node:https`](https://nodejs.org/api/https.html) modules that these libraries rely on.

> Note: See [Node.js compatibility](/docs/runtime/nodejs-compat#node-http) for details.

```sh
bun add express
```

***

To define an HTTP route and start a server with Express:

**File:** `server.ts`
```ts
import express from "express";

const app = express();
const port = 8080;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(port, () => {
  console.log(`Listening on port ${port}...`);
});
```

***

To start the server on `localhost`:

```sh
bun server.ts
```

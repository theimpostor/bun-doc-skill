# Streaming HTTP Server with Node.js Streams
Source: https://bun.com/docs/guides/http/stream-node-streams-in-bun


In Bun, a [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) accepts a Node.js [`Readable`](https://nodejs.org/api/stream.html#stream_readable_streams) as its body.

This works because Bun's `Response` accepts any async iterable as its body, and Node.js streams are async iterables.

**File:** `server.ts`
```ts
import { Readable } from "stream";
import { serve } from "bun";
serve({
  port: 3000,
  fetch(req) {
    return new Response(Readable.from(["Hello, ", "world!"]), {
      headers: { "Content-Type": "text/plain" },
    });
  },
});
```

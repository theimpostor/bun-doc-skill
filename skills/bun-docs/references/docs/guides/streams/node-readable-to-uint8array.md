# Convert a Node.js Readable to an Uint8Array
Source: https://bun.com/docs/guides/streams/node-readable-to-uint8array


To convert a Node.js `Readable` stream to a `Uint8Array` in Bun, create a `Response` with the stream as the body, then call `bytes()`.

```ts
import { Readable } from "stream";
const stream = Readable.from(["Hello, ", "world!"]);
const buf = await new Response(stream).bytes();
```

# Convert a Buffer to an ArrayBuffer
Source: https://bun.com/docs/guides/binary/buffer-to-arraybuffer


The Node.js [`Buffer`](https://nodejs.org/api/buffer.html) class views and manipulates data in an underlying `ArrayBuffer`. The `buffer` property returns that `ArrayBuffer`.

```ts
const nodeBuf = Buffer.alloc(64);
const arrBuf = nodeBuf.buffer;
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).

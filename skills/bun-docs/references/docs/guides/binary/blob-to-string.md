# Convert a Blob to a string
Source: https://bun.com/docs/guides/binary/blob-to-string


The [`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob) class provides several methods for consuming its contents in different formats, including `.text()`.

```ts
const blob = new Blob(["hello world"]);
const str = await blob.text();
// => "hello world"
```

***

See [Binary Data](/docs/runtime/binary-data#conversion).

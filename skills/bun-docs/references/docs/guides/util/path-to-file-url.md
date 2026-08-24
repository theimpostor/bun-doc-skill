# Convert an absolute path to a file URL
Source: https://bun.com/docs/guides/util/path-to-file-url


Use `Bun.pathToFileURL()` to convert an absolute path to a `file://` URL.

```ts
Bun.pathToFileURL("/path/to/file.txt").href;
// => "file:///path/to/file.txt"
```

***

See [Utils](/docs/runtime/utils).

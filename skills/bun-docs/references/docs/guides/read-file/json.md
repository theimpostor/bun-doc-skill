# Read a JSON file
Source: https://bun.com/docs/guides/read-file/json


The `Bun.file()` function accepts a path and returns a `BunFile` instance. `BunFile` extends `Blob`, so you can read the file lazily in a variety of formats. Use `.json()` to read and parse the contents of a `.json` file as a plain object.

Bun sets the MIME type of the `BunFile` accordingly.

**File:** `index.ts`
```ts
const path = "/path/to/package.json";
const file = Bun.file(path);

const contents = await file.json();
// { name: "my-package" }

file.type; // => "application/json;charset=utf-8";
```

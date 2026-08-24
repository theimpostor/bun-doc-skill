# Import a HTML file as text
Source: https://bun.com/docs/guides/runtime/import-html


To import a `.html` file in Bun as a text file, use the `type: "text"` attribute in the import statement.

**File:** `file.ts`
```ts
import html from "./file.html" with { type: "text" };

console.log(html); // <!DOCTYPE html><html><head>...
```

With hot module reloading or watch mode, Bun reloads whenever `./file.html` changes.

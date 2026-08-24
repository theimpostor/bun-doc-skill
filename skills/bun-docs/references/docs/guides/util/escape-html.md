# Escape an HTML string
Source: https://bun.com/docs/guides/util/escape-html


`Bun.escapeHTML()` escapes HTML characters in a string. It makes the following replacements.

* `"` becomes `"""`
* `&` becomes `"&"`
* `'` becomes `"'"`
* `<` becomes `"<"`
* `>` becomes `">"`

This function is optimized for large input. It converts non-string values to a string before escaping them.

```ts
Bun.escapeHTML("<script>alert('Hello World!')</script>");
// &lt;script&gt;alert(&#x27;Hello World!&#x27;)&lt;/script&gt;
```

***

See [Utils](/docs/runtime/utils).

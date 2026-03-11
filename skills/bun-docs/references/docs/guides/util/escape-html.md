# Escape an HTML string
Source: https://bun.com/docs/guides/util/escape-html


The `Bun.escapeHTML()` utility can be used to escape HTML characters in a string. The following replacements are made.

* `"` becomes `"""`
* `&` becomes `"&"`
* `'` becomes `"'"`
* `<` becomes `"<"`
* `>` becomes `">"`

This function is optimized for large input. Non-string types will be converted to a string before escaping.

```ts
Bun.escapeHTML("<script>alert('Hello World!')</script>");
// &lt;script&gt;alert(&#x27;Hello World!&#x27;)&lt;&#x2F;script&gt;
```

***

See [Docs > API > Utils](/runtime/utils) for more useful utilities.

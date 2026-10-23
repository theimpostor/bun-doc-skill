# unicorn/prefer-response-static-json
Source: https://bun.com/docs/lint/rules/unicorn/prefer-response-static-json

Require `Response.json()` instead of `new Response(JSON.stringify())`


`new Response(JSON.stringify(data))` sends JSON with the content type `text/plain`, unless you remember to set the header. `Response.json(data)` serializes the data and sets `Content-Type: application/json` for you.

`--fix` doesn't change the code, because the header changes. `--fix-suggestions` rewrites the call.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"unicorn/prefer-response-static-json" = "error" # or "warn"
```


## Examples

Reported:

```js
Bun.serve({
  routes: {
    "/user": () => new Response(JSON.stringify({ name: "Ada" })),
    "/missing": () => new Response(JSON.stringify({ error: "not found" }), { status: 404 }),
  },
});
```

Not reported:

```js
Bun.serve({
  routes: {
    "/user": () => Response.json({ name: "Ada" }),
    "/missing": () => Response.json({ error: "not found" }, { status: 404 }),
  },
});
```

`JSON.stringify()` with a replacer or an indent isn't reported, because `Response.json()` has no way to pass them:

```js
const pretty = new Response(JSON.stringify(report, null, 2));
```

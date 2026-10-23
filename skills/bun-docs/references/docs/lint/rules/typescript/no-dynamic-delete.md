# @typescript-eslint/no-dynamic-delete
Source: https://bun.com/docs/lint/rules/typescript/no-dynamic-delete

Disallow `delete` with a computed property key


`delete sessions[userId]` with a key that's only known at run time means you're using the object as a map. TypeScript can't check that the key exists, and `delete` doesn't tell you whether it removed anything. Use a `Map` or a `Set` instead. Their `.delete()` returns `true` only if the key was there.

A literal key is fine: a string, a number, or a negative number.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"@typescript-eslint/no-dynamic-delete" = "error" # or "warn"
```


## Examples

Reported:

```ts
const sessions: Record<string, Date> = {};

function logout(userId: string) {
  delete sessions[userId];
}
```

Not reported:

```ts
const sessions = new Map<string, Date>();

function logout(userId: string) {
  sessions.delete(userId);
}
```

```ts
const headers: Record<string, string> = {};

delete headers.cookie;
delete headers["set-cookie"];
```

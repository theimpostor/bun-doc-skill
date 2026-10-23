# @typescript-eslint/prefer-ts-expect-error
Source: https://bun.com/docs/lint/rules/typescript/prefer-ts-expect-error

Require `@ts-expect-error` instead of `@ts-ignore`


`@ts-ignore` hides every type error on the next line, forever. When the error is fixed, the comment stays, and the next real error on that line is hidden too. `@ts-expect-error` does the same job, but TypeScript complains once there's no error left to hide, so you know to delete it.

`--fix` replaces `@ts-ignore` with `@ts-expect-error`.

typescript-eslint has deprecated this rule. Use `@typescript-eslint/ban-ts-comment` instead.

## Examples

Reported:

```ts
// @ts-ignore: `retries` is missing from the package's types
client.retries = 3;
```

Not reported:

```ts
// @ts-expect-error: `retries` is missing from the package's types
client.retries = 3;
```

## When not to use it

`@typescript-eslint/ban-ts-comment` covers this and the other `@ts-` comments. If you use it, you don't need this rule.

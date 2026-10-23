# no-process-env
Source: https://bun.com/docs/lint/rules/eslint/no-process-env

Disallow `process.env`


`process.env` is global state. If you read it all over a project, nobody can list which variables the project needs, every reader has to deal with a missing or misspelled value, and tests have to change the whole process's environment.

Read the environment in one file, check the values there, and import that file everywhere else. Turn the rule off for that one file.

The rule only checks `process.env`, not `Bun.env` or `import.meta.env`.

ESLint has deprecated this rule. Use `n/no-process-env` instead.

## Examples

Reported:

```js
function connect() {
  return open(process.env.DATABASE_URL);
}
```

Not reported:

```js
import { config } from "./config.js";

function connect() {
  return open(config.databaseUrl);
}
```

## When not to use it

Reading `process.env` directly is fine in a small script, or in a project that doesn't keep its configuration in one place.

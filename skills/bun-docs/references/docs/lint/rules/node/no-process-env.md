# n/no-process-env
Source: https://bun.com/docs/lint/rules/node/no-process-env

Disallow `process.env`


When you read `process.env` all over the code, it's hard to list the variables the program needs, a misspelled name gives `undefined` without an error, and tests have to change the process's environment. Read the environment in one config file and import the values from there.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"n/no-process-env" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"n/no-process-env" = ["error", {
  allowedVariables = [], # list of strings
}]
```


## Examples

Reported:

```js
if (process.env.NODE_ENV === "development") {
  enableLogging();
}
```

Not reported:

```js
import { config } from "./config";

if (config.env === "development") {
  enableLogging();
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowedVariables` | `[]` | Names of variables you can read from `process.env`. |

```js
const isProduction = process.env.NODE_ENV === "production";
const mode = process.env["NODE_ENV"];
```

Other variables are still reported, and so is `process.env` by itself:

```js
const port = process.env.PORT;
const { NODE_ENV } = process.env;
```

## When not to use it

Turn it off for the one file that reads the environment, and in scripts and small tools where a config file is more than you need.

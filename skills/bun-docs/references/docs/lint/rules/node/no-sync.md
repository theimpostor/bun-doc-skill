# n/no-sync
Source: https://bun.com/docs/lint/rules/node/no-sync

Disallow calls to functions with names that end in `Sync`


A function such as `fs.readFileSync()` blocks the thread until it's done. In a server, every other request waits for that one file to be read. The versions that return a promise or take a callback let other work run in the meantime.

The rule only goes by the name. It reports any call to a function or method with a name that ends in `Sync`. Mentioning the function without calling it isn't reported.


## Configure

Off by default. To turn it on:

**File:** `bunfig.toml`
```toml
[lint.rules]
"n/no-sync" = "error" # or "warn"
```

Every option, set to its default:

**File:** `bunfig.toml`
```toml
[lint.rules]
"n/no-sync" = ["error", {
  allowAtRootLevel = false,
  ignores = [], # list of strings
}]
```


## Examples

Reported:

```js
function handle(request) {
  const page = fs.readFileSync("index.html", "utf8");
  return new Response(page);
}
```

Not reported:

```js
async function handle(request) {
  const page = await fs.promises.readFile("index.html", "utf8");
  return new Response(page);
}
```

## Options

| Option | Default | What it does |
| --- | --- | --- |
| `allowAtRootLevel` | `false` | Allow calls outside of any function, which run once when the file is loaded. |
| `ignores` | `[]` | Names of functions that are never reported. |

```js
const template = fs.readFileSync("index.html", "utf8");
```

```js
function template() {
  return fs.readFileSync("index.html", "utf8");
}
```

```js
function hasConfig() {
  return fs.existsSync("config.json");
}
```

## When not to use it

In scripts, build steps and command line tools, nothing else is waiting for the thread, and the synchronous calls are simpler.

# Bun Runtime
Source: https://bun.com/docs/runtime/index

Execute JavaScript/TypeScript files, package.json scripts, and executable packages with Bun's fast runtime.


The Bun Runtime is designed to start fast and run fast.

Bun uses the [JavaScriptCore engine](https://developer.apple.com/documentation/javascriptcore), developed by Apple for Safari. JavaScriptCore usually starts and runs faster than V8, the engine used by Node.js and Chromium-based browsers. Bun's transpiler and runtime are written in Rust. On Linux, Bun starts [4x faster](https://twitter.com/jarredsumner/status/1499225725492076544) than Node.js.

| Command         | Time     |
| --------------- | -------- |
| `bun hello.js`  | `5.2ms`  |
| `node hello.js` | `25.1ms` |

The benchmark runs a Hello World script on Linux.

## Run a file

Use `bun run` to execute a source file.

```bash
bun run index.js
```

Bun supports TypeScript and JSX with no configuration. Bun transpiles every file on the fly with its native [transpiler](/runtime/transpiler) before running it.

```bash
bun run index.js
bun run index.jsx
bun run index.ts
bun run index.tsx
```

Alternatively, you can omit the `run` keyword and use the "naked" command; it behaves identically.

```bash
bun index.tsx
bun index.js
```

### `--watch`

To run a file in watch mode, use the `--watch` flag.

```bash
bun --watch run index.tsx
```

> Note
When using `bun run`, put Bun flags like `--watch` immediately after `bun`.

```bash
bun --watch run dev # ✔️ do this
bun run dev --watch # ❌ don't do this
```

`bun` ignores flags at the end of the command and passes them through to the `"dev"` script itself.


### `--check`

Bun runs TypeScript files without checking their types. To type check a file and everything it imports before Bun runs it, use the `--check` flag.

```bash
bun --check index.tsx
```

If there is a type error, Bun prints it, exits with code `1`, and does not run the file. See [`bun check`](/runtime/check#check-before-you-run-build-or-test).

## Run a `package.json` script

> Note
Compare to `npm run <script>` or `yarn <script>`

```sh
bun [bun flags] run <script> [script flags]
```

Your `package.json` can define named `"scripts"` that correspond to shell commands.

**File:** `package.json`
```json
{
  // ... other fields
  "scripts": {
    "clean": "rm -rf dist && echo 'Done.'",
    "dev": "bun server.ts"
  }
}
```

Use `bun run <script>` to execute these scripts.

```bash
bun run clean
rm -rf dist && echo 'Done.'
```

```txt
Done.
```

Bun executes the script command in a subshell. On Linux & macOS, it checks for the following shells in order, using the first one it finds: `bash`, `sh`, `zsh`. On Windows, it uses the [Bun Shell](/runtime/shell) to support bash-like syntax and many common commands.

> Note: ⚡️ The startup time for `npm run` on Linux is roughly 170ms; with Bun it is `6ms`.

You can also run scripts with the shorter command `bun <script>`. If a built-in `bun` command has the same name, the built-in command takes precedence; use the explicit `bun run <script>` to run your package script instead.

```bash
bun run dev
```

To see a list of available scripts, run `bun run` without any arguments.

```bash
bun run
```

```txt
...
package.json scripts (2 found):
  $ bun run clean
    rm -rf dist && echo 'Done.'

  $ bun run dev
    bun server.ts
```

Bun respects lifecycle hooks. For instance, `bun run clean` runs `preclean` and `postclean`, if defined. If the `pre<script>` fails, Bun does not run the script itself.

### `--bun`

It's common for `package.json` scripts to reference locally-installed CLIs like `vite` or `next`. These CLIs are often JavaScript files marked with a [shebang](<https://en.wikipedia.org/wiki/Shebang_(Unix)>) to indicate that they should be executed with `node`.

**File:** `cli.js`
```js
#!/usr/bin/env node

// do stuff
```

By default, Bun respects this shebang and executes the script with `node`. The `--bun` flag overrides it: the CLI runs with Bun instead of Node.js.

```bash
bun run --bun vite
```

### Filtering

In a monorepo, the `--filter` argument runs a script in many packages at once.

`bun run --filter <pattern> <script>` executes `<script>` in every package selected by `<pattern>`. The pattern can be a package name glob, a `./path`, a `{dir}` directory or a dependency relation like `foo...`.
For example, if you have subdirectories containing packages named `foo`, `bar` and `baz`, running

```bash
bun run --filter 'ba*' <script>
```

executes `<script>` in both `bar` and `baz`, but not in `foo`.

See [`--filter`](/pm/filter#running-scripts-with-filter).

## `bun run -` to pipe code from stdin

`bun run -` reads JavaScript, TypeScript, TSX, or JSX from stdin and executes it without writing to a temporary file first.

```bash
echo "console.log('Hello')" | bun run -
```

```txt
Hello
```

You can also use `bun run -` to redirect files into Bun. For example, to run a `.js` file as if it were a `.ts` file:

```bash
echo "console.log!('This is TypeScript!' as any)" > secretly-typescript.js
bun run - < secretly-typescript.js
```

```txt
This is TypeScript!
```

`bun run -` treats all input as TypeScript with JSX support.

## `bun run --console-depth`

Control the depth of object inspection in console output with the `--console-depth` flag.

```bash
bun --console-depth 5 run index.tsx
```

`--console-depth` sets how deeply Bun displays nested objects in `console.log()` output. The default depth is `2`. Higher values show more nested properties but may produce verbose output for complex objects.

**File:** `console.ts`
```ts
const nested = { a: { b: { c: { d: "deep" } } } };
console.log(nested);
// With --console-depth 2 (default): { a: { b: { c: [Object] } } }
// With --console-depth 4: { a: { b: { c: { d: 'deep' } } } }
```

## `bun run --smol`

In memory-constrained environments, use the `--smol` flag to reduce memory usage at a cost to performance.

```bash
bun --smol run index.tsx
```

`--smol` makes the garbage collector run more frequently, which can slow down execution. Bun adjusts the garbage collector's heap size based on the available memory (accounting for cgroups and other memory limits) with and without the `--smol` flag. The flag is therefore mostly useful when you want the heap to grow more slowly.

## Resolution order

Bun always executes absolute paths and paths starting with `./` or `.\` as source files. Unless you use `bun run`, a name with an allowed extension resolves to the file rather than a `package.json` script.

When a `package.json` script and a file have the same name, `bun run` prefers the script. The full resolution order is:

1. `package.json` scripts: `bun run build`
2. Source files: `bun run src/main.js`
3. Binaries from project packages: `bun add eslint && bun run eslint`
4. (`bun run` only) System commands: `bun run ls`

---

# CLI Usage

```bash
bun run <file or script>
```

### General Execution Options

### `--silent`

Type: `boolean`
Don't print the script command

### `--if-present`

Type: `boolean`
Exit without an error if the entrypoint does not exist

### `--eval`

Type: `string`
Evaluate argument as a script. Alias: `-e`

### `--print`

Type: `string`
Evaluate argument as a script and print the result. Alias: `-p`

### `--help`

Type: `boolean`
Display this menu and exit. Alias: `-h`

### Workspace Management

### `--elide-lines`

Type: `number`; Default: `0`
Truncate each script's output to its last N lines when using --filter. Default 0 shows all lines

### `--filter`

Type: `string`
Run a script in all workspace packages matching the pattern. Alias: `-F`

### `--workspaces`

Type: `boolean`
Run a script in all workspace packages (from the `workspaces` field in `package.json`)

### `--parallel`

Type: `boolean`
Run multiple scripts or workspace scripts concurrently with prefixed output

### `--sequential`

Type: `boolean`
Run multiple scripts or workspace scripts one after another with prefixed output

### `--no-exit-on-error`

Type: `boolean`
When using `--parallel` or `--sequential`, continue running other scripts when one fails

### Runtime & Process Control

### `--bun`

Type: `boolean`
Force a script or package to use Bun's runtime instead of Node.js (via symlinking node). Alias: `-b`

### `--shell`

Type: `string`
Control the shell used for `package.json` scripts. Supports either `bun` or `system`

### `--interactive`

Type: `boolean`
Open the Node.js-compatible REPL (`node:repl`). When combined with `-e`, starts the REPL and
then evaluates the script. Under `--interactive`, `-e` is raw JavaScript (matching{" "}
`node -i -e`). Use `bun repl` for TypeScript. Distinct from `bun repl`, which is
Bun's native REPL.

### `--smol`

Type: `boolean`
Use less memory, but run garbage collection more often

### `--expose-gc`

Type: `boolean`
Expose `gc()` on the global object. Has no effect on `Bun.gc()`

### `--no-deprecation`

Type: `boolean`
Silence all deprecation warnings

### `--throw-deprecation`

Type: `boolean`
Throw deprecation warnings as errors

### `--title`

Type: `string`
Set the process title

### `--zero-fill-buffers`

Type: `boolean`
Force `Buffer.allocUnsafe(size)` to be zero-filled

### `--no-addons`

Type: `boolean`
Throw an error if `process.dlopen` or `bun:ffi` `cc()` is called, and disable export
condition `node-addons`

### `--no-ffi-cc`

Type: `boolean`
Throw an error if `bun:ffi` `cc()` is called (disables the C compiler)

### `--unhandled-rejections`

Type: `string`
One of `strict`, `throw`, `warn`, `none`, or{" "}
`warn-with-error-code`

### `--console-depth`

Type: `number`; Default: `2`
Set the default depth for `console.log` object inspection (default: 2)

### Development Workflow

### `--check`

Type: `boolean`
Type check before running. Nothing runs if there are type errors. See <a href="/runtime/check">bun check</a>

### `--watch`

Type: `boolean`
Automatically restart the process on file change

### `--watch-kill-signal`

Type: `string`; Default: `SIGTERM`
Signal whose handlers run when --watch restarts the process

### `--hot`

Type: `boolean`
Enable auto reload in the Bun runtime, test runner, or bundler

### `--no-clear-screen`

Type: `boolean`
Disable clearing the terminal screen on reload when --hot or --watch is enabled

### Debugging

### `--inspect`

Type: `string`
Activate Bun's debugger

### `--inspect-wait`

Type: `string`
Activate Bun's debugger, wait for a connection before executing

### `--inspect-brk`

Type: `string`
Activate Bun's debugger, set breakpoint on first line of code and wait

### Dependency & Module Resolution

### `--preload`

Type: `string`
Import a module before Bun loads other modules. Alias: `-r`

### `--require`

Type: `string`
Alias of --preload, for Node.js compatibility

### `--import`

Type: `string`
Alias of --preload, for Node.js compatibility

### `--no-install`

Type: `boolean`
Disable auto install in the Bun runtime

### `--install`

Type: `string`; Default: `auto`
Configure auto-install behavior. One of `auto` (default, auto-installs when no node_modules),{" "}
`fallback` (missing packages only), `force` (always)

### `-i`

Type: `boolean`
Auto-install dependencies during execution. Equivalent to --install=fallback

### `--prefer-offline`

Type: `boolean`
Skip staleness checks for packages in the Bun runtime and resolve from disk

### `--prefer-latest`

Type: `boolean`
Use the latest matching versions of packages in the Bun runtime, always checking npm

### `--conditions`

Type: `string`
Pass custom conditions to resolve

### `--main-fields`

Type: `string`
Main fields to lookup in `package.json`

### `--preserve-symlinks`

Type: `boolean`
Preserve symlinks when resolving files

### `--preserve-symlinks-main`

Type: `boolean`
Preserve symlinks when resolving the main entry point

### `--extension-order`

Type: `string`; Default: `.tsx,.ts,.jsx,.cts,.cjs,.js,.mjs,.mts,.json,.node`
Defaults to: `.tsx,.ts,.jsx,.cts,.cjs,.js,.mjs,.mts,.json,.node`

### Transpilation & Language Features

### `--tsconfig-override`

Type: `string`
Specify custom `tsconfig.json`. Default `$cwd/tsconfig.json`

### `--define`

Type: `string`
Substitute K:V while parsing, e.g. `--define process.env.NODE_ENV:"development"`. Bun parses values as
JSON. Alias: `-d`

### `--drop`

Type: `string`
Remove function calls, e.g. `--drop=console` removes all `console.*` calls

### `--loader`

Type: `string`
Parse files with `.ext:loader`, e.g. `--loader .js:jsx`. Valid loaders: `js`,{" "}
`jsx`, `ts`, `tsx`, `json`, `toml`, `text`,{" "}
`file`, `wasm`, `napi`. Alias: `-l`

### `--no-macros`

Type: `boolean`
Disable macro execution in the bundler, transpiler and runtime

### `--jsx-factory`

Type: `string`
Changes the function called when compiling JSX elements using the classic JSX runtime

### `--jsx-fragment`

Type: `string`
Changes the function called when compiling JSX fragments

### `--jsx-import-source`

Type: `string`; Default: `react`
Declares the module specifier used to import the jsx and jsxs factory functions. Default: `react`

### `--jsx-runtime`

Type: `string`; Default: `automatic`
`automatic` (default) or `classic`

### `--jsx-side-effects`

Type: `boolean`
Treat JSX elements as having side effects (disable pure annotations)

### `--ignore-dce-annotations`

Type: `boolean`
Ignore tree-shaking annotations such as `@__PURE__`

### Networking & Security

### `--port`

Type: `number`
Set the default port for `Bun.serve`

### `--fetch-preconnect`

Type: `string`
Preconnect to a URL while code is loading

### `--max-http-header-size`

Type: `number`; Default: `16384`
Set the maximum size of HTTP headers in bytes. Default is 16KiB

### `--dns-result-order`

Type: `string`; Default: `verbatim`
Set the default order of DNS lookup results. Valid orders: `verbatim` (default), `ipv4first`,{" "}
`ipv6first`

### `--use-system-ca`

Type: `boolean`
Use the system's trusted certificate authorities

### `--use-openssl-ca`

Type: `boolean`
Use OpenSSL's default CA store

### `--use-bundled-ca`

Type: `boolean`
Use bundled CA store

### `--redis-preconnect`

Type: `boolean`
Preconnect to `$REDIS_URL` at startup

### `--sql-preconnect`

Type: `boolean`
Preconnect to PostgreSQL at startup

### `--user-agent`

Type: `string`
Set the default User-Agent header for HTTP requests

### Global Configuration & Context

### `--env-file`

Type: `string`
Load environment variables from the specified file(s)

### `--cwd`

Type: `string`
Absolute path to resolve files & entrypoints from. This only changes the process' cwd

### `--config`

Type: `string`
Specify path to Bun config file. Default `$cwd/bunfig.toml`. Alias: `-c`

## Examples

Run a JavaScript or TypeScript file:

```bash
bun run ./index.js
bun run ./index.tsx
```

Run a package.json script:

```bash
bun run dev
bun run lint
```

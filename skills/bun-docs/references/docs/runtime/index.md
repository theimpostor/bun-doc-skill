# Bun Runtime
Source: https://bun.com/docs/runtime/index

Execute JavaScript/TypeScript files, package.json scripts, and executable packages with Bun's fast runtime.

The Bun Runtime is designed to start fast and run fast.

Under the hood, Bun uses the [JavaScriptCore engine](https://developer.apple.com/documentation/javascriptcore), which is developed by Apple for Safari. In most cases, the startup and running performance is faster than V8, the engine used by Node.js and Chromium-based browsers. Its transpiler and runtime are written in Zig, a modern, high-performance language. On Linux, this translates into startup times [4x faster](https://twitter.com/jarredsumner/status/1499225725492076544) than Node.js.

| Command         | Time     |
| --------------- | -------- |
| `bun hello.js`  | `5.2ms`  |
| `node hello.js` | `25.1ms` |

This benchmark is based on running a Hello World script on Linux

## Run a file

Use `bun run` to execute a source file.

```bash
bun run index.js
```

Bun supports TypeScript and JSX out of the box. Every file is transpiled on the fly by Bun's fast native transpiler before being executed.

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

Flags that occur at the end of the command will be ignored and passed through to the `"dev"` script itself.

## Run a `package.json` script

> Note
Compare to `npm run <script>` or `yarn <script>`

```sh
bun [bun flags] run <script> [script flags]
```

Your `package.json` can define a number of named `"scripts"` that correspond to shell commands.

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
Cleaning...
Done.
```

Bun executes the script command in a subshell. On Linux & macOS, it checks for the following shells in order, using the first one it finds: `bash`, `sh`, `zsh`. On Windows, it uses [bun shell](/runtime/shell) to support bash-like syntax and many common commands.

> Note: ⚡️ The startup time for `npm run` on Linux is roughly 170ms; with Bun it is `6ms`.

Scripts can also be run with the shorter command `bun <script>`, however if there is a built-in bun command with the same name, the built-in command takes precedence. In this case, use the more explicit `bun run <script>` command to execute your package script.

```bash
bun run dev
```

To see a list of available scripts, run `bun run` without any arguments.

```bash
bun run
```

```txt
quickstart scripts:

 bun run clean
   rm -rf dist && echo 'Done.'

 bun run dev
   bun server.ts

2 scripts
```

Bun respects lifecycle hooks. For instance, `bun run clean` will execute `preclean` and `postclean`, if defined. If the `pre<script>` fails, Bun will not execute the script itself.

### `--bun`

It's common for `package.json` scripts to reference locally-installed CLIs like `vite` or `next`. These CLIs are often JavaScript files marked with a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) to indicate that they should be executed with `node`.

**File:** `cli.js`
```js
#!/usr/bin/env node

// do stuff
```

By default, Bun respects this shebang and executes the script with `node`. However, you can override this behavior with the `--bun` flag. For Node.js-based CLIs, this will run the CLI with Bun instead of Node.js.

```bash
bun run --bun vite
```

### Filtering

In monorepos containing multiple packages, you can use the `--filter` argument to execute scripts in many packages at once.

Use `bun run --filter <name_pattern> <script>` to execute `<script>` in all packages whose name matches `<name_pattern>`.
For example, if you have subdirectories containing packages named `foo`, `bar` and `baz`, running

```bash
bun run --filter 'ba*' <script>
```

will execute `<script>` in both `bar` and `baz`, but not in `foo`.

Find more details in the docs page for [filter](/pm/filter#running-scripts-with-filter).

## `bun run -` to pipe code from stdin

`bun run -` lets you read JavaScript, TypeScript, TSX, or JSX from stdin and execute it without writing to a temporary file first.

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

For convenience, all code is treated as TypeScript with JSX support when using `bun run -`.

## `bun run --console-depth`

Control the depth of object inspection in console output with the `--console-depth` flag.

```bash
bun --console-depth 5 run index.tsx
```

This sets how deeply nested objects are displayed in `console.log()` output. The default depth is `2`. Higher values show more nested properties but may produce verbose output for complex objects.

**File:** `console.ts`
```ts
const nested = { a: { b: { c: { d: "deep" } } } };
console.log(nested);
// With --console-depth 2 (default): { a: { b: [Object] } }
// With --console-depth 4: { a: { b: { c: { d: 'deep' } } } }
```

## `bun run --smol`

In memory-constrained environments, use the `--smol` flag to reduce memory usage at a cost to performance.

```bash
bun --smol run index.tsx
```

This causes the garbage collector to run more frequently, which can slow down execution. However, it can be useful in environments with limited memory. Bun automatically adjusts the garbage collector's heap size based on the available memory (accounting for cgroups and other memory limits) with and without the `--smol` flag, so this is mostly useful for cases where you want to make the heap size grow more slowly.

## Resolution order

Absolute paths and paths starting with `./` or `.\` are always executed as source files. Unless using `bun run`, running a file with an allowed extension will prefer the file over a package.json script.

When there is a package.json script and a file with the same name, `bun run` prioritizes the package.json script. The full resolution order is:

1. package.json scripts, eg `bun run build`
2. Source files, eg `bun run src/main.js`
3. Binaries from project packages, eg `bun add eslint && bun run eslint`
4. (`bun run` only) System commands, eg `bun run ls`

***

# CLI Usage

```bash
bun run <file or script>
```

### General Execution Options

- (boolean) Don't print the script command

- (boolean) Exit without an error if the entrypoint does not exist

- (string) Evaluate argument as a script. Alias: `-e`

- (string) Evaluate argument as a script and print the result. Alias: `-p`

- (boolean) Display this menu and exit. Alias: `-h`

### Workspace Management

- (number) Number of lines of script output shown when using --filter (default: 10). Set to 0 to show all lines

- (string) Run a script in all workspace packages matching the pattern. Alias: `-F`

- (boolean) Run a script in all workspace packages (from the `workspaces` field in `package.json`)

- (boolean) Run multiple scripts or workspace scripts concurrently with prefixed output

- (boolean) Run multiple scripts or workspace scripts one after another with prefixed output

- (boolean) When using `--parallel` or `--sequential`, continue running other scripts when one fails

### Runtime & Process Control

- (boolean) Force a script or package to use Bun's runtime instead of Node.js (via symlinking node). Alias: `-b`

- (string) Control the shell used for `package.json` scripts. Supports either `bun` or `system`

- (boolean) Use less memory, but run garbage collection more often

- (boolean) Expose `gc()` on the global object. Has no effect on `Bun.gc()`

- (boolean) Suppress all reporting of the custom deprecation

- (boolean) Determine whether or not deprecation warnings result in errors

- (string) Set the process title

- (boolean) Boolean to force `Buffer.allocUnsafe(size)` to be zero-filled

- (boolean) Throw an error if `process.dlopen` is called, and disable export condition `node-addons`

- (string) One of `strict`, `throw`, `warn`, `none`, or `warn-with-error-code`

- (number) Set the default depth for `console.log` object inspection (default: 2)

### Development Workflow

- (boolean) Automatically restart the process on file change

- (boolean) Enable auto reload in the Bun runtime, test runner, or bundler

- (boolean) Disable clearing the terminal screen on reload when --hot or --watch is enabled

### Debugging

- (string) Activate Bun's debugger

- (string) Activate Bun's debugger, wait for a connection before executing

- (string) Activate Bun's debugger, set breakpoint on first line of code and wait

### Dependency & Module Resolution

- (string) Import a module before other modules are loaded. Alias: `-r`

- (string) Alias of --preload, for Node.js compatibility

- (string) Alias of --preload, for Node.js compatibility

- (boolean) Disable auto install in the Bun runtime

- (string) Configure auto-install behavior. One of `auto` (default, auto-installs when no node_modules), `fallback` (missing packages only), `force` (always)

- (boolean) Auto-install dependencies during execution. Equivalent to --install=fallback

- (boolean) Skip staleness checks for packages in the Bun runtime and resolve from disk

- (boolean) Use the latest matching versions of packages in the Bun runtime, always checking npm

- (string) Pass custom conditions to resolve

- (string) Main fields to lookup in `package.json`. Defaults to --target dependent

- (boolean) Preserve symlinks when resolving files

- (boolean) Preserve symlinks when resolving the main entry point

- (string) Defaults to: `.tsx,.ts,.jsx,.js,.json`

### Transpilation & Language Features

- (string) Specify custom `tsconfig.json`. Default `$cwd/tsconfig.json`

- (string) Substitute K:V while parsing, e.g. `--define process.env.NODE_ENV:"development"`. Values are parsed as JSON. Alias: `-d`

- (string) Remove function calls, e.g. `--drop=console` removes all `console.*` calls

- (string) Parse files with `.ext:loader`, e.g. `--loader .js:jsx`. Valid loaders: `js`, `jsx`, `ts`, `tsx`, `json`, `toml`, `text`, `file`, `wasm`, `napi`. Alias: `-l`

- (boolean) Disable macros from being executed in the bundler, transpiler and runtime

- (string) Changes the function called when compiling JSX elements using the classic JSX runtime

- (string) Changes the function called when compiling JSX fragments

- (string) Declares the module specifier to be used for importing the jsx and jsxs factory functions. Default: `react`

- (string) `automatic` (default) or `classic`

- (boolean) Treat JSX elements as having side effects (disable pure annotations)

- (boolean) Ignore tree-shaking annotations such as `@**PURE**`

### Networking & Security

- (number) Set the default port for `Bun.serve`

- (string) Preconnect to a URL while code is loading

- (number) Set the maximum size of HTTP headers in bytes. Default is 16KiB

- (string) Set the default order of DNS lookup results. Valid orders: `verbatim` (default), `ipv4first`, `ipv6first`

- (boolean) Use the system's trusted certificate authorities

- (boolean) Use OpenSSL's default CA store

- (boolean) Use bundled CA store

- (boolean) Preconnect to `$REDIS_URL` at startup

- (boolean) Preconnect to PostgreSQL at startup

- (string) Set the default User-Agent header for HTTP requests

### Global Configuration & Context

- (string) Load environment variables from the specified file(s)

- (string) Absolute path to resolve files & entry points from. This just changes the process' cwd

- (string) Specify path to Bun config file. Default `$cwd/bunfig.toml`. Alias: `-c`

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

# Formatter
Source: https://bun.com/docs/format/index

Bun's fast, built-in formatter for JavaScript, TypeScript, CSS, HTML, JSON, YAML, Markdown, and more


Bun ships with a fast, built-in code formatter. There's nothing to install and nothing to configure.

- JavaScript, TypeScript, JSX, CSS, SCSS, Less, HTML, Vue, Svelte, Angular, JSON, YAML, TOML, Markdown, MDX, GraphQL, and Handlebars
- The same output as [Prettier](https://prettier.io)
- Sorts imports, Tailwind CSS classes, and `package.json`
- Works with your existing Prettier or oxfmt config

## Run the formatter

```bash
bun fmt
```

```txt
src/index.ts
src/server.ts
Formatted 2 files, 2 unchanged [3.47ms]
```

`bun fmt` rewrites the files in the current directory that need it and prints their names. It skips `node_modules`, anything in your `.gitignore` or `.git/info/exclude`, minified files (`*.min.js`, `*.min.css`) and lock files such as `package-lock.json`.

To format specific files, pass paths or globs.

```bash
bun fmt src "test/**/*.ts"
```

Embedded code is formatted too: `<script>` and `<style>` in HTML, Vue, and Svelte, code blocks in Markdown, and `` css`...` ``, `` html`...` ``, and `` graphql`...` `` templates in JavaScript.

A syntax error inside a `<script>` or `<style>` of a Svelte component is a warning. That block stays as written, and the rest of the file is formatted.

## Check without writing

`--check` lists the files that need formatting and writes nothing.

```bash
bun fmt --check
```

```txt
src/index.ts
src/server.ts
2 files need formatting. Run bun fmt to fix them.
```

The exit code is `1` if a file needs formatting, `0` if none do, and `2` if something went wrong, like a syntax error. That makes it the command for CI.

**File:** `.github/workflows/format.yml`
```yaml
steps:
  - uses: actions/checkout@v4
  - uses: oven-sh/setup-bun@v2
  - run: bun fmt --check
```

## Options

Options live in `bunfig.toml`. To create the section, run `bun fmt --init`.

**File:** `bunfig.toml`
```toml
[fmt]
printWidth = 100
semi = false
singleQuote = true
```

| Option          | Default | What it does                  |
| --------------- | ------- | ----------------------------- |
| `printWidth`    | `80`    | Wrap lines at this column     |
| `tabWidth`      | `2`     | Spaces per indentation level  |
| `useTabs`       | `false` | Indent with tabs              |
| `semi`          | `true`  | Print semicolons              |
| `singleQuote`   | `false` | Use single quotes             |
| `trailingComma` | `"all"` | `"all"`, `"es5"`, or `"none"` |

All of [Prettier's options](https://prettier.io/docs/options) work, under the same names. Each one is also a flag, like `--print-width 100` or `--no-semi`.

### Different options for some files

**File:** `bunfig.toml`
```toml
[[fmt.overrides]]
files = ["*.test.ts", "scripts/**"]
options = { printWidth = 120 }
```

### `.editorconfig`

`bun fmt` reads `indent_style`, `indent_size`, `tab_width`, `max_line_length`, and `end_of_line` from `.editorconfig`. `bunfig.toml` overrides them.

## Ignore files

Every `.gitignore` in the repository counts, whichever directory you run `bun fmt` from. Outside a repository, those in the current directory and below it count. With a Prettier config, only the `.gitignore` in the current directory does, because that's the only one Prettier reads.

To skip more than `.gitignore` does, list the files in `bunfig.toml`. A `.prettierignore` file works too.

**File:** `bunfig.toml`
```toml
[fmt]
ignorePatterns = ["vendor/", "**/*.gen.ts"]
```

## Ignore code

`bun fmt` uses Prettier's comment, so existing ones keep working. It applies to the next statement, element, or rule.

```ts
// prettier-ignore
const matrix = [
  1, 0, 0,
  0, 1, 0,
  0, 0, 1,
];
```

In JSX it's `{/* prettier-ignore */}`, in CSS `/* prettier-ignore */`, in HTML and Markdown `<!-- prettier-ignore -->`, and in YAML and GraphQL `# prettier-ignore`.

## Sort imports

**File:** `bunfig.toml`
```toml
[fmt]
sortImports = true
```

**File:** `Before`
```ts
import { z } from "zod";
import { b, a } from "./util";
import { db } from "@/db";
import { readFile } from "node:fs/promises";
import { c } from "./util";
```

**File:** `After`
```ts
import { readFile } from "node:fs/promises";

import { z } from "zod";

import { db } from "@/db";

import { a, b, c } from "./util";
```

- Imports are grouped: built-in modules, packages, aliases like `@/`, relative paths, styles.
- Each group is sorted by path, and the names in `{ }` are sorted too.
- Two imports from the same module become one.
- Side-effect imports like `import "./setup"` never move, and nothing moves past one.
- A comment directly above an import moves with it. Above the first import, comments about the whole file stay at the top: `// @ts-nocheck`, `/// <reference ... />`, `/* eslint-disable */`, `// @flow`, `/** @jsxImportSource ... */`, a license.

To pick your own groups, use a table. See [`format.sortImports`](/runtime/bunfig#format-sortimports).

**File:** `bunfig.toml`
```toml
[fmt.sortImports]
groups = ["react", "builtin", "external", "internal", ["parent", "sibling", "index"]]
customGroups = [{ groupName = "react", elementNamePattern = ["react", "react-dom/**"] }]
```

## Sort Tailwind CSS classes

**File:** `bunfig.toml`
```toml
[fmt]
sortTailwindcss = true
```

```tsx
<a className="p-4 flex m-2" />
<a className="m-2 flex p-4" />
```

Classes are sorted in Tailwind's recommended order, in `class` and `className` and in calls to `clsx`, `cn`, `cva`, `twMerge`, and [a few more](/runtime/bunfig#format-sorttailwindcss). They are sorted with your project's `tailwindcss`, version 3 or 4, and are left as they are if it isn't installed.

If your `.prettierrc` lists `prettier-plugin-tailwindcss`, sorting is already on, with that plugin's options and defaults.

To name your own functions or your stylesheet, use a table.

**File:** `bunfig.toml`
```toml
[fmt.sortTailwindcss]
stylesheet = "./src/app.css"
functions = ["clsx", "tw"]
```

## Sort `package.json`

**File:** `bunfig.toml`
```toml
[fmt]
sortPackageJson = true
```

Keys go in the conventional order: `name`, `version`, `description`, and so on.

If your `.prettierrc` lists `prettier-plugin-packagejson`, sorting is already on and uses that plugin's order.

**File:** `Before`
```json
{
  "dependencies": { "zod": "^4.0.0" },
  "scripts": { "dev": "bun --hot src/index.ts" },
  "version": "1.0.0",
  "name": "app"
}
```

**File:** `After`
```json
{
  "name": "app",
  "version": "1.0.0",
  "scripts": {
    "dev": "bun --hot src/index.ts"
  },
  "dependencies": {
    "zod": "^4.0.0"
  }
}
```

## Format JSDoc comments

**File:** `bunfig.toml`
```toml
[fmt]
jsdoc = true
```

**File:** `Before`
```js
/**
 * adds two numbers
 * @returns {number} the sum
 * @param {number} b second number
 * @param {number} a   first number
 */
```

**File:** `After`
```js
/**
 * Adds two numbers
 *
 * @param {number} a First number
 * @param {number} b Second number
 * @returns {number} The sum
 */
```

## Svelte

`.svelte` files are formatted by default, like `prettier-plugin-svelte` formats them. To change how, use a table. These are the defaults:

**File:** `bunfig.toml`
```toml
[fmt.svelte]
sortOrder = "options-scripts-markup-styles"
allowShorthand = true
indentScriptAndStyle = true
```

To leave `.svelte` files alone, turn it off.

**File:** `bunfig.toml`
```toml
[fmt]
svelte = false
```

See [`format.svelte`](/runtime/bunfig#format-svelte).

## Standard input

Pipe text through `bun fmt`. It prints the result and writes nothing. The path picks the language and the options. The file doesn't have to exist.

```bash
bun fmt --stdin-filepath src/index.ts < src/index.ts
```

No path to give? Name the parser instead. Your config still applies, except for what goes by a file name: `overrides`, `.editorconfig`, and ignore files.

```bash
bun run generate-types | bun fmt --parser typescript > types.ts
```

## Git hooks

`--staged` formats only the files you're about to commit and stages them again, so you don't need `lint-staged`.

**File:** `.git/hooks/pre-commit`
```sh
#!/bin/sh
bun fmt --staged
```

If a file has both staged and unstaged changes, Bun looks at the staged version, which is what the commit gets. It doesn't write such a file, because staging it again would commit the rest. If the staged version needs formatting, Bun names the file and exits with code `2`.

Config files, such as `bunfig.toml` and `.prettierrc`, are read from disk.

`--changed` formats the files that differ from your default branch. Pass a ref to compare with something else.

```bash
bun fmt --changed
bun fmt --changed=origin/dev
```

## Migrate from Prettier or oxfmt

Already have a `.prettierrc` or an `.oxfmtrc.json`? `bun fmt` reads it and prints what that tool prints. Change the script and you're done.

**File:** `package.json`
```json
{
  "scripts": {
    "format": "prettier --write .",
    "format": "bun fmt"
  }
}
```

If `package.json` has a `fmt` script, `bun fmt` runs that script. Inside the script, `bun fmt` is the formatter. If `package.json` has `"fmt"` in it but can't be parsed, as in the middle of a merge, `bun fmt` can't tell whether that is a script: it formats nothing and exits with code 2.

Writing a tool that calls Bun in projects you don't control? Pass `--no-script`: `bun fmt --no-script` is always the formatter.

Astro isn't built in. If your `.prettierrc` lists its plugin, Bun sends those files to your installed Prettier. To see which files those are, and which packages you can uninstall:

```bash
bun fmt --doctor
```

See the guides: [Migrate from Prettier](/guides/format/migrate-from-prettier) and [Migrate from oxfmt](/guides/format/migrate-from-oxfmt).

# CLI Usage

```bash
bun fmt [flags] [files, directories, or globs]
```

### Modes

### `-c, --check`

Type: `boolean`
Write nothing. Exit with code 1 if a file needs formatting

### `-l, --list-different`

Type: `boolean`
Like `--check`, but print only the file names

### `--stdin-filepath`

Type: `string`
Format standard input as this file and print the result

### `--init`

Type: `boolean`
Add a `[fmt]` section to `bunfig.toml`

### `--doctor`

Type: `boolean`
Show what Bun does with your Prettier or oxfmt config, and which packages you can remove

### `--no-script`

Type: `boolean`
Run the formatter even if the project has a `fmt` script

### Files

### `--staged`

Type: `boolean`
Format only the files staged in Git, and stage them again

### `--changed`

Type: `string`
Format only the files that differ from a Git ref. Defaults to the default branch

### `--ignore-pattern`

Type: `string`
Skip files that match this glob. Can be repeated

### Options

### `--print-width`

Type: `number`; Default: `80`
Wrap lines at this column

### `--tab-width`

Type: `number`; Default: `2`
Spaces per indentation level

### `--use-tabs`

Type: `boolean`
Indent with tabs

### `--no-semi`

Type: `boolean`
Only print semicolons where they are needed

### `--single-quote`

Type: `boolean`
Use single quotes

### `--trailing-comma`

Type: `string`; Default: `all`
`all`, `es5`, or `none`

### `--sort-imports`

Type: `boolean`
Sort and group imports

### `--sort-tailwindcss`

Type: `boolean`
Sort Tailwind CSS classes

### `--sort-package-json`

Type: `boolean`
Sort the keys of `package.json`

### `--jsdoc`

Type: `boolean`
Format JSDoc comments

### `--svelte`

Type: `boolean`
Format Svelte components. This is the default without a Prettier or oxfmt config

### `--no-svelte`

Type: `boolean`
Do not format Svelte components

### `--no-editorconfig`

Type: `boolean`
Do not read `.editorconfig`

All of [Prettier's options](https://prettier.io/docs/options) are flags too.

### Output

### `--log-level`

Type: `string`; Default: `log`
`silent`, `error`, `warn`, `log`, or `debug`

### `--threads`

Type: `number`
Number of threads. Defaults to one per CPU core

`bun fmt` also accepts the flags of Prettier and oxfmt. Run `bun fmt --help --all` to see them.

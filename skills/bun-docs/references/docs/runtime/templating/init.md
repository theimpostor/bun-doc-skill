# bun init
Source: https://bun.com/docs/runtime/templating/init

Scaffold an empty Bun project with the interactive `bun init` command

Scaffold a new Bun project with `bun init`.

```bash
bun init my-app
```

```txt
? Select a project template - Press return to submit.
❯ Blank
  React
  Library

✓ Select a project template: Blank

 + .gitignore
 + CLAUDE.md
 + .cursor/rules/use-bun-instead-of-node-vite-npm-pnpm.mdc -> CLAUDE.md
 + index.ts
 + tsconfig.json (for editor autocomplete)
 + README.md
```

Press `enter` to accept the default answer for each prompt, or pass the `-y` flag to auto-accept the defaults.

***

`bun init` infers settings with sane defaults and is non-destructive when run multiple times.

![Demo](https://user-images.githubusercontent.com/709451/183006613-271960a3-ff22-4f7c-83f5-5e18f684c836.gif)

It creates:

* a `package.json` file with a name that defaults to the current directory name
* a `tsconfig.json` or `jsconfig.json` file, depending on whether the entry point is a TypeScript file
* an entry point, which defaults to `index.ts` unless any of `index.{tsx, jsx, js, mts, mjs}` exist or the `package.json` specifies a `module` or `main` field
* a `README.md` file

AI Agent rules (disable with `$BUN_AGENT_RULE_DISABLED=1`):

* a `CLAUDE.md` file when `bun init` detects Claude CLI (disable with `CLAUDE_CODE_AGENT_RULE_DISABLED` env var)
* a `.cursor/rules/*.mdc` file when `bun init` detects Cursor (disable with `CURSOR_AGENT_RULE_DISABLED` env var); the file tells [Cursor AI](https://cursor.sh) to use Bun instead of Node.js and npm

Pass `-y` or `--yes` to accept the defaults without prompting.

At the end, it runs `bun install` to install `@types/bun`.

***

## CLI Usage

```bash
bun init <folder?>
```

### Initialization Options

- (boolean) Accept all default prompts without asking questions. Alias: `-y`

- (boolean) Only initialize type definitions (skip app scaffolding). Alias: `-m`

### Project Templates

- (string|boolean) Scaffold a React project. When used without a value, creates a baseline React app. <br> Accepts values for presets: <ul> <li> `tailwind` – React app preconfigured with Tailwind CSS </li> <li> `shadcn` – React app with `@shadcn/ui` and Tailwind CSS </li> </ul> Examples: <pre> ` bun init --reactbun init --react=tailwindbun init --react=shadcn ` </pre>

### Output & Files

- (info) Initializes project files and configuration for the chosen options. Exact files vary by template.

### Help

- (boolean) Print this help menu. Alias: `-h`

### Examples

* Accept all defaults

```bash
bun init -y
```

* React

```bash
bun init --react
```

* React + Tailwind CSS

```bash
bun init --react=tailwind
```

* React + @shadcn/ui
```bash
bun init --react=shadcn
```

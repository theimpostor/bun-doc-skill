# Build a frontend using Vite and Bun
Source: https://bun.com/docs/guides/ecosystem/vite


> Note
You can use Vite with Bun, but many projects get faster builds & drop hundreds of dependencies by switching to [HTML
imports](/docs/bundler/fullstack).

***

Vite works with Bun with no extra configuration. Get started with one of Vite's templates.

```bash
bun create vite my-app
```

```txt
◇  Select a framework:
│  React
│
◇  Select a variant:
│  TypeScript
│
◇  Which linter to use?
│  Oxlint
│
◇  Install with bun and start now?
│  No
│
◇  Scaffolding project in /path/to/my-app...
```

***

Then `cd` into the project directory and install dependencies.

```bash
cd my-app
bun install
```

***

Start the development server with the `vite` CLI using `bunx`.

The `--bun` flag tells Bun to run Vite's CLI using `bun` instead of `node`. By default, Bun respects Vite's `#!/usr/bin/env node` [shebang line](https://en.wikipedia.org/wiki/Shebang_(Unix)).

```bash
bunx --bun vite
```

***

To simplify this command, update the `"dev"` script in `package.json` to the following.

**File:** `package.json`
```json
  "scripts": {
    "dev": "vite",
    "dev": "bunx --bun vite",
    "build": "tsc -b && vite build",
    "lint": "oxlint",
    "preview": "vite preview"
  },
  // ...
```

***

Now you can start the development server with `bun run dev`.

```bash
bun run dev
```

***

Build your app for production.

```sh
bunx --bun vite build
```

***

For more information, see the [Vite documentation](https://vite.dev/guide/).

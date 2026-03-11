# Quickstart
Source: https://bun.com/docs/quickstart

Build your first app with Bun

## Overview

Build a minimal HTTP server with `Bun.serve`, run it locally, then evolve it by installing a package.

> Info: Prerequisites: Bun installed and available on your `PATH`. See [installation](/installation) for setup.

***

### Step 1
Initialize a new project with `bun init`.

```bash
bun init my-app
```

It'll prompt you to pick a template, either `Blank`, `React`, or `Library`. For this guide, we'll pick `Blank`.

```bash
bun init my-app
```

```txt
✓ Select a project template: Blank

- .gitignore
- CLAUDE.md
- .cursor/rules/use-bun-instead-of-node-vite-npm-pnpm.mdc -> CLAUDE.md
- index.ts
- tsconfig.json (for editor autocomplete)
- README.md
```

This automatically creates a `my-app` directory with a basic Bun app.

### Step 2
Run the `index.ts` file using `bun run index.ts`.

```bash
cd my-app
bun run index.ts
```

```txt
Hello via Bun!
```

You should see a console output saying `"Hello via Bun!"`.

### Step 3
Replace the contents of `index.ts` with the following code:

**File:** `index.ts`
```ts
const server = Bun.serve({
  port: 3000,
  routes: {
    "/": () => new Response('Bun!'),
  }
});

console.log(`Listening on ${server.url}`);
```

Run the `index.ts` file again using `bun run index.ts`.

```bash
bun run index.ts
```

```txt
Listening on http://localhost:3000
```

Visit [`http://localhost:3000`](http://localhost:3000) to test the server. You should see a simple page that says `"Bun!"`.

### Seeing TypeScript errors on Bun?
If you used `bun init`, Bun will have automatically installed Bun's TypeScript declarations and configured your `tsconfig.json`. If you're trying out Bun in an existing project, you may see a type error on the `Bun` global.

To fix this, first install `@types/bun` as a dev dependency.

```bash
bun add -d @types/bun
```

Then add the following to your `compilerOptions` in `tsconfig.json`:

**File:** `tsconfig.json`
```json
{
  "compilerOptions": {
    "lib": ["ESNext"],
    "target": "ESNext",
    "module": "Preserve",
    "moduleDetection": "force",
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "noEmit": true
  }
}
```

### Step 4
Install the `figlet` package and its type declarations. Figlet is a utility for converting strings into ASCII art.

```bash
bun add figlet
bun add -d @types/figlet # TypeScript users only
```

Update `index.ts` to use `figlet` in `routes`.

**File:** `index.ts`
```ts
import figlet from 'figlet';

const server = Bun.serve({
  port: 3000,
  routes: {
    "/": () => new Response('Bun!'),
    "/figlet": () => {
      const body = figlet.textSync('Bun!');
      return new Response(body);
    }
  }
});

console.log(`Listening on ${server.url}`);
```

Run the `index.ts` file again using `bun run index.ts`.

```bash
bun run index.ts
```

```txt
Listening on http://localhost:3000
```

Visit [`http://localhost:3000/figlet`](http://localhost:3000/figlet) to test the server. You should see a simple page that says `"Bun!"` in ASCII art.

```txt
____              _
| __ ) _   _ _ __ | |
|  _ \| | | | '_ \| |
| |_) | |_| | | | |_|
|____/ \__,_|_| |_(_)
```

### Step 5
Let's add some HTML. Create a new file called `index.html` and add the following code:

**File:** `index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bun</title>
  </head>
  <body>
    <h1>Bun!</h1>
  </body>
</html>
```

Then, import this file in `index.ts` and serve it from the root `/` route.

**File:** `index.ts`
```ts
import figlet from 'figlet';
import index from './index.html';

const server = Bun.serve({
  port: 3000,
  routes: {
    "/": index,
    "/figlet": () => {
      const body = figlet.textSync('Bun!');
      return new Response(body);
    }
  }
});

console.log(`Listening on ${server.url}`);
```

Run the `index.ts` file again using `bun run index.ts`.

```bash
bun run index.ts
```

```txt
Listening on http://localhost:3000
```

Visit [`http://localhost:3000`](http://localhost:3000) to test the server. You should see the static HTML page.

🎉 Congratulations! You've built a simple HTTP server with Bun and installed a package.

***

## Run a script

Bun can also execute `"scripts"` from your `package.json`. Add the following script:

**File:** `package.json`
```json
{
  "name": "quickstart",
  "module": "index.ts",
  "type": "module",
  "private": true,
  "scripts": {
    "start": "bun run index.ts"
  },
  "devDependencies": {
    "@types/bun": "latest"
  },
  "peerDependencies": {
    "typescript": "^5"
  }
}
```

Then run it with `bun run start`.

```bash
bun run start
```

```txt
Listening on http://localhost:3000
```

> Note: ⚡️ **Performance** — `bun run` is roughly 28x faster than `npm run` (6ms vs 170ms of overhead).

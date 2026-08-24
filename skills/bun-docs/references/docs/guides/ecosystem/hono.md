# Build an HTTP server using Hono and Bun
Source: https://bun.com/docs/guides/ecosystem/hono


[Hono](https://github.com/honojs/hono) is a lightweight web framework designed for the edge.

**File:** `server.ts`
```ts
import { Hono } from "hono";
const app = new Hono();

app.get("/", c => c.text("Hono!"));

export default app;
```

***

Use `create-hono` to get started with one of Hono's project templates. Select `bun` when prompted for a template.

```sh
bun create hono myapp
```

```txt
create-hono version 0.19.4
✔ Using target directory … myapp
✔ Which template do you want to use? bun
✔ Do you want to install project dependencies? Yes
✔ Which package manager do you want to use? bun
✔ Cloning the template
✔ Installing project dependencies
🎉 Copied project files
Get started with: cd myapp
```

```sh
cd myapp
bun install
```

***

Then start the dev server and visit [localhost:3000](http://localhost:3000).

```sh
bun run dev
```

***

Refer to Hono's [getting started with Bun](https://hono.dev/docs/getting-started/bun) guide.

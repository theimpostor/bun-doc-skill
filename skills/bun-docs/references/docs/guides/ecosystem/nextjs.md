# Build an app with Next.js and Bun
Source: https://bun.com/docs/guides/ecosystem/nextjs


[Next.js](https://nextjs.org/) is a React framework for building full-stack web applications. It supports server-side rendering, static site generation, and API routes. Bun installs packages fast and can run Next.js development and production servers.

***

### Create a new Next.js app
Use the interactive CLI to scaffold a new Next.js project and install its dependencies.

```sh
bun create next-app@latest my-bun-app
```

### Start the dev server
Change to the project directory and run the dev server with Bun.

```sh
cd my-bun-app
bun --bun run dev
```

This starts the Next.js dev server with Bun's runtime.

Open [`http://localhost:3000`](http://localhost:3000) in your browser to see the result. Changes you make to `app/page.tsx` are hot-reloaded in the browser.

### Update scripts in package.json
Prefix the Next.js CLI commands in your `package.json` scripts with `bun --bun` so that Bun executes the Next.js CLI for `dev`, `build`, and `start`.

**File:** `package.json`
```json
{
  "scripts": {
    "dev": "bun --bun next dev",
    "build": "bun --bun next build",
    "start": "bun --bun next start"
  }
}
```

***

## Hosting

### Vercel
Link: `/guides/deployment/vercel`
Deploy on Vercel

### Railway
Link: `/guides/deployment/railway`
Deploy on Railway

### DigitalOcean
Link: `/guides/deployment/digital-ocean`
Deploy on DigitalOcean

### AWS Lambda
Link: `/guides/deployment/aws-lambda`
Deploy on AWS Lambda

### Google Cloud Run
Link: `/guides/deployment/google-cloud-run`
Deploy on Google Cloud Run

### Render
Link: `/guides/deployment/render`
Deploy on Render

***

## Templates

### Bun + Next.js Basic Starter
Link: `https://github.com/bun-templates/bun-nextjs-basic`
A basic App Router starter with Bun, Next.js, and Tailwind CSS.

### Todo App with Next.js + Bun
Link: `https://github.com/bun-templates/bun-nextjs-todo`
A full-stack todo application built with Bun, Next.js, and PostgreSQL.

***

Refer to the [Next.js documentation](https://nextjs.org/docs) for more on building and deploying Next.js applications.

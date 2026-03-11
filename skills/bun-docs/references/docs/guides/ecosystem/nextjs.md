# Build an app with Next.js and Bun
Source: https://bun.com/docs/guides/ecosystem/nextjs


[Next.js](https://nextjs.org/) is a React framework for building full-stack web applications. It supports server-side rendering, static site generation, API routes, and more. Bun provides fast package installation and can run Next.js development and production servers.

***

### Create a new Next.js app
Use the interactive CLI to create a new Next.js app. This will scaffold a new Next.js project and automatically install dependencies.

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

Open [`http://localhost:3000`](http://localhost:3000) with your browser to see the result. Any changes you make to `app/page.tsx` will be hot-reloaded in the browser.

### Update scripts in package.json
Modify the scripts field in your `package.json` by prefixing the Next.js CLI commands with `bun --bun`. This ensures that Bun executes the Next.js CLI for common tasks like `dev`, `build`, and `start`.

**File:** `package.json`
```json
{
  "scripts": {
    "dev": "bun --bun next dev",
    "build": "bun --bun next build",
    "start": "bun --bun next start",
  }
}
```

***

## Hosting

Next.js applications on Bun can be deployed to various platforms.

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
A simple App Router starter with Bun, Next.js, and Tailwind CSS.

### Todo App with Next.js + Bun
Link: `https://github.com/bun-templates/bun-nextjs-todo`
A full-stack todo application built with Bun, Next.js, and PostgreSQL.

***

[→ See Next.js's official documentation](https://nextjs.org/docs) for more information on building and deploying Next.js applications.

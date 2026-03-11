# Install dependencies with Bun in GitHub Actions
Source: https://bun.com/docs/guides/install/cicd


Use the official [`setup-bun`](https://github.com/oven-sh/setup-bun) GitHub Action to install `bun` in your GitHub Actions runner.

**File:** `workflow.yml`
```yaml
title: my-workflow
jobs:
  my-job:
    title: my-job
    runs-on: ubuntu-latest
    steps:
      # ...
      - uses: actions/checkout@v4
      - uses: oven-sh/setup-bun@v2

      # run any `bun` or `bunx` command
      - run: bun install
```

***

To specify a version of Bun to install:

**File:** `workflow.yml`
```yaml
title: my-workflow
jobs:
  my-job:
    title: my-job
    runs-on: ubuntu-latest
    steps:
      # ...
      - uses: oven-sh/setup-bun@v2
         with:
          version: "latest" # or "canary"
```

***

Refer to the [README.md](https://github.com/oven-sh/setup-bun) for complete documentation of the `setup-bun` GitHub Action.

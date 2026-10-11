---
name: bun-docs
description: Consult Bun's official documentation snapshot for runtime APIs, `bun` CLI commands, `bunfig.toml`, package management, bundling, type checking, testing, deployment guides, and ecosystem integrations. Use this whenever the user asks how to do something with Bun, troubleshoot Bun-specific behavior, compare Bun to Node/npm, or wants Bun command or API guidance, even if they only mention a command like `bun install`, `bun test`, `bun build`, `bun check`, `bunx`, `Bun.serve`, or a Bun config option.
---

# Bun Docs

Use this skill to answer Bun-specific questions from the bundled official documentation. Check `references/index.md` for the snapshot date, source, and Git ref when pinned to a release.

## What this skill is for

- Ground Bun answers in the official docs snapshot instead of memory.
- Find the smallest relevant doc page or pages before answering.
- Quote commands, config keys, API names, and caveats accurately.
- Say when the bundled snapshot appears insufficient or when a question likely depends on a newer Bun release.

## Workflow

1. Open `references/index.md`.
2. Choose the most relevant section overview in `references/sections/`.
3. From that section file, open only the specific page files you need under `references/docs/`.
4. Answer the user with Bun-specific guidance, using the doc pages as the primary source of truth.

## Source selection

- Start narrow. If the user asks about `bun test --coverage`, open the test runner section and then the coverage or configuration page, not the whole runtime.
- If the request mixes Bun with a framework, use the Bun docs for the Bun-specific part and the local repository for project-specific code.
- If the question is about installation, onboarding, or "what is Bun?", start with `references/sections/getting-started.md`.
- If the request is about commands like `bun add`, `bun install`, `bun dedupe`, `bun prune`, `bun publish`, or registries, start with the package-manager section.
- If the request is about `Bun.serve`, routing, TLS, cookies, or WebSockets, start with the runtime HTTP section.
- If the request is about `bun build`, executables, CSS, HTML imports, minification, macros, or plugins, start with the bundler section.
- If the request is about parallel or isolated tests, lifecycle hooks, mocks, snapshots, coverage, or reporters, start with the test runner section.
- If the request is about Bun's built-in support for XML, YAML, JSON5, JSONL, TOML, or Markdown, start with the runtime section.
- If the request is about `bun check` or `--check` before running, building, or testing, open `references/docs/runtime/check.md`.
- If the request is about `Bun.FetchSession`, connection pools, or fetch proxies, open `references/docs/runtime/networking/fetch.md`.
- If the request is about `Bun.ModuleGraph`, open `references/docs/runtime/module-graph.md` and preserve its experimental status and lifecycle caveats.
- If the request is a recipe-style question like deployment, framework setup, file conversion, or HTTP examples, start with the relevant guides section.

## Answering guidance

- Lead with the direct answer, then include the Bun command, config snippet, or code example the user needs.
- Keep Bun terminology exact. If the docs distinguish Bun runtime behavior from Node compatibility behavior, preserve that distinction.
- Mention the relevant doc page names when useful so the user can inspect them.
- If the snapshot does not clearly answer the question, say so instead of filling gaps with guesses.

## Version awareness

- This skill uses a local snapshot of the Bun docs, not a live browse of bun.com.
- If the user asks for the latest Bun behavior, release-specific changes, or something that seems newer than the snapshot, say that the reference may need refresh and verify online if tools allow.
- To refresh from the live combined feed, run `python3 scripts/refresh_references.py` from this skill's directory.
- For a specific release, run `python3 scripts/refresh_references.py --ref bun-vX.Y.Z`, replacing `X.Y.Z` with the requested version. This reads the official repository at that tag, including CLI snippets; the combined feed can lag new releases.

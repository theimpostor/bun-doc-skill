# Repository Guidelines

## Project Structure & Module Organization

This repository contains a single skill package, `skills/bun-docs/`. This is a repackaging of the [Bun](https://bun.com) [documentation](https://bun.com/docs).io). The existing [llms.txt](https://bun.sh/llms-full.txt) is split into multiple files (300+) for easier agent navigation with extraneous markup removed.

- `skills/bun-docs/SKILL.md`: the skill definition, trigger description, and usage guidance.
- `skills/bun-docs/scripts/refresh_references.py`: regenerates the bundled Bun docs snapshot.
- `skills/bun-docs/references/index.md`: entry point for navigating the local docs mirror.
- `skills/bun-docs/references/sections/`: 25 section overview files used to pick relevant docs quickly.
- `skills/bun-docs/references/docs/`: generated per-page Bun documentation files.

Do not hand-edit files under `skills/bun-docs/references/docs/` unless you are debugging generation output; regenerate them instead.

## Build, Test, and Development Commands

- `python3 skills/bun-docs/scripts/refresh_references.py`: download and rebuild the cleaned Bun reference tree from `https://bun.sh/llms-full.txt`.
- `rg 'theme=\\{| icon=\"|\\[!code|<Tabs>|<ParamField' skills/bun-docs/references/docs`: quick audit for leftover MDX/site markup after regeneration.

There is no separate app build or test runner in this repository.

## Coding Style & Naming Conventions

Use Python 3 with 4-space indentation and standard-library-only code unless a dependency is clearly justified. Keep `SKILL.md` concise, imperative, and specific to Bun workflows. Use lowercase, hyphenated names for skill and section files; keep generated doc paths aligned with Bun doc paths under `skills/references/docs/...`.

## Testing Guidelines

Testing is lightweight and file-based:

- Re-run `refresh_references.py` after script changes.
- Compile the script with `py_compile`.
- Run the markup audit command and spot-check a few generated docs such as `installation.md` or `pm/cli/publish.md`.

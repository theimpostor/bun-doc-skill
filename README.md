# Bun Documentation Skill

[Bun](https://bun.com) [documentation](https://bun.com/docs) packaged as an [agent skill](https://agentskills.io). The documentation is split into 1,300+ files for easier agent navigation with extraneous markup removed, including formatter docs and the canary-only linter's rule catalog.

The bundled snapshot uses the official `bun-v1.4.4` release tag. Regenerate it with:

```sh
python3 skills/bun-docs/scripts/refresh_references.py --ref bun-v1.4.4
```

Omit `--ref` to refresh from the combined docs feed, which can lag new releases. Snapshot provenance is recorded in `skills/bun-docs/references/index.md` and `metadata.json`.

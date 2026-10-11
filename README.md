# Bun Documentation Skill

[Bun](https://bun.com) [documentation](https://bun.com/docs) packaged as an [agent skill](https://agentskills.io). The existing [llms.txt](https://bun.sh/llms-full.txt) is split into multiple files (300+) for easier agent navigation with extraneous markup removed.

The bundled snapshot uses the official `bun-v1.4.3` release tag. Regenerate it with:

```sh
python3 skills/bun-docs/scripts/refresh_references.py --ref bun-v1.4.3
```

Omit `--ref` to refresh from the combined docs feed, which can lag new releases. Snapshot provenance is recorded in `skills/bun-docs/references/index.md` and `metadata.json`.

# Design to Ship contributor instructions

This repository maintains one canonical workflow in `skills/design-to-ship/SKILL.md`. Keep vendor adapters thin and do not fork the methodology into separate copies.

## Working rules

- Read the canonical skill and the directly relevant reference before changing workflow behavior.
- Preserve traceability across evidence (`E-*`), requirements (`R-*`), decisions (`D-*`), and verification.
- Never present invented research, test results, accessibility compliance, or user approval as fact.
- Keep `SKILL.md` concise; place detailed guidance in a directly linked file under `references/`.
- Prefer vendor-neutral language in the canonical skill. Put platform-specific installation details in `docs/compatibility.md`.
- Add or update a fixture when changing schemas, verdict logic, or required deliverables.
- Run `python3 scripts/validate.py` before reporting completion.

## Release rules

- Keep versions synchronized across `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, and `VERSION`.
- Treat compatibility claims as tested claims. Mark untested integrations accurately.
- Do not add runtime dependencies without a demonstrated need.


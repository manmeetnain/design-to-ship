# Migration guide

## From 0.x to 1.0

The five gates, operating modes, evidence states, identifier prefixes, capability levels, and verdicts are now stable.

Existing 0.2–0.5 contracts should:

1. Add `screens` when screen/state traceability is relevant.
2. Add `verifications` for performed checks.
3. Ensure every passing verification includes evidence.
4. Resolve material `UNKNOWN` or `CONFLICTING` evidence before using `READY`.
5. Name the next stage represented by the verdict in human-readable reports.

Run:

```bash
PYTHONPATH=src python3 -m design_to_ship validate path/to/project.json
PYTHONPATH=src python3 -m design_to_ship trace path/to/project.json
```

Warnings remain non-blocking unless the specification marks the underlying behavior as required. Errors indicate a contract contradiction or missing required structure.

## Future major versions

Major migrations will document changed normative language, schema differences, CLI behavior, skill activation, and required benchmark updates. Historical schemas and migration notes will remain available in tagged releases.


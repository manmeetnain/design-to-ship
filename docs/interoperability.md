# Interoperability

The canonical workflow is `skills/design-to-ship/SKILL.md`. Host-specific manifests and instruction files point to it without redefining the method.

## Portable minimum

An agent host can use Design to Ship if it can read Markdown and relevant project artifacts. Native skill discovery improves activation and progressive disclosure but is not required for method conformance.

## Host behavior

| Host feature | Design to Ship behavior |
|---|---|
| Skill discovery | Load the canonical name and description, then the body on demand |
| Repository instructions | Point to the canonical skill for design-related tasks |
| Files and images | Record inspected artifacts as evidence |
| Design connector | Extract structured nodes, variables, components, and source identifiers |
| Code editing | Preserve local conventions and run repository checks |
| Browser/device control | Execute acceptance criteria and capture evidence |
| Parallel agents | Partition by artifact or verification surface; preserve one shared contract |

## Multi-agent coordination

Use one coordinator to own the evidence ledger and verdict. Specialists may work on research synthesis, experience structure, system design, implementation, and verification, but they must return stable identifiers and evidence rather than disconnected prose.

Do not assign the same requirement to independent agents without a reconciliation step. Do not let the implementation agent approve its own unreviewed verification when an independent verification surface is available.

## Optional tool connections

Design to Ship does not require any external service. Connectors for product documents, issue trackers, analytics, Figma, source control, browsers, simulators, or accessibility tools increase evidence capability. They must honor host permissions and must never be treated as implicitly authorized.


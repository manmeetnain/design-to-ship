# Beacon — complete Design to Ship example

Beacon is a fictional incident-triage workspace for small software teams. This example starts with a short product brief and carries it through structure, system, implementation, and recorded proof.

The example is intentionally honest: product requirements are hypothetical, and verification claims cover only the included static prototype and automated checks.

## Brief

Small software teams receive incident signals from monitoring tools, support, and colleagues. During an incident, responders lose time deciding what is active, who owns it, and what changed most recently.

Beacon should let an on-call responder:

1. Identify the highest-priority unresolved incident.
2. See ownership and the latest meaningful update.
3. Acknowledge an incident without opening a separate detail page.
4. Use the core queue at a 375 px viewport and with a keyboard.

The first release is a read-focused queue demonstration. Authentication, integrations, persistence, notification delivery, and production incident-management policies are outside this example.

## Intent

**Outcome:** Reduce the time required to understand and acknowledge the next incident requiring action.

**Primary user:** An on-call engineer entering the queue with limited context and elevated time pressure.

**Success signals:** Time to identify the first actionable incident; successful keyboard acknowledgement; correct recognition of priority, ownership, and status.

**Non-goals:** Replacing a full incident-command system, editing runbooks, managing schedules, or simulating backend persistence.

See [project.json](project.json) for the complete evidence, requirement, decision, screen, and verification contract.

## Structure

```text
Queue
├── Status summary
├── Filters
├── Incident list
│   ├── Priority and status
│   ├── Incident identity
│   ├── Owner and latest update
│   └── Acknowledge action
└── Selection detail
    ├── Summary
    ├── Ownership
    └── Timeline
```

The desktop layout uses a queue-and-detail relationship. At narrow widths, the detail panel follows the queue so priority and action remain first.

## System

- **Principle — calm urgency:** Reserve warm colors for genuine priority; keep the surrounding system quiet.
- **Principle — scan before read:** Align priority, identity, ownership, and time consistently.
- **Principle — state is language:** Pair color with explicit labels and live status text.
- **Typography:** System sans-serif for fast rendering and familiar shapes; tabular numerals for time-sensitive metrics.
- **Color:** Deep navy environment, high-contrast neutral text, coral for critical, amber for elevated, cyan for focus and active structure.
- **Motion:** No decorative motion. Status updates change text and announce through a live region.

## Build

The dependency-free prototype uses semantic HTML, CSS custom properties, responsive grid rules, and a small JavaScript interaction. Open [prototype/index.html](prototype/index.html) directly or serve this directory with a local HTTP server.

## Proof

The repository validator checks the contract and traceability. The prototype verification report records the inspected scope and known limitations in [verification.md](verification.md).

```bash
PYTHONPATH=src python3 -m design_to_ship validate examples/beacon/project.json
PYTHONPATH=src python3 -m design_to_ship trace examples/beacon/project.json
```


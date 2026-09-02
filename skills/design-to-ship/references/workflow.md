# Five-gate workflow

## Gate 1 — Intent

Required outputs:

- One-sentence product outcome
- Primary and secondary users
- Jobs, pain points, and critical context
- Confirmed constraints and explicit non-goals
- Success signals and failure risks
- Evidence ledger with stable requirement IDs

Pass when the team can explain what success means without naming a UI pattern.

## Gate 2 — Structure

Required outputs:

- Content and object model
- Information architecture
- Primary journey plus alternate and recovery paths
- State inventory
- Permission and data considerations

Pass when each critical job has an understandable path, including failure and recovery.

## Gate 3 — System

Required outputs:

- Design principles tied to product context
- Visual direction with rationale and anti-patterns
- Semantic tokens and type/spacing/layout rules
- Component and interaction behavior
- Responsive, accessibility, content, and motion rules

Pass when another designer could extend the product coherently without copying a screenshot.

## Gate 4 — Build

Required outputs:

- Screen-to-component map
- Requirement-to-acceptance-criteria trace
- Implementation notes for the target platform
- Asset, data, and dependency list
- Verification plan

Pass when an engineer can implement behavior and states without guessing consequential details.

## Gate 5 — Proof

Required outputs:

- Functional checks
- Visual comparison or inspection evidence
- Responsive checks at relevant widths
- Keyboard, focus, contrast, semantics, and reduced-motion checks
- Content stress tests
- Known gaps and readiness verdict

Pass only when evidence supports the acceptance criteria.

## Stopping rules

Stop and request a decision when an unknown changes legal or safety exposure, user permissions, destructive behavior, core data architecture, brand ownership, or the primary product outcome. Continue with labeled proposals for reversible visual and interaction details.


# Method

Design to Ship treats design as a chain of accountable decisions rather than a sequence of pictures.

## The traceability chain

```text
Evidence → Requirement → Decision → Artifact → Acceptance criterion → Verification
```

A gap anywhere in this chain creates a recognizable failure:

- Evidence without requirements becomes unused research.
- Requirements without decisions become a feature list.
- Decisions without artifacts remain opinion.
- Artifacts without acceptance criteria become ambiguous handoff.
- Acceptance criteria without verification become unproven claims.

## Five gates

### Intent

Establish the outcome, audience, evidence, constraints, success signals, non-goals, and unresolved decisions. Pass when the team can define success without naming a UI pattern.

### Structure

Define the object model, information architecture, journeys, permissions, states, and recovery. Pass when critical jobs remain understandable outside the happy path.

### System

Create a coherent visual and behavioral language tied to the product context. Pass when another designer can extend it without copying a screenshot.

### Build

Translate approved intent into reusable components, platform behavior, content contracts, data needs, and requirement-linked acceptance criteria. Pass when implementation no longer depends on consequential guessing.

### Proof

Inspect the result across relevant states and contexts. Pass only when evidence supports functional, visual, responsive, accessible, and content-resilience claims.

## Evidence language

Use `CONFIRMED`, `INFERRED`, `PROPOSED`, `UNKNOWN`, and `CONFLICTING` consistently. These are epistemic labels—not workflow statuses. Something can be beautifully designed and still be based on an unknown assumption.

## Readiness language

Every run ends in one verdict: `READY`, `READY WITH RISKS`, `REVISE`, or `BLOCKED`. A verdict represents readiness for the next named stage, not permanent product quality.


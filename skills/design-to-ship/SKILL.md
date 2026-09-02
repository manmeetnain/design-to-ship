---
name: design-to-ship
description: Turn product requirements into distinctive, accessible, implementation-ready interfaces and verify the finished result with evidence. Use when designing or redesigning a digital product, defining UX flows or information architecture, creating a design system, specifying responsive screens and states, translating design into implementation guidance, reviewing an existing interface, or auditing whether a build fulfills its product and design intent.
---

# Design to Ship

Move through five gates: Intent, Structure, System, Build, and Proof. Preserve traceability from requirement to implementation. Never invent research, evidence, constraints, or user approval.

## Start with the operating mode

Select one mode and state it in the deliverable:

- `EXPLORE`: Turn an early idea into a testable product direction.
- `DEFINE`: Convert known requirements into architecture, flows, and specifications.
- `DESIGN`: Produce a coherent visual system and screen-level direction.
- `BUILD`: Translate approved design intent into implementation-ready guidance or code.
- `AUDIT`: Evaluate an existing design or implementation against its intent.
- `FULL`: Run the complete workflow.

Read [workflow.md](references/workflow.md) for gate requirements and stopping rules. Read [deliverables.md](references/deliverables.md) before producing artifacts. For review or verification, also read [quality-rubric.md](references/quality-rubric.md) and [verification-recipes.md](references/verification-recipes.md). For implementation work, read [implementation.md](references/implementation.md). For accessibility-sensitive work, read [accessibility.md](references/accessibility.md).

When the repository library is available, consult `library/product-playbooks.json` for domain context, `library/ux-patterns.json` for specific journeys, `library/content-stress.json` for resilience cases, and `library/anti-patterns.json` during critique. Treat library guidance as contextual heuristics, not user research or universal rules.

## Establish the evidence ledger

Before designing, classify consequential statements:

- `CONFIRMED`: Explicitly supplied or supported by inspected evidence.
- `INFERRED`: Strongly implied; include the reasoning.
- `PROPOSED`: A reversible design recommendation.
- `UNKNOWN`: Material information that is not available.
- `CONFLICTING`: Sources disagree; preserve both claims.

Do not silently convert an inference into a fact. Ask only about unknowns that would substantially change scope, safety, architecture, or product direction. Otherwise proceed with clearly labeled assumptions.

## Apply the five gates

### 1. Intent

Define the outcome, users, jobs, constraints, success signals, risks, content needs, and non-goals. Rewrite feature requests as user or business outcomes where possible. Create requirement IDs such as `R-01` so later decisions can cite them.

### 2. Structure

Model the information architecture, primary journeys, navigation, permissions, data dependencies, and recovery paths. Include empty, loading, error, offline, partial, destructive, success, and first-use states when relevant.

### 3. System

Choose a defensible visual direction based on audience, context, brand, density, platform, and content—not trend imitation. Define semantic tokens, typography, spacing, layout, component behavior, interaction states, motion, responsiveness, accessibility, and explicit anti-patterns.

### 4. Build

Map screens to reusable components and requirements to acceptance criteria. Reuse an existing product's components and tokens before creating new ones. Specify behavior before decoration. Treat generated code as incomplete until verified in its target environment.

### 5. Proof

Verify the implementation at representative breakpoints and states. Check functional behavior, visual hierarchy, content integrity, accessibility, responsiveness, resilience, and alignment with confirmed intent. Attach evidence and distinguish observed results from untested claims.

State the host capability level used: `L1 Reason`, `L2 Inspect`, `L3 Build`, or `L4 Prove`. Never claim results from a higher level than the available tools and evidence support.

## Make design decisions

For every consequential decision, record:

1. The requirement or evidence it serves.
2. The chosen approach.
3. The rejected credible alternative.
4. The tradeoff.
5. How the decision will be verified.

Avoid interchangeable AI aesthetics. Do not default to purple gradients, excessive cards, glass effects, generic hero copy, decorative charts, or animation without a product reason. Distinctiveness must come from the product's content, behavior, voice, and constraints.

## Finish with a verdict

Return exactly one readiness verdict:

- `READY`: All required gates pass and material claims have evidence.
- `READY WITH RISKS`: The output can advance, with named non-blocking risks.
- `REVISE`: Important gaps remain but can be resolved within the current direction.
- `BLOCKED`: A missing decision or dependency makes responsible progress impossible.

List evidence, unresolved items, and the next smallest action. Never report a gate as passed solely because an artifact exists.

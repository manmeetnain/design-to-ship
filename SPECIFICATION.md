# Design to Ship specification 1.0

**Status:** Stable  
**Version:** 1.0.0

Design to Ship defines a vendor-neutral contract for carrying product intent into implementation and recording evidence about the result.

## Normative language

The terms **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** describe conformance requirements.

## Required concepts

A conforming workflow MUST:

1. Identify its operating mode and intended next stage.
2. Separate confirmed evidence from inference, proposals, unknowns, and conflicts.
3. Give stable identifiers to evidence, requirements, and consequential decisions.
4. Link requirements to supporting evidence.
5. Link consequential decisions to requirements and a verification method.
6. Include relevant non-default, failure, and recovery states.
7. Distinguish planned verification from performed verification.
8. State the capability level used.
9. End with one readiness verdict.

A workflow MUST NOT claim user research, inspection, testing, compliance, or approval that did not occur.

## Operating modes

- `EXPLORE`: Frame an early opportunity and testable direction.
- `DEFINE`: Produce structure, journeys, content, and requirements.
- `DESIGN`: Produce a visual and behavioral system.
- `BUILD`: Translate approved intent into implementation.
- `AUDIT`: Evaluate an existing design or implementation.
- `FULL`: Run all applicable gates.

## Evidence states

- `CONFIRMED`: Explicit input or inspected evidence supports the claim.
- `INFERRED`: Available evidence strongly implies the claim; reasoning is recorded.
- `PROPOSED`: A reversible recommendation awaiting acceptance or validation.
- `UNKNOWN`: Material information is unavailable.
- `CONFLICTING`: Available sources disagree.

## Required traceability

```text
Evidence (E-*) → Requirement (R-*) → Decision (D-*)
                                      ↓
                              Verification (V-*)
```

Requirements SHOULD include observable acceptance criteria. Decisions SHOULD record a credible alternative and tradeoff. Passing verification MUST include evidence.

## Five gates

1. **Intent:** outcome, audience, evidence, constraints, success, risks, and non-goals.
2. **Structure:** object model, information architecture, journeys, permissions, states, and recovery.
3. **System:** principles, tokens, components, behavior, content, motion, responsiveness, and accessibility.
4. **Build:** screen/component mapping, platform behavior, data needs, acceptance criteria, and verification plan.
5. **Proof:** observed functional, visual, responsive, accessibility, resilience, and intent-fidelity evidence.

Not every mode produces every gate. `FULL` MUST address all five.

## Capability levels

- `L1 Reason`: Work from supplied text and context.
- `L2 Inspect`: Inspect product, design, image, or repository evidence.
- `L3 Build`: Change an implementation and execute local checks.
- `L4 Prove`: Exercise the result through an interactive verification surface.

An output MUST NOT claim evidence requiring a higher capability level than was available.

## Verdicts

- `READY`: Required gates pass; material claims and acceptance criteria have evidence.
- `READY WITH RISKS`: Work can advance with explicit non-blocking risks.
- `REVISE`: Important gaps remain within the current direction.
- `BLOCKED`: A missing decision or dependency prevents responsible progress.

The verdict MUST name the next stage for which readiness is being assessed.

## Machine-readable contract

Projects MAY serialize this model using `schemas/design-project.schema.json`. Extensions SHOULD use namespaced properties or a separately versioned schema until adopted into the core specification.

## Conformance levels

- **Method-conformant:** Satisfies the required concepts in a human-readable artifact.
- **Contract-conformant:** Also validates against the versioned project schema.
- **Evidence-conformant:** Also includes reproducible proof for every passing material requirement.


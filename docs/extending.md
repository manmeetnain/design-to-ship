# Extending Design to Ship

Design to Ship has a conservative, vendor-neutral core and explicit extension points. Extensions add reach without creating a competing copy of the methodology.

## Extension rules

Every extension must:

1. preserve the five gates and verdict meanings;
2. preserve traceability across `E-*`, `R-*`, `D-*`, and `V-*` records;
3. distinguish observed, inferred, proposed, unknown, and conflicting information;
4. claim only capabilities and compatibility that were actually tested;
5. document inputs, outputs, limitations, ownership, and verification;
6. keep vendor-specific behavior outside the canonical `SKILL.md`;
7. include a representative example and a maintenance plan.

## Add an AI model or host adapter

Use an adapter when a model, agent host, IDE, or automation platform needs installation instructions or capability translation.

- Put setup and invocation guidance in `docs/compatibility.md` or a thin host manifest.
- Map available capabilities to Reason, Inspect, Build, and Prove.
- Explain what the host cannot inspect or verify.
- Never duplicate or rewrite the canonical workflow for a vendor.
- Test installation, invocation, artifact access, and at least one realistic workflow.

## Add an agent skill

The canonical skill lives at `skills/design-to-ship/SKILL.md`. A compatible skill should reference that contract rather than fork it.

- Keep discovery metadata concise and accurate.
- Put detailed knowledge in directly linked references.
- Preserve mode names, gates, evidence states, and verdicts.
- Add trigger and behavior cases when activation or workflow behavior changes.
- Verify that the host does not claim unavailable inspection, execution, or proof.

## Add a framework or platform playbook

Put framework guidance under `library/frameworks/` and platform guidance under `library/platforms/`.

- Describe how existing tokens, components, routes, states, and tests are discovered.
- Cover responsive behavior, accessibility, loading, error, empty, permission, and recovery states.
- Prefer native conventions unless a documented product decision justifies divergence.
- Include implementation checks, not only code snippets.
- Link the playbook from the relevant library index or documentation surface.

## Add a benchmark

Benchmarks protect the contract from fluent but invalid output.

- Add a minimal fixture under `benchmarks/fixtures/`.
- Declare the expected verdict or failure condition.
- Include both a passing case and the nearest important failure case.
- Avoid subjective visual scoring without a reproducible rubric and evidence.
- Update `benchmarks/cases.json` and run `python3 benchmarks/run.py`.

## Publish a compatible integration

An external tool may describe itself as “compatible with Design to Ship” when it:

- produces or consumes the documented contract without changing required semantics;
- preserves source and verification provenance;
- documents the Design to Ship version tested;
- publishes known limitations;
- does not imply official certification, partnership, or endorsement.

Use “Built with Design to Ship” for products that apply the workflow. Use “Design to Ship compatible” for tools that interoperate with its contract. Do not use “official” unless the project governance explicitly grants that status.

## Proposal and review path

1. Open an extension proposal using the GitHub issue form.
2. Agree on scope, ownership, compatibility, and verification before substantial work.
3. Open a pull request using the repository template.
4. Run `python3 scripts/validate.py` plus relevant tests and benchmarks.
5. Address maintainer review and automated checks.
6. Merge, credit contributors, and include user-visible changes in release notes.


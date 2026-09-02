# Governance

Design to Ship is maintained as an open method with a conservative core and an extensible knowledge library.

## Decision principles

Changes are judged by whether they improve product truth, traceability, user outcomes, implementation clarity, accessibility, evidence quality, or interoperability. Popularity of a visual trend is not sufficient evidence.

## Change classes

- **Editorial:** Clarifies wording without changing conformance.
- **Library:** Adds contextual patterns, playbooks, examples, or framework guidance.
- **Compatible contract:** Adds optional schema fields or tooling without invalidating conforming projects.
- **Breaking:** Changes required concepts, identifiers, evidence states, verdict meaning, or removes supported behavior.

Breaking changes require a major release and migration guidance. Compatible contract changes require a minor release. Editorial corrections and fixes use patch releases.

## Proposal requirements

A substantive proposal must include context, intended outcome, rejected alternative, compatibility impact, verification approach, and representative example. Normative changes require benchmark cases.

## Maintainer responsibility

Maintainers review evidence quality, scope, accessibility impact, security implications, and compatibility. They may reject large catalogs that lack provenance, context, retrieval design, or a maintenance plan.

Changes to the canonical workflow, schemas, governance, security policy, and release surfaces require code-owner review. The `main` branch is protected: contributions enter through pull requests, required validation must pass, and review conversations must be resolved before merge.

Maintainers credit merged contributions through Git history and release notes. Sustained contributors may be invited into scoped ownership as the project grows; ownership decisions remain explicit and reviewable.

## Version support

The latest stable major version receives fixes. Security issues may be backported when impact and maintainability justify it.

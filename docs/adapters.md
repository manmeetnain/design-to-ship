# Adapter contracts

Adapters connect external product, design, code, or verification tools to the vendor-neutral Design to Ship contract. An adapter should gather evidence or export artifacts; it must not silently change the method.

## Product-source adapter

Input: PRDs, issues, research notes, analytics, support evidence, or content.

Output: evidence records with source, status, claim, materiality, and optional timestamp. Preserve conflicts and access boundaries.

## Design-source adapter

Input: Figma or another inspectable design artifact.

Output: screens, component instances, variables/tokens, interaction states, responsive constraints, assets, and source node identifiers. Screenshots are supporting evidence, not a substitute for structure when structured context exists.

## Codebase adapter

Input: repository files and executable project commands.

Output: framework, routes, tokens, components, data boundaries, test commands, and mappings to Design to Ship requirements. Never replace an established system without recording the tradeoff.

## Verification adapter

Input: implementation URL or executable application plus acceptance criteria.

Output: verification records containing method, environment, requirement IDs, result, evidence, and limitations. Preserve screenshots, logs, and machine-readable reports where permitted.

## Figma sequence

1. Inspect the target file, relevant pages, variables, and component library.
2. Map existing tokens and components before creating anything.
3. Associate frames and components with requirement and decision identifiers.
4. Make changes incrementally and preserve design-system bindings.
5. Capture source node identifiers and screenshots for verification.

The repository does not require a Figma connection. When unavailable, use exported artifacts and label the lower evidence level.


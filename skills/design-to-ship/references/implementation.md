# Implementation guidance

## Inspect before proposing

When a codebase exists, identify its framework, routing, styling approach, design tokens, component library, state management, data layer, validation, tests, and established conventions. Reuse the local system unless a confirmed requirement makes it insufficient.

## Build contract

For each screen or flow, define:

- Requirements served
- Components reused, extended, and introduced
- Data inputs, mutations, permissions, and validation
- Default, hover, focus, active, disabled, selected, loading, empty, error, success, and destructive states as applicable
- Responsive behavior driven by content and tasks
- Keyboard and assistive-technology behavior
- Acceptance criteria and verification method

## Implementation priorities

1. Correct product behavior
2. Semantic structure and accessible interaction
3. Content and state completeness
4. Responsive resilience
5. Visual fidelity and motion
6. Performance and maintainability

Do not use this priority order to excuse poor visual quality. Use it to prevent polish from hiding broken fundamentals.

## Evidence bundle

Where tools permit, preserve:

- Commands and tests executed
- Viewports and states inspected
- Screenshots or recordings with context
- Accessibility checks and manual keyboard results
- Known gaps and untested claims
- Requirement-linked verdict


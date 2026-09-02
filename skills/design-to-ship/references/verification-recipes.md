# Verification recipes

Select checks from the requirement and risk profile; do not mechanically claim every recipe ran.

## Responsive recipe

1. Identify actual layout transition points from content constraints.
2. Inspect just below and above each transition.
3. Include the narrowest supported viewport and a representative wide viewport.
4. Stress long labels, dense rows, open overlays, keyboards, and 200% zoom.
5. Check both visual order and keyboard/focus order.
6. Record viewport, environment, screenshot, overflow, clipping, and unresolved risks.

## Interaction recipe

1. Run the primary task from a clean state.
2. Exercise alternate, cancel, retry, and destructive paths.
3. Interrupt network or long-running work when relevant.
4. Verify visible feedback, preserved input, focus placement, and status announcements.
5. Repeat the critical path using keyboard input.

## Accessibility recipe

1. Inspect semantic structure, names, roles, relationships, and heading order.
2. Complete the critical journey with keyboard input.
3. Check visible focus and focus restoration after overlays or route changes.
4. Test zoom/reflow, text scaling, contrast, non-color cues, and reduced motion.
5. Use automated scanning as a defect finder, not a certification.
6. Test with relevant assistive technology when scope and risk require it.

## Visual recipe

1. Capture named viewports and deterministic states.
2. Compare hierarchy, spacing, typography, tokens, content, and component states.
3. Separate intentional implementation adaptations from unexplained drift.
4. Never let pixel similarity override incorrect behavior or inaccessible semantics.


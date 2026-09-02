# Quality rubric

Score each dimension from 0 to 4. A high visual score cannot compensate for broken behavior or inaccessible interaction.

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| Intent fidelity | Contradicts the brief | Supports main goal with gaps | Every major choice traces to intent |
| Task completion | Core path fails | Happy path works | Primary, alternate, and recovery paths work |
| Information clarity | Confusing hierarchy | Generally understandable | Immediate, economical, and predictable |
| Interaction integrity | Controls mislead or fail | Main states work | All states, feedback, and recovery are coherent |
| Visual coherence | Arbitrary styling | Mostly consistent | Distinctive system with disciplined reuse |
| Accessibility | Critical blockers | Basic semantics and contrast | Keyboard, focus, semantics, contrast, motion, and zoom verified |
| Responsive resilience | Breaks at common widths | Major layouts adapt | Content and interaction remain robust across target contexts |
| Content resilience | Real content breaks UI | Typical content fits | Long, short, empty, localized, and error content remain usable |
| Implementation quality | Fragile or duplicated | Maintainable core | Reusable, tokenized, performant, and platform-appropriate |
| Evidence quality | Claims without proof | Partial checks | Reproducible evidence covers acceptance criteria |

## Verdict guidance

- `READY`: No dimension below 3; task completion, accessibility, and evidence quality are 4.
- `READY WITH RISKS`: No dimension below 2; risks are explicit and non-blocking.
- `REVISE`: Any dimension is 1, or several are 2.
- `BLOCKED`: A dimension cannot be assessed because a material decision or dependency is missing.

Treat numerical scoring as a discussion aid, not false precision. Include observations and evidence beside every score.


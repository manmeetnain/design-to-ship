# Worked slice: calmer guest checkout

This deliberately small example demonstrates traceability. It is not presented as user research.

## Direction

**Mode:** `DEFINE + DESIGN`

**Outcome:** Help first-time mobile shoppers understand their total and complete checkout without being forced to create an account.

| Evidence | Status | Claim |
|---|---|---|
| E-01 | CONFIRMED | The hypothetical brief requires guest checkout. |
| E-02 | CONFIRMED | The target viewport includes 375 px mobile screens. |
| E-03 | PROPOSED | Show delivery cost before requesting payment details. |
| E-04 | UNKNOWN | Supported payment methods and regions are not specified. |

| Requirement | Statement | Evidence |
|---|---|---|
| R-01 | A shopper can continue without creating an account. | E-01 |
| R-02 | The primary checkout path remains usable at 375 px. | E-02 |
| R-03 | Cost changes are visible before payment confirmation. | E-03 |

## Experience

Primary journey: Cart → Contact → Delivery → Payment → Review → Confirmation.

Recovery states include invalid address, delivery quote failure, rejected payment, expired session, unavailable item, and accidental navigation. Entered non-sensitive information should survive recoverable failures.

## Decision record

| Decision | Choice | Serves | Alternative | Tradeoff | Verification |
|---|---|---|---|---|---|
| D-01 | Keep account creation optional after confirmation. | R-01 | Require sign-in before payment | Less pre-purchase identity data; lower interruption | Complete checkout in a signed-out session |
| D-02 | Use one responsive column and persistent order-summary access on mobile. | R-02, R-03 | Two compressed columns | More vertical travel; clearer fields and totals | Inspect at 375 px with long address and currency content |

## Acceptance criteria

- R-01: A signed-out shopper reaches confirmation without encountering a mandatory password field.
- R-02: At 375 px, controls do not overlap, clip, or require horizontal scrolling at 200% zoom.
- R-03: Shipping, tax, discounts, and total changes are announced and visible before the final confirmation action.

## Verdict

`READY WITH RISKS` — the interaction direction can advance, but payment methods and operating regions must be confirmed before the Payment step is specified.


# Verification system

Design to Ship separates verification into layers so teams can run fast checks continuously without presenting them as complete proof.

## Layers

| Layer | Method | Proves | Does not prove |
|---|---|---|---|
| Contract | Schema and trace validation | Required structure and connected identifiers | Product usefulness or UI behavior |
| Static | Source inspection | Presence of selected semantic and resilience mechanisms | Runtime behavior or assistive-technology experience |
| Browser | Interaction and viewport automation | Observable browser behavior under tested conditions | Every browser, device, user, or accessibility need |
| Visual | Captured screenshots and optional baselines | Appearance in a named environment | Semantic or functional correctness |
| Manual | Human and assistive-technology evaluation | The specifically observed experience | Untested contexts |

## Evidence record

Every result should include:

- Requirement and decision identifiers
- Result: pass, fail, partial, or not run
- Method and environment
- Artifact or observation
- Limitations
- Timestamp or commit when reproducibility matters

## Browser evidence

The optional browser suite serves the Beacon fixture and checks:

- Critical incident ordering
- Inline acknowledgement and live-region feedback
- Mobile horizontal overflow
- Priority filtering
- Desktop and mobile screenshots

Run it after installing the development dependency:

```bash
python3 -m http.server 4173 --directory examples/beacon/prototype
npm run test:browser
```

CI uploads browser screenshots as build artifacts. These are evidence for the named fixture and environment, not a universal accessibility certification.


# Release process

1. Update `VERSION`, Python package version, npm package version, plugin manifests, README badge, and changelog.
2. Run repository validation, static checks, unit tests, CLI exercises, benchmark, and browser verification.
3. Inspect desktop and mobile evidence for the showcase.
4. Commit and push to `main`.
5. Require the GitHub Actions workflow to pass.
6. Create the matching `vX.Y.Z` GitHub release.
7. Confirm the tag points at the validated commit and the working tree is clean.

Do not publish a release when version surfaces disagree or when a required CI job is failing.


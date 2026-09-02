# Models and agent hosts

Design to Ship avoids model lock-in. It separates three layers that are often incorrectly grouped together.

| Layer | Examples | What matters to this project |
|---|---|---|
| Model family | GPT, Claude, Gemini, open-weight models | Reasoning and multimodal capability |
| Agent host | Codex, ChatGPT, Claude Code, Gemini CLI, Cursor, GitHub Copilot | Skill discovery, tools, files, execution, and permissions |
| Workflow | Design to Ship | Decisions, artifacts, quality gates, and evidence contract |

The same model can produce different results across hosts because the available context and tools differ. Compatibility claims therefore name the host and capability level instead of promising identical output from every model.

## Prompting contract

The canonical workflow is deliberately free of model-version-specific tricks. A compatible host should be able to:

1. Read Markdown instructions and referenced files.
2. Preserve stable evidence, requirement, and decision identifiers.
3. State assumptions and capability limitations.
4. Produce the deliverable contract in order.
5. Avoid claiming unperformed verification.

Better models may reason more deeply or interpret visuals more accurately; they do not change the definition of evidence.

## Tool-aware enhancement

When present, use tools in this order:

1. Product source: PRDs, issue trackers, research, analytics, and content.
2. Design source: Figma or another inspectable design artifact.
3. Implementation source: repository, component library, tokens, and tests.
4. Verification surface: browser, simulator, device, accessibility tooling, and screenshots.

External connectors should remain optional. Missing tools reduce the capability level; they do not authorize fabricated evidence.

## Adding a host

Before marking a new host as supported:

1. Link its official instruction or skill-format documentation.
2. Add the thinnest adapter that points to the canonical skill.
3. Run at least one trigger, one non-trigger, and one incomplete-input case.
4. Record which capability levels were exercised.
5. Mark the integration accurately as native, adapter, or portable fallback.


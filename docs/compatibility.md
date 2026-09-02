# AI compatibility

Design to Ship is model-agnostic. The canonical artifact follows the open Agent Skills shape: a `SKILL.md` with progressive references. Compatibility depends on the **agent host**, not only the underlying model.

## Supported surfaces

| Surface | Integration | Invocation | Status |
|---|---|---|---|
| OpenAI Codex and ChatGPT | `skills/design-to-ship`, `agents/openai.yaml`, `.codex-plugin/plugin.json` | `$design-to-ship` or skill picker | Native package |
| Claude Code | Open Agent Skill | `/design-to-ship` after installation | Native skill |
| Gemini CLI | Open Agent Skill | Install from Git, then request `design-to-ship` | Native skill |
| Cursor | `skills/` plus `.cursor-plugin/plugin.json` | Install plugin or load the repository skill | Native plugin/skill |
| GitHub Copilot | `.github/copilot-instructions.md` and `AGENTS.md` | Ask Copilot to follow Design to Ship | Instruction adapter |
| Other coding agents | `AGENTS.md` plus direct `SKILL.md` path | Ask the agent to read the skill | Portable fallback |

“Native” means the host officially documents skill discovery in this format. “Instruction adapter” means the host receives the core workflow through its documented repository-instruction mechanism; it does not imply every feature of the skill standard is supported.

## Installation

### Codex and ChatGPT

For repository-scoped use, copy or link the skill directory to:

```text
.agents/skills/design-to-ship/
```

For personal use across repositories:

```text
~/.agents/skills/design-to-ship/
```

The repository also includes an OpenAI plugin manifest for distributable packaging.

### Claude Code

Copy the canonical skill directory to either:

```text
.claude/skills/design-to-ship/    # project
~/.claude/skills/design-to-ship/  # personal
```

Then invoke `/design-to-ship` or ask Claude to use it when relevant.

### Gemini CLI

Install the public repository:

```bash
gemini skills install https://github.com/manmeetnain/design-to-ship
```

Use `--scope workspace` for project-only installation. Inspect discovery with `/skills list` and refresh changes with `/skills reload`.

### Cursor

Install the public repository as a plugin or import its skill. The `.cursor-plugin/plugin.json` manifest points to the canonical `skills/` directory. Cursor can also use the root `AGENTS.md` as a simple project rule.

### GitHub Copilot

When this repository is open, Copilot reads `.github/copilot-instructions.md` in supported surfaces. To use the workflow in another repository, copy that adapter and the canonical skill folder, or explicitly attach/link the skill content in the chat surface you use.

## Capability levels

The workflow degrades honestly based on available tools:

| Level | Host capabilities | Valid outcome |
|---|---|---|
| L1 — Reason | Text context | Brief, architecture, system direction, build contract |
| L2 — Inspect | Files, images, or design context | Grounded critique and implementation map |
| L3 — Build | Repository editing and commands | Implemented interface with local checks |
| L4 — Prove | Browser/device control and test tools | Evidence-backed verification report |

An L1 host must not claim L4 verification. Always record which evidence was actually inspected.

## Official references

- [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills)
- [OpenAI: Codex skills](https://developers.openai.com/codex/skills)
- [Anthropic: Extend Claude with skills](https://code.claude.com/docs/en/slash-commands)
- [Google: Managing Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/)
- [Cursor: Plugins reference](https://cursor.com/docs/reference/plugins)
- [GitHub: Custom instructions support](https://docs.github.com/en/copilot/reference/custom-instructions-support)


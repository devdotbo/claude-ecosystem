---
title: UltraThink
project: Claude-UltraThink
type: documentation
tags: [claude_ultrathink, [[Multi-Agent-Orchestration|multi-agent]], single-agent, context-management, cognition-ai]
created: 2025-07-08
source: README.md
---

# UltraThink

A methodology for effective single-agent development in Claude Code, following Cognition.ai's "Don't Build Multi-Agents" research.

## What is UltraThink?

UltraThink is **not** a framework or tool - it's a methodology that helps you use Claude Code more effectively by applying proven single-agent principles.

### The Evolution

UltraThink started as a 1,500+ line Python framework before we realized we were rebuilding what Claude Code already does perfectly. The transformation to a simple methodology embodies the very principles it teaches. [[History|Read the full story]].

## Core Principles

1. **Linear Task Processing** - One task at a time, always
2. **TodoWrite Workflow** - Systematic task planning and execution  
3. **Complete Context** - Let conversation thread maintain full history
4. **No Parallel Work** - Finish current task before starting next

## Quick Start

1. Copy the commands to your Claude Code project:
   ```bash
   cp -r commands .claude/commands
   ```

2. In Claude Code, use:
   - `/ultrathink` - Activate the methodology
   - `/linear` - Check linear processing status

3. Follow the workflow:
   - Use TodoWrite for all tasks
   - Mark ONE task as in_progress
   - Complete it before starting next
   - Update CLAUDE.md with progress

## Why UltraThink?

Based on Cognition.ai research showing [[Multi-Agent-Orchestration|multi-agent]] systems create fragility:
- **No coordination overhead** - Single agent (Claude) handles everything
- **No context fragmentation** - One conversation thread
- **Predictable execution** - Linear processing is debuggable
- **Zero dependencies** - Just markdown files and methodology

## What's Included

```
commands/
├── ultrathink.md    # Main methodology activation
└── linear.md        # Linear processing checker
```

That's it. No Python code, no complex setup, no dependencies.

## Integration with Your Projects

UltraThink works with ANY Claude Code project:
1. Add the commands to `.claude/commands/`
2. Follow the linear processing workflow
3. Use existing Claude Code features (TodoWrite, /memory, etc.)

## License

MIT - Use freely in your projects.
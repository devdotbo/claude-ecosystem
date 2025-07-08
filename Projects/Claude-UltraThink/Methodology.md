---
title: UltraThink Methodology
project: Claude-UltraThink
type: documentation
tags: [claude_ultrathink, [[Multi-Agent-Orchestration|multi-agent]], single-agent, context-management, cognition-ai]
created: 2025-07-08
source: CLAUDE.md
---

# UltraThink Methodology

## Overview

UltraThink is a methodology for effective single-agent development in Claude Code, following Cognition.ai's "Don't Build Multi-Agents" principles.

## Core Principles

- **Single-agent linear processing** - One task at a time, no parallel coordination
- **Complete context preservation** - Maintain full conversation history
- **Actions carry implicit decisions** - Consistent reasoning throughout
- **TodoWrite workflow** - Systematic task planning and execution

## Workflow Guidelines

### Linear Task Processing
1. **Use TodoWrite** for all task planning
2. **One task at a time** - Mark as in_progress before starting
3. **Complete immediately** - Mark completed right after finishing
4. **No parallel work** - Finish current task before starting next

### Context Management
- Let Claude Code's conversation thread maintain context
- Update CLAUDE.md with major milestones and decisions
- Use /memory command to review or update this file
- No complex context compression needed - it happens naturally

## Implementation

### Getting Started
1. Copy UltraThink commands to `.claude/commands/`
2. Use `/ultrathink` to activate the methodology
3. Follow linear processing workflow

### Available Commands
- `/ultrathink` - Activate UltraThink methodology
- `/linear` - Check linear task processing status

### Model Selection
- Use Claude Code's default model settings
- No complex switching needed - Claude handles it
- Users can manually change models if needed for credits

### Best Practices
- Always use TodoWrite for task planning
- Process tasks sequentially, not in parallel
- Update CLAUDE.md with significant progress
- Trust Claude Code's built-in capabilities

## Cognition.ai Alignment

### Research Principles Applied
- **No [[Multi-Agent-Orchestration|multi-agent]] systems** - Claude Code is already a single agent
- **Full context sharing** - Conversation thread maintains complete history
- **Linear processing** - TodoWrite ensures sequential execution
- **Actions carry decisions** - Single agent ensures consistency

### Why UltraThink Works
- **Simplicity** - No complex framework, just methodology
- **Reliability** - Single agent eliminates coordination failures
- **Efficiency** - No overhead from inter-agent communication
- **Clarity** - Linear processing is predictable and debuggable

## Philosophy: Methodology Over Framework

### Why We Chose Simplicity
UltraThink evolved from a 1,500+ line Python framework to just 2 command files. This transformation embodies the single-agent principle: do one thing well.

### The Realization
- Claude Code already IS a single agent
- Building another layer adds complexity, not value
- Methodology teaches better usage of existing tools
- Simplicity enables immediate adoption

## Key Differentiators

### From [[Multi-Agent-Orchestration|Multi-Agent]] Systems
- No agent coordination complexity
- No context fragmentation
- No inter-agent communication overhead
- Single point of control and debugging

### From Complex Frameworks  
- No dependencies or setup required
- No custom code to maintain
- Works with any Claude Code project
- Pure methodology, not technology
- 2 files instead of 1,500+ lines

## Summary

UltraThink transforms how you use Claude Code by applying proven single-agent principles from Cognition.ai research. No framework needed - just smarter workflow.
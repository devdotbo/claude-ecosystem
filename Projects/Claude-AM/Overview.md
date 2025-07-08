---
title: Claude Agentic Maestro (CAM)
project: Claude-AM
type: documentation
tags: [claude_am, multi-agent, context-management]
created: 2025-07-08
source: README.md
---

# Claude Agentic Maestro (CAM)

A self-bootstrapping multi-agent system where AI agents build and coordinate themselves using Claude Code.

## Overview

Claude Agentic Maestro is a recursive system where each agent helps build the next agent. The system features:

- **Self-Building Architecture**: Agents create and improve other agents
- **Multi-Agent Coordination**: Specialized agents for different tasks
- **Session Preservation**: Seamless context management and orchestrator handoffs
- **Real-Time Monitoring**: Agentic test-driven development with immediate feedback
- **Security Integration**: Comprehensive hooks system for safe operation
- **24/7 Operation**: Autonomous continuous development capability

## Agent Ecosystem

### Core Agents

- **Maestro**: Primary orchestrator and task coordinator
- **Seshy**: Session manager handling context preservation and agent handoffs
- **Tasky**: Task manager for planning and coordination
- **Testy**: Agentic test-driven development and monitoring
- **Versio**: Version control and git management
- **Docsy**: Documentation maintenance and generation
- **Speaky**: Voice system with Apple Silicon optimization

### Key Features

- **Model Intelligence**: Automatic Opus/Sonnet model selection based on task complexity
- **Session Continuity**: Cost-free session preservation via local storage
- **Security First**: Pre-commit hooks preventing sensitive data exposure
- **Apple Silicon Optimized**: Native MLX-Audio integration for M-series hardware
- **Open Source**: Professional documentation and MIT licensing

## Quick Start

```bash
# Clone and setup
git clone https://github.com/yourusername/claude-agentic-maestro.git
cd claude-agentic-maestro

# Initialize Claude Code hooks
claude config add hooks

# Start the system
claude
```

## Architecture

The system operates in bootstrap phases:

1. **Foundation**: Basic structure and session management
2. **Coordination**: Core orchestration and task management  
3. **Enhancement**: Advanced capabilities and specialized agents
4. **Autonomous Operation**: Self-improving 24/7 system

## Contributing

This project builds itself - contributions happen through the agent system. See the documentation for integration patterns.

## License

MIT License - see LICENSE file for details.

## Status

This system is actively building itself. Current orchestrator will hand off to Maestro once session management is established.
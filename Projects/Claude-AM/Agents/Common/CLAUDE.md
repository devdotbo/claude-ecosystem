---
title: Common - Shared Agent Utilities
project: Claude-AM
type: agent
tags: [claude_am, agent]
created: 2025-07-08
source: CLAUDE.md
---

# Common - Shared Agent Utilities

## Purpose
Shared utilities and base classes for all Claude Agentic Maestro agents.

## Core Components

### Slash Command Base Class
- Reusable slash command handling framework
- Common command parsing and execution
- Built-in help, status, and history commands
- Command aliasing and parameter validation
- Command history tracking

### Shared Utilities
- Common data structures and enums
- Utility functions for agent development
- Standardized error handling
- Configuration management helpers

## File Structure
```
agents/common/
├── CLAUDE.md              # This documentation
├── __init__.py           # Package initialization
├── slash_command_base.py # Base class for slash commands
└── utils.py              # General utility functions (future)
```

## Usage

### Implementing Slash Commands in an Agent

```python
from agents.common import SlashCommandHandler, SlashCommand, CommandType

class MyAgentHandler(SlashCommandHandler):
    def __init__(self):
        super().__init__("MyAgent")
        
        # Register agent-specific commands
        self.register_command(
            SlashCommand(
                name="mytask",
                description="Execute my task",
                handler=self._handle_mytask,
                command_type=CommandType.OPERATION,
                parameters=[
                    {"name": "param1", "type": "str", "required": True}
                ]
            )
        )
```

### Built-in Commands

All agents inheriting from `SlashCommandHandler` get these commands:

- `/help` - Show available commands
- `/status` - Show agent status (override for custom implementation)
- `/history [limit]` - Show command history

### Command Types

- **SYSTEM** - System-level commands (help, history)
- **OPERATION** - Action commands that perform tasks
- **QUERY** - Information retrieval commands
- **CONFIG** - Configuration management
- **DEBUG** - Debugging and development commands

## Integration Guidelines

### For New Agents
1. Import `SlashCommandHandler` from common
2. Create agent-specific handler class
3. Register custom commands in `__init__`
4. Override `_handle_status_command` for agent-specific status
5. Use `create_cli_interface()` for CLI support

### Command Design Principles
- Keep command names short and intuitive
- Provide helpful descriptions
- Include usage examples for complex commands
- Use aliases for frequently used commands
- Validate parameters before execution

### Error Handling
- All exceptions are caught and returned as error results
- Command history tracks both successful and failed executions
- Detailed error messages help users correct issues

## Quality Standards

### Command Consistency
- Consistent naming conventions across agents
- Standardized parameter formats
- Unified error response structure
- Common status output format

### User Experience
- Clear, helpful error messages
- Command suggestions for typos
- Comprehensive help documentation
- Examples for complex commands

### Performance
- Efficient command parsing
- Limited history memory usage
- Fast command execution
- Minimal overhead
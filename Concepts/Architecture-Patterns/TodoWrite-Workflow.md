---
title: TodoWrite Workflow Pattern
type: concept
category: architecture-patterns
tags: [workflow, task_management, pattern, shared]
related: ["Linear-Task-Processing", "Claude-UltraThink", "Claude-AM"]
created: 2025-07-08
---

# TodoWrite Workflow Pattern

## Definition

A systematic task management pattern using Claude Code's built-in TodoWrite tool for planning, tracking, and executing work.

## Core Components

### Task States
- **pending** - Not yet started
- **in_progress** - Currently working (only ONE at a time)
- **completed** - Finished successfully

### Workflow Rules
1. Plan all tasks upfront
2. One task in_progress maximum
3. Complete immediately after finishing
4. Update list frequently

## Implementation

### In UltraThink
[[Claude-UltraThink]] uses TodoWrite for [[Linear-Task-Processing]]:
```
TodoWrite → One in_progress → Execute → Complete → Next
```

### In CAM
[[Claude-AM]] uses TodoWrite but allows multiple agents to have tasks in_progress, creating coordination complexity.

## Best Practices

### Task Creation
- Break complex work into discrete tasks
- Make tasks specific and actionable
- Include validation in task description
- Order by dependencies

### Task Execution
- Mark in_progress BEFORE starting
- Complete work fully before marking done
- Update immediately after completion
- Never leave tasks in limbo

### Example Workflow
```
1. Create task list with TodoWrite
   - Analyze requirements (pending)
   - Design solution (pending)
   - Implement core logic (pending)
   - Add tests (pending)
   - Document changes (pending)

2. Execute linearly
   - Mark "Analyze requirements" → in_progress
   - [Do analysis work]
   - Mark "Analyze requirements" → completed

3. Continue with next task...
```

## Benefits

- **Visibility** - Clear progress tracking
- **Accountability** - Explicit task ownership
- **Planning** - Upfront task organization
- **History** - Complete execution record

## Anti-Patterns to Avoid

- Multiple in_progress tasks
- Batch status updates
- Skipping task creation
- Incomplete task descriptions
- Forgetting to mark complete

TodoWrite is simple but powerful when used correctly, forming the backbone of both [[Single-Agent-Architecture]] and [[Multi-Agent-Orchestration]] approaches.

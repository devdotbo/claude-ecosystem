---
title: Linear Task Processing
type: concept
category: task-processing
tags: [task_processing, linear, sequential, ultrathink]
related: ["TodoWrite-Workflow", "Parallel-Task-Processing"]
created: 2025-07-08
---

# Linear Task Processing

## Definition

Processing tasks sequentially, one at a time, completing each before starting the next. No parallel execution or coordination required.

## Core Principle

> "One task in progress at a time, always."

## Implementation in UltraThink

[[Claude-UltraThink]] enforces linear processing through:
- [[TodoWrite-Workflow]] with single in_progress task
- Complete task before marking next
- No parallel branches
- Sequential execution guarantee

## Benefits

### Predictability
- Clear execution order
- Easy to trace and debug
- No race conditions
- Consistent state

### Simplicity
- No coordination logic
- No synchronization needs
- Single execution path
- Reduced complexity

### Reliability
- No parallel failures
- Clear error attribution
- Simple recovery
- Consistent results

## Workflow Example

```
1. TodoWrite: Create task list
2. Mark Task 1 → in_progress
3. Execute Task 1
4. Mark Task 1 → completed
5. Mark Task 2 → in_progress
6. Repeat...
```

## Contrast with Parallel

Unlike [[Parallel-Task-Processing]]:
- No coordination overhead
- No complex dependencies
- No synchronization issues
- No partial completion states

## Performance Consideration

While parallel seems faster, coordination overhead often negates benefits:
- Linear: Task1 + Task2 + Task3
- Parallel: Task1 + Coordination + Sync + Error handling

## Best Practices

1. Use TodoWrite for all tasks
2. One in_progress task maximum
3. Complete immediately after execution
4. Update context after each task
5. No speculative execution

Linear processing aligns with [[Cognition-AI-Research]] recommendations for reliable AI systems.

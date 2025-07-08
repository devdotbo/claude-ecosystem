---
title: Don't Build Multi-Agents Principle
type: philosophy
tags: [cognition_ai, research, principle, best_practice]
related: ["Single-Agent-Architecture", "Cognition-AI-Research"]
created: 2025-07-08
---

# Don't Build Multi-Agents Principle

## Origin

From [[Cognition-AI-Research|Cognition.ai's research]], this principle warns against building multi-agent systems with current technology.

## Key Finding

> "Current multi-agent collaboration produces 'fragile systems'. Agents struggle to effectively share and communicate context."

## Why It Matters

### Context Sharing Failures
- Agents cannot effectively share full action traces
- Partial information leads to poor decisions
- Context gets lost in handoffs

### Dispersed Decision-Making
- Multiple agents make conflicting choices
- No unified reasoning process
- Implicit decisions create conflicts

### Coordination Overhead
- Complex messaging systems required
- Synchronization delays execution
- Multiple points of failure

## Evidence from Practice

[[Claude-AM]] demonstrates these problems:
- Distributed session management complexity
- Inter-agent messaging system requirements
- SDK coordination layer overhead

While [[Claude-UltraThink]] avoids them:
- Single conversation thread
- Immediate execution
- Unified decision-making

## Recommendations

1. **Use single agents** for reliability
2. **Maintain complete context** in one place
3. **Process linearly** without coordination
4. **Wait for research advances** before multi-agent

## Future Outlook

The principle acknowledges this may change:
> "Expect improvements in single-agent communication. Anticipate future breakthroughs in agent collaboration."

Until then, single-agent architectures remain superior.

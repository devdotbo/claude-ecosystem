---
title: Cognition.ai Research - Don't Build Multi-Agents
type: research
tags: [research, cognition_ai, multi_agent, evidence]
related: ["Dont-Build-Multi-Agents", "Single-Agent-Architecture", "Claude-UltraThink"]
created: 2025-07-08
source: "https://cognition.ai/blog/dont-build-multi-agents"
---

# Cognition.ai Research: Don't Build Multi-Agents

## Executive Summary

Groundbreaking research showing that current multi-agent systems create "fragile systems" that underperform single agents.

## Key Findings

### 1. Context Sharing Failures

> "Agents struggle to effectively share and communicate context."

**Evidence**: Agents need full action traces, not just messages
**Problem**: Partial information leads to poor decisions
**Solution**: Maintain unified context in single agent

### 2. Dispersed Decision-Making

> "Avoid dispersed decision-making that fragments context."

**Evidence**: Multiple agents make conflicting assumptions
**Problem**: No unified reasoning process
**Solution**: Single decision authority

### 3. Actions Carry Implicit Decisions

> "Actions carry implicit decisions. Prevent conflicting assumptions between agents."

**Evidence**: Each action implies reasoning that others miss
**Problem**: Agents work from different implicit assumptions
**Solution**: One agent maintains consistent reasoning

## Practical Validation

### CAM Proves the Research

Recent [[Claude-AM]] commits validate these warnings:

```
2d21d94 sdk(persistence): implement distributed session management
→ Exactly the "fragmented context" problem

3c28df3 sdk(communication): implement inter-agent messaging system
→ Exactly the "agents struggle to communicate" problem

a579cf8 sdk(config): add SDK integration layer configuration
→ Exactly the "fragile systems" complexity
```

### UltraThink Implements Solutions

[[Claude-UltraThink]] directly implements recommendations:
- Single agent (no fragmentation)
- Complete context (full traces)
- Linear processing (unified decisions)
- No coordination (no communication failures)

## Technical Deep Dive

### Why Context Sharing Fails

1. **Information Loss**
   - Agent A performs action with reasoning R
   - Agent A sends message M to Agent B
   - Message M lacks implicit context of R
   - Agent B makes decision with incomplete information

2. **Synchronization Issues**
   - Agents have different views at time T
   - Coordination messages take time
   - State diverges during coordination
   - Conflicts arise from timing

3. **Handoff Problems**
   - Context packaged for transfer
   - Details lost in serialization
   - Receiving agent reconstructs differently
   - Errors compound over handoffs

## Recommendations

### Current Best Practice
1. Use single agents for reliability
2. Maintain complete context
3. Process tasks linearly
4. Avoid coordination complexity

### Future Evolution

> "Expect improvements in single-agent communication. Anticipate future breakthroughs in agent collaboration."

The research acknowledges this may change but emphasizes current limitations.

## Impact on Architecture Decisions

This research fundamentally challenges the appeal of multi-agent systems:

**Before**: "More agents = more capability"
**After**: "More agents = more fragility"

**Before**: "Parallel processing = faster"
**After**: "Coordination overhead = slower"

**Before**: "Specialization = better results"
**After**: "Fragmentation = worse results"

## Conclusion

Until agent communication significantly improves, single-agent architectures provide superior:
- Reliability
- Performance  
- Maintainability
- Predictability

This research forms the foundation for [[Claude-UltraThink|UltraThink's]] approach and explains why [[Claude-AM|CAM's]] complexity creates problems rather than solving them.

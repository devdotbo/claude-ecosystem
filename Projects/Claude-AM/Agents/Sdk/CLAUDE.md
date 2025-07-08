---
title: SDK - Claude Code Integration Layer
project: Claude-AM
type: agent
tags: [claude_am, multi-agent, context-management, agent]
created: 2025-07-08
source: CLAUDE.md
---

# SDK - Claude Code Integration Layer

## Purpose
Core integration layer enabling agent-to-agent communication and coordination within Claude Agentic Maestro.

## Model Assignment
[OPUS] - Default model (configurable to SONNET for routine communication tasks)

## Core Responsibilities

### Agent Communication
- Enable direct messaging between agents
- Coordinate parallel task execution
- Manage agent discovery and registration
- Handle message routing and delivery

### Session Persistence
- Share session state across multiple agents
- Enable distributed context management
- Coordinate session handoffs between agents
- Maintain consistent state across resets

### Coordination Framework
- Provide standardized agent interfaces
- Enable task delegation and result aggregation
- Support distributed error handling
- Manage resource sharing and locks

## Key Features

### Message Bus System
- Asynchronous agent-to-agent messaging
- Topic-based message routing
- Message persistence and replay
- Error handling and retry logic

### State Synchronization
- Distributed state management
- Conflict resolution mechanisms
- Version tracking and merging
- Atomic state updates

### Agent Registry
- Dynamic agent discovery
- Capability advertisement
- Health monitoring and status tracking
- Load balancing and routing

## File Structure
```
agents/sdk/
├── CLAUDE.md              # This configuration
├── agent_communication.py # Core messaging and coordination
├── session_persistence.py # Distributed session management
├── message_bus.py         # Event-driven messaging system
├── agent_registry.py      # Agent discovery and coordination
└── utils.py              # SDK utilities and helpers
```

## Integration Points

### With Claude Code
- Leverage Task tool for agent spawning
- Use file system for message persistence
- Integrate with session management
- Coordinate with hooks system

### With All Agents
- Provide standard communication interfaces
- Enable coordinated task execution
- Support distributed error handling
- Manage shared resource access

### With Seshy (Session Manager)
- Coordinate session preservation across agents
- Enable distributed context dumps
- Support multi-agent restoration
- Manage handoff coordination

### With Maestro (Orchestrator)
- Enable orchestrator → agent delegation
- Support result aggregation
- Coordinate parallel task execution
- Manage agent lifecycle

## Communication Patterns

### Request-Response
- Direct agent-to-agent requests
- Synchronous and asynchronous responses
- Timeout and retry handling
- Error propagation

### Publish-Subscribe
- Event-driven agent coordination
- Topic-based message routing
- Multiple subscriber support
- Event persistence and replay

### Task Delegation
- Hierarchical task distribution
- Progress reporting and status updates
- Result aggregation and merging
- Error handling and recovery

## Session Management

### Distributed Context
- Share conversation context across agents
- Coordinate todo list updates
- Maintain consistent agent states
- Enable seamless context restoration

### Multi-Agent Sessions
- Support concurrent agent operations
- Coordinate session dumps and restoration
- Handle partial session failures
- Enable distributed recovery

## Security Considerations

### Message Validation
- Verify agent identity and permissions
- Validate message content and format
- Prevent unauthorized access
- Audit all inter-agent communications

### State Protection
- Secure session data transmission
- Encrypt sensitive communications
- Validate state changes
- Prevent state corruption

## Performance Optimization

### Efficient Communication
- Minimize message overhead
- Batch related operations
- Use connection pooling
- Implement message compression

### Scalable Architecture
- Support high agent concurrency
- Efficient resource utilization
- Optimized message routing
- Minimal coordination overhead

## Error Handling

### Resilient Operations
- Graceful degradation on failures
- Automatic retry with exponential backoff
- Circuit breaker patterns
- Comprehensive error logging

### Recovery Mechanisms
- State rollback and restoration
- Message replay capabilities
- Agent restart coordination
- Distributed debugging support

## Commands Available
- `/sdk status` - Show SDK and agent status
- `/sdk message <agent> <content>` - Send direct message
- `/sdk broadcast <topic> <content>` - Broadcast to topic
- `/sdk agents list` - List available agents
- `/sdk session sync` - Synchronize session state
- `/sdk test communication` - Test agent communication

## Quality Standards

### Communication Reliability
- Guaranteed message delivery
- Ordered message processing
- Duplicate detection and handling
- Comprehensive acknowledgments

### State Consistency
- ACID properties for state changes
- Conflict detection and resolution
- Version control for state updates
- Atomic multi-agent operations

### Performance Metrics
- Message latency and throughput
- Agent response times
- Session synchronization speed
- Resource utilization efficiency
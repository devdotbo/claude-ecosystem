---
title: Context Window Strategy Decision Tree
project: Claude-Contexify
type: documentation
tags: [claude_contexify, context-management]
created: 2025-07-08
source: decision-tree.md
---

# Context Window Strategy Decision Tree

## Start Here: What's Your Situation?

This decision tree helps you choose the optimal strategy (or combination) for your specific use case.

```
┌─────────────────────────────────┐
│   What's your primary need?     │
└────────────┬────────────────────┘
             │
    ┌────────┴────────┬─────────────┬──────────────┬───────────────┐
    ▼                 ▼             ▼              ▼               ▼
┌─────────┐    ┌─────────────┐ ┌─────────┐  ┌──────────┐  ┌────────────┐
│ Improve │    │ Handle Large│ │Find Spec│  │Build      │  │Search Many │
│ Accuracy│    │ Documents   │ │Info     │  │Persistent│  │Documents   │
└────┬────┘    └──────┬──────┘ └────┬────┘  │System    │  └─────┬──────┘
     │                │              │       └────┬─────┘        │
     ▼                ▼              ▼            ▼              ▼
Position         Summary        Strategic     Context          RAG
Hacking          Chains         Chunking      Budgeting
```

## Detailed Decision Paths

### 🎯 Path 1: "I want better accuracy from my prompts"

**Start with Position Hacking**

```
Is your content > 2K tokens?
├─ NO → Position Hacking only
│        • Move instructions to start
│        • Key facts to end
│        • Add reminders
│
└─ YES → Position Hacking + Another Strategy
         │
         Is content structured (sections/chapters)?
         ├─ YES → Add Summary Chains
         │        • Summarize by section
         │        • Position hack the summaries
         │
         └─ NO → Add Strategic Chunking
                  • Filter relevant parts
                  • Position hack filtered content
```

### 📚 Path 2: "I have documents too large for context"

**How large is "too large"?**

```
Document Size?
├─ 10-50 pages → Summary Chains
│   │
│   └─ Is it structured content?
│       ├─ YES → Hierarchical summaries
│       └─ NO → Linear chunk summaries
│
├─ 50-200 pages → Strategic Chunking + Summary Chains
│   │
│   └─ Steps:
│       1. Strategic chunk to find relevant sections
│       2. Summary chain on relevant sections only
│       3. Position hack final prompt
│
└─ 200+ pages → RAG (if API) or Manual Chunking
    │
    ├─ Have API access?
    │   └─ YES → Implement RAG system
    │
    └─ NO → Manual Strategic Chunking
            • Break into searchable sections
            • Manual relevance filtering
            • Summary chains on results
```

### 🔍 Path 3: "I need specific information from documents"

**What type of information?**

```
Information Type?
├─ Known location → Direct Extraction
│   └─ Jump to specific section
│
├─ Topic-based → Strategic Chunking
│   │
│   └─ Single document?
│       ├─ YES → Basic chunking + filter
│       └─ NO → Chunking across all docs
│
├─ Entity/keyword → Keyword Search + Chunking
│   └─ Grep/search first, then chunk
│
└─ Conceptual → RAG or Summary Chains
    │
    ├─ Need all mentions?
    │   └─ YES → RAG with semantic search
    │
    └─ Need overview?
        └─ YES → Summary chains by topic
```

### 🤖 Path 4: "I'm building a persistent system"

**What's your environment?**

```
API Access Available?
├─ YES → Full Implementation Options
│   │
│   └─ Context Budgeting + Your Choice:
│       ├─ Q&A System → RAG + Budgeting
│       ├─ Chatbot → Budgeting + Position Hacking
│       ├─ Analysis Tool → All strategies orchestrated
│       └─ Document Processor → Summary Chains + Budgeting
│
└─ NO → Chatbot/Manual Implementation
    │
    └─ Viable Strategies:
        ├─ Position Hacking (always)
        ├─ Manual Summary Chains
        ├─ Manual Strategic Chunking
        └─ Basic context awareness
```

### 🗂️ Path 5: "I need to search many documents"

**How many documents and what kind?**

```
Document Collection Size?
├─ < 10 documents → Manual Methods
│   └─ Strategic Chunking + Summary
│
├─ 10-100 documents → Semi-Automated
│   │
│   ├─ Similar structure?
│   │   └─ YES → Template-based extraction
│   │
│   └─ NO → Category-based approach
│
└─ 100+ documents → RAG Required
    │
    ├─ Build vector database
    ├─ Semantic search
    └─ Retrieved context management
```

## Strategy Combination Matrix

### When to Combine Strategies

| Primary Strategy | Best Combined With | When to Combine |
|-----------------|-------------------|-----------------|
| Position Hacking | Any strategy | Always - it's free! |
| Summary Chains | Position Hacking | Always |
| Summary Chains | Strategic Chunking | Documents > 50 pages |
| Strategic Chunking | Position Hacking | Always |
| Strategic Chunking | Summary Chains | Very large filtered results |
| Context Budgeting | All strategies | Building systems |
| RAG | Context Budgeting | Production systems |
| RAG | Position Hacking | Query optimization |

## Quick Decision Matrix

### By Document Size
- **< 8K tokens**: Position Hacking only
- **8K - 32K tokens**: Position Hacking + Summary Chains
- **32K - 128K tokens**: Strategic Chunking + Summary Chains
- **> 128K tokens**: RAG (or manual chunking)

### By Use Case
- **One-time analysis**: Summary Chains
- **Repeated queries**: RAG
- **Specific extraction**: Strategic Chunking
- **System building**: Context Budgeting
- **Quick improvement**: Position Hacking

### By Access Level
- **API Access**: All strategies available
- **Chatbot Only**: Position, Summary, Strategic
- **Hybrid Access**: Optimize per platform

## Decision Flowchart Tool

### Step 1: Answer These Questions

1. **Document Size**: 
   - [ ] Fits in context (< 8K tokens)
   - [ ] Medium (8K - 100K tokens)
   - [ ] Large (> 100K tokens)

2. **Query Type**:
   - [ ] General analysis
   - [ ] Specific information
   - [ ] Comparison/synthesis
   - [ ] Repeated queries

3. **Access Level**:
   - [ ] Full API access
   - [ ] Chatbot only
   - [ ] Both available

4. **Performance Needs**:
   - [ ] Real-time response
   - [ ] Batch processing OK
   - [ ] Cost sensitive

### Step 2: Calculate Your Strategy

Based on your answers:

#### Scoring
- Document Size: Large = 3, Medium = 2, Small = 1
- Query Type: Repeated = RAG, Specific = Chunking, General = Summary
- Access: API = All options, Chat = Limited options
- Performance: Real-time = Position/Budget, Batch = Any

### Step 3: Your Recommended Approach

#### If Total Score ≥ 7: Complex Approach Needed
```
Primary: RAG (if API) or Strategic Chunking
Secondary: Summary Chains for large results
Always: Position Hacking
Consider: Context Budgeting for systems
```

#### If Total Score 4-6: Moderate Approach
```
Primary: Summary Chains
Secondary: Strategic Chunking for filtering
Always: Position Hacking
Optional: Basic context budgeting
```

#### If Total Score ≤ 3: Simple Approach
```
Primary: Position Hacking
Optional: Basic summary if needed
Focus: Quick optimizations
```

## Common Scenarios Quick Guide

### Scenario 1: "Analyzing earnings reports"
- **Strategy**: Summary Chains + Position Hacking
- **Why**: Structured documents, need comprehensive view
- **Implementation**: Summarize by section, combine, position optimize

### Scenario 2: "Finding legal clauses"
- **Strategy**: Strategic Chunking + Position Hacking
- **Why**: Specific information needed
- **Implementation**: Filter for legal terms, process matches

### Scenario 3: "Customer support bot"
- **Strategy**: Context Budgeting + RAG + Position
- **Why**: Persistent system, repeated queries
- **Implementation**: Budget for conversation, RAG for knowledge

### Scenario 4: "Research across papers"
- **Strategy**: RAG + Summary Chains
- **Why**: Many documents, conceptual queries
- **Implementation**: Index papers, retrieve relevant, summarize

### Scenario 5: "Quick document summary"
- **Strategy**: Position Hacking + Basic Summary
- **Why**: One-time need, simple requirement
- **Implementation**: Position optimize, maybe split if huge

## Strategy Complexity Levels

### 🟢 Beginner (Start Here)
1. **Position Hacking**: No code, immediate results
2. **Basic Summary**: Manual splitting, simple prompts

### 🟡 Intermediate
1. **Summary Chains**: Some automation helpful
2. **Strategic Chunking**: Requires planning
3. **Basic Context Budgeting**: Need token awareness

### 🔴 Advanced
1. **RAG Implementation**: Significant setup
2. **Full Context Budgeting**: Complex tracking
3. **Multi-Strategy Orchestration**: Coordination required

## Final Recommendations

### If You're Unsure:
1. **Start with Position Hacking** - It's free and always helps
2. **Add Summary Chains** - If document is too large
3. **Try Strategic Chunking** - If you need specific info
4. **Implement others as needed** - Based on results

### For Production Systems:
1. **Always use Context Budgeting** - Control is critical
2. **Implement RAG for scale** - Handles growth
3. **Position Hack everything** - Free optimization
4. **Monitor and adjust** - Strategies evolve with usage

### Remember:
- Strategies stack - use multiple for best results
- Start simple, add complexity as needed
- Test different approaches with your specific content
- The "best" strategy depends on your exact needs

## Next Steps

1. Identify your primary need above
2. Follow the decision path
3. Read the specific [[strategy guide]]
4. Start with [[Quick Start|quick implementation]]
5. Iterate based on results
# Claude Ecosystem Knowledge Graph

An Obsidian knowledge graph exploring the philosophical tensions and complementary approaches between three Claude-related projects:

- **[Claude-UltraThink](Projects/Claude-UltraThink/)** - Single-agent methodology based on Cognition.ai research
  - 🔗 [GitHub Repository](https://github.com/devdotbo/claude-ultrathink)
- **[Claude-AM](Projects/Claude-AM/)** - Multi-agent orchestration system
  - 🔗 [GitHub Repository](https://github.com/devdotbo/claude-am)
- **[Claude-Contexify](Projects/Claude-Contexify/)** - Context window optimization strategies
  - 🔗 [GitHub Repository](https://github.com/devdotbo/claude-contexify)

## Overview

This knowledge graph visualizes the relationships, tensions, and complementary aspects of different approaches to AI development with Claude. It's built using Obsidian's linked note system and follows UltraThink's linear processing methodology.

## 📊 Current Status

- ✅ Knowledge graph structure complete with 40+ notes
- ✅ Core documentation extracted from all three projects
- ✅ Automation scripts created and ready for testing
- ⚠️ Scripts need manual execution (see [TESTING_STATUS.md](TESTING_STATUS.md))
- 📋 Full project details in [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

## Key Philosophical Tensions

### 🥊 UltraThink vs CAM
- **Single-agent** vs **Multi-agent** architecture
- **2 files** vs **4,250+ lines** of code
- **Methodology** vs **Framework**
- Based on opposing interpretations of AI development best practices

### 🧩 Context Management Approaches
- **Unified Context** (UltraThink) - Everything in one conversation thread
- **Distributed Context** (CAM) - Split across multiple agents
- **Optimized Context** (Contexify) - Working within real limitations

## Structure

```
📁 Projects/           # Individual project documentation
📁 Concepts/           # Core concepts and patterns
📁 Philosophies/       # Underlying philosophical approaches
📁 Research/           # Research papers and evidence
📁 Comparisons/        # Head-to-head comparisons
📁 _templates/         # Obsidian note templates
📄 scripts/            # Automation and sync scripts
```

## Quick Start

1. **Open in Obsidian**: 
   - Download [Obsidian](https://obsidian.md)
   - Open this folder as a vault
   - Enable Graph View to see connections

2. **Explore Key Concepts**:
   - Start with [Project Overviews](Projects/)
   - Explore [Philosophical Differences](Philosophies/)
   - Dive into [Technical Comparisons](Comparisons/)

3. **Follow Links**: Click [[wiki-style]] links to navigate between concepts

## Automation Scripts

- ✅ `extract_docs.py` - Extract documentation from source projects
- ✅ `create_core_notes.py` - Generate concept and comparison notes
- ✅ `generate_links.py` - Analyze links and suggest improvements
- 🚧 `sync_knowledge.py` - Sync updates from source repositories (planned)

### Testing Scripts
- `test_scripts.py` - Comprehensive test harness
- `simple_test.py` - Quick validation check
- See [TESTING_STATUS.md](TESTING_STATUS.md) for testing instructions

## Maintenance

This knowledge graph follows UltraThink's linear processing methodology:

1. **One update at a time** - No parallel modifications
2. **Complete context** - Full commit messages with reasoning
3. **Linear workflow** - Plan → Execute → Validate → Commit

## Contributing

Following UltraThink principles:
- One maintainer works at a time
- Use TodoWrite workflow for planning changes
- Keep updates atomic and well-documented

## Key Insights

### From UltraThink
- Simplicity beats complexity
- Methodology over framework
- Single-agent reliability

### From CAM  
- Multi-agent coordination challenges
- Context fragmentation issues
- Complexity growth over time

### From Contexify
- Reality vs marketing (10% rule)
- Practical optimization strategies
- Working within limitations

## Research Foundation

Based on [Cognition.ai's "Don't Build Multi-Agents"](Research/Cognition-AI-Research.md) research, which found that current multi-agent systems create "fragile systems" with context fragmentation and coordination failures.

## Visualization

Best viewed in Obsidian with:
- Graph View for relationship visualization
- Canvas for architectural comparisons
- Dataview for dynamic queries

## Repository Organization

This ecosystem is organized into multiple repositories:

1. **claude-ecosystem** (this repository) - Central documentation and knowledge graph
2. **claude-ultrathink** - Simple single-agent implementation
3. **claude-am** - Multi-agent orchestration framework
4. **claude-contexify** - Context window optimization tools

Each repository is independent but documented here for comparison and analysis.

## License

Documentation and scripts are MIT licensed. Source project licenses apply to their respective content.

---

*"The best solutions often involve removing code, not adding it."* - UltraThink Philosophy
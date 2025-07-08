# Git Integration & UltraThink Planning for Obsidian Knowledge Graph

## Overview

This document outlines how to integrate git version control with the Obsidian knowledge graph and apply UltraThink principles to maintain and evolve it.

## Git Repository Structure

```
claude-ecosystem-knowledge-graph/
├── .git/                    # Git repository
├── .gitignore              # Ignore Obsidian workspace files
├── .obsidian/              # Obsidian configuration
│   ├── workspace.json      # (gitignored)
│   ├── graph.json         # Graph view settings
│   └── plugins/           # Community plugins
├── Projects/              # Project documentation
├── Concepts/              # Core concepts
├── Philosophies/          # Philosophical foundations
├── Research/              # Research papers and evidence
├── Comparisons/           # Comparative analyses
├── _templates/            # Note templates
├── scripts/               # Automation scripts
│   ├── extract_docs.py
│   ├── create_core_notes.py
│   ├── sync_knowledge.py
│   └── generate_links.py
└── README.md              # Repository documentation
```

## Git Configuration

### .gitignore
```gitignore
# Obsidian workspace files
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
.obsidian/hotkeys.json

# OS files
.DS_Store
Thumbs.db

# Python
__pycache__/
*.py[cod]
*$py.class
.venv/
venv/

# Temporary files
*.tmp
*.bak
~*
```

### Initial Setup
```bash
# Initialize repository
cd /Users/bioharz/git/2025_2/claude-ecosystem-knowledge-graph
git init

# Create .gitignore
cat > .gitignore << 'EOF'
# Obsidian workspace files
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
.obsidian/hotkeys.json

# OS files
.DS_Store
Thumbs.db

# Python
__pycache__/
*.py[cod]
.venv/
EOF

# Initial commit
git add .
git commit -m "Initial knowledge graph structure with UltraThink, CAM, and Contexify documentation"
```

## UltraThink Workflow for Knowledge Graph Maintenance

### 1. Linear Update Process

Following UltraThink's [[Linear-Task-Processing]] principle:

```markdown
## Update Workflow (using TodoWrite)

1. **Identify Changes** (pending)
   - Check source repositories for updates
   - Review new research papers
   - Gather user feedback

2. **Plan Updates** (pending)
   - List specific files to update
   - Identify new concepts to add
   - Plan relationship changes

3. **Execute Updates** (pending)
   - Run extraction scripts
   - Update individual notes
   - Add new connections

4. **Validate Changes** (pending)
   - Check all links work
   - Verify frontmatter
   - Test Dataview queries

5. **Commit Changes** (pending)
   - Review git diff
   - Write descriptive commit message
   - Push to remote
```

### 2. Single-Agent Approach

One person maintains the knowledge graph at a time:
- No merge conflicts from parallel edits
- Consistent voice and structure
- Clear ownership of changes

### 3. Context Preservation

Each commit should include:
- What changed and why
- Which source projects were updated
- New insights or connections discovered

## Automated Sync Script

```python
#!/usr/bin/env python3
"""
sync_knowledge.py - UltraThink-based knowledge graph synchronization
"""

import subprocess
from pathlib import Path
from datetime import datetime

class KnowledgeGraphSync:
    def __init__(self, kg_path: str, source_path: str):
        self.kg_path = Path(kg_path)
        self.source_path = Path(source_path)
        
    def check_updates(self):
        """Check source repositories for updates."""
        updates = []
        for project in ['claude-ultrathink', 'claude-am', 'claude-contexify']:
            project_path = self.source_path / project
            if project_path.exists():
                # Get last commit info
                result = subprocess.run(
                    ['git', 'log', '-1', '--format=%H %s'],
                    cwd=project_path,
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    updates.append(f"{project}: {result.stdout.strip()}")
        return updates
        
    def sync_project(self, project: str):
        """Sync a single project following UltraThink linear processing."""
        print(f"Syncing {project}...")
        
        # 1. Extract documentation
        subprocess.run(['python', 'extract_docs.py', '--project', project])
        
        # 2. Update core notes if needed
        subprocess.run(['python', 'create_core_notes.py', '--project', project])
        
        # 3. Generate new links
        subprocess.run(['python', 'generate_links.py', '--project', project])
        
    def commit_changes(self, message: str):
        """Commit changes with descriptive message."""
        subprocess.run(['git', 'add', '.'], cwd=self.kg_path)
        subprocess.run(['git', 'commit', '-m', message], cwd=self.kg_path)
        
    def run(self):
        """Run complete sync following UltraThink methodology."""
        print("🔄 Starting UltraThink knowledge graph sync...")
        
        # Linear processing - one task at a time
        updates = self.check_updates()
        if updates:
            print("📋 Found updates:")
            for update in updates:
                print(f"  - {update}")
                
            # Process each project sequentially
            for project in ['claude-ultrathink', 'claude-am', 'claude-contexify']:
                self.sync_project(project)
                
            # Commit all changes together
            commit_msg = f"Update knowledge graph - {datetime.now().strftime('%Y-%m-%d')}\n\n"
            commit_msg += "\n".join(updates)
            self.commit_changes(commit_msg)
            
            print("✅ Sync complete!")
        else:
            print("✨ No updates needed")
```

## Version Control Best Practices

### 1. Atomic Commits
- Each commit should represent one logical change
- Don't mix unrelated updates
- Use descriptive commit messages

### 2. Commit Message Format
```
<type>: <description>

[optional body]

Updates: <project names>
Concepts: <new/modified concepts>
```

Example:
```
feat: Add context fragmentation analysis

Added detailed comparison of context fragmentation between
UltraThink and CAM, with real-world evidence from recent commits.

Updates: claude-am, claude-ultrathink
Concepts: Context-Fragmentation, Distributed-Context
```

### 3. Branching Strategy

Following UltraThink's linear processing:
- Work directly on main branch
- No complex branching needed
- If experimenting, use single feature branch

## Integration with Obsidian

### 1. Obsidian Git Plugin
- Install community plugin for git integration
- Configure for automatic pulls on startup
- Manual commits for intentional updates

### 2. Mobile Sync
- Use Obsidian Sync for mobile devices
- Git remains source of truth
- Resolve conflicts on desktop

## Maintenance Schedule

### Daily
- Check for source project updates
- Quick fixes and corrections

### Weekly  
- Run full sync script
- Update relationships and links
- Add new insights from usage

### Monthly
- Review overall structure
- Refactor if needed
- Update documentation

## UltraThink Principles Applied

1. **Linear Processing**: Update one project at a time
2. **Complete Context**: Full commit messages with reasoning
3. **Single Agent**: One maintainer at a time
4. **TodoWrite Workflow**: Plan updates before executing

## Future Enhancements

### Planned Features
1. Automatic update detection via GitHub webhooks
2. AI-assisted relationship discovery
3. Conflict resolution helpers
4. Graph visualization exports

### Following UltraThink Evolution
As UltraThink methodology evolves, so should this workflow:
- Keep it simple
- Avoid over-engineering
- Focus on value, not complexity
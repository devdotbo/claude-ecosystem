#!/usr/bin/env python3
"""
Extract and convert documentation from Claude projects into Obsidian knowledge graph format.
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

class ObsidianDocExtractor:
    def __init__(self, source_base: str, target_base: str):
        self.source_base = Path(source_base)
        self.target_base = Path(target_base)
        self.project_mappings = {
            'claude-ultrathink': 'Claude-UltraThink',
            'claude-am': 'Claude-AM',
            'claude-contexify': 'Claude-Contexify'
        }
        
    def extract_ultrathink(self):
        """Extract and convert UltraThink documentation."""
        print("📚 Extracting Claude-UltraThink documentation...")
        
        source_dir = self.source_base / 'claude-ultrathink'
        target_dir = self.target_base / 'Projects' / 'Claude-UltraThink'
        
        # Document mappings for UltraThink
        file_mappings = {
            'README.md': 'Overview.md',
            'CLAUDE.md': 'Methodology.md',
            'ARCHITECTURE.md': 'Architecture.md',
            'HISTORY.md': 'Evolution-Story.md',
            'COGNITION_AI_ALIGNMENT.md': ('../../Research/Cognition-AI-Research.md', True),
            'VS_CAM.md': ('../../Comparisons/UltraThink-vs-CAM.md', True),
        }
        
        # Process main documentation files
        for source_file, target_info in file_mappings.items():
            if isinstance(target_info, tuple):
                target_file, is_shared = target_info
            else:
                target_file, is_shared = target_info, False
                
            source_path = source_dir / source_file
            target_path = self.target_base / (target_dir / target_file if not is_shared else Path(target_file).parent / Path(target_file).name)
            
            if source_path.exists():
                self._process_file(source_path, target_path, 'Claude-UltraThink')
                
        # Process command files
        commands_dir = source_dir / 'commands'
        if commands_dir.exists():
            target_commands = target_dir / 'Commands'
            target_commands.mkdir(parents=True, exist_ok=True)
            
            for cmd_file in commands_dir.glob('*.md'):
                target_path = target_commands / cmd_file.name
                self._process_file(cmd_file, target_path, 'Claude-UltraThink', file_type='command')
                
    def extract_cam(self):
        """Extract and convert Claude-AM documentation."""
        print("🤖 Extracting Claude-AM documentation...")
        
        source_dir = self.source_base / 'claude-am'
        target_dir = self.target_base / 'Projects' / 'Claude-AM'
        
        # Process main documentation
        main_files = ['README.md', 'LICENSE']
        for file_name in main_files:
            source_path = source_dir / file_name
            if source_path.exists():
                target_name = 'Overview.md' if file_name == 'README.md' else file_name
                target_path = target_dir / target_name
                self._process_file(source_path, target_path, 'Claude-AM')
                
        # Process agent documentation
        agents_dir = source_dir / 'agents'
        if agents_dir.exists():
            for agent_dir in agents_dir.iterdir():
                if agent_dir.is_dir() and agent_dir.name != '__pycache__':
                    self._process_agent_docs(agent_dir, target_dir / 'Agents' / agent_dir.name.title())
                    
    def extract_contexify(self):
        """Extract and convert Claude-Contexify documentation."""
        print("🧩 Extracting Claude-Contexify documentation...")
        
        source_dir = self.source_base / 'claude-contexify' / 'context-window-solutions'
        target_dir = self.target_base / 'Projects' / 'Claude-Contexify'
        
        if not source_dir.exists():
            print(f"⚠️  Warning: {source_dir} not found")
            return
            
        # Process the directory structure
        for item in source_dir.iterdir():
            if item.is_dir() and item.name.startswith(('0', '1')):
                # Process numbered directories
                clean_name = re.sub(r'^\d+-', '', item.name).replace('-', ' ').title()
                target_subdir = target_dir / clean_name.replace(' ', '-')
                target_subdir.mkdir(parents=True, exist_ok=True)
                
                for md_file in item.glob('*.md'):
                    target_path = target_subdir / md_file.name
                    self._process_file(md_file, target_path, 'Claude-Contexify')
                    
            elif item.suffix == '.md':
                # Process root level markdown files
                target_path = target_dir / item.name
                self._process_file(item, target_path, 'Claude-Contexify')
                
    def _process_file(self, source_path: Path, target_path: Path, project: str, file_type: str = 'documentation'):
        """Process a single file with frontmatter and link conversion."""
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Convert links and add frontmatter
        processed_content = self._add_frontmatter(content, source_path, project, file_type)
        processed_content = self._convert_links(processed_content, project)
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)
            
        print(f"  ✅ {source_path.name} → {target_path.relative_to(self.target_base)}")
        
    def _process_agent_docs(self, agent_dir: Path, target_dir: Path):
        """Process agent-specific documentation."""
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Look for CLAUDE.md or README.md in agent directory
        for doc_name in ['CLAUDE.md', 'README.md', '__init__.py']:
            doc_path = agent_dir / doc_name
            if doc_path.exists():
                if doc_path.suffix == '.py':
                    # Extract docstrings from Python files
                    content = self._extract_docstrings(doc_path)
                    if content:
                        target_path = target_dir / f"{agent_dir.name}-overview.md"
                        processed_content = self._add_frontmatter(content, doc_path, 'Claude-AM', 'agent')
                        with open(target_path, 'w', encoding='utf-8') as f:
                            f.write(processed_content)
                        print(f"  ✅ Extracted docs from {doc_path.name}")
                else:
                    target_name = 'Overview.md' if doc_name == 'README.md' else doc_name
                    target_path = target_dir / target_name
                    self._process_file(doc_path, target_path, 'Claude-AM', 'agent')
                    
    def _extract_docstrings(self, py_file: Path) -> str:
        """Extract docstrings from Python files."""
        with open(py_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Simple docstring extraction (could be enhanced)
        docstring_pattern = r'"""(.*?)"""'
        docstrings = re.findall(docstring_pattern, content, re.DOTALL)
        
        if docstrings:
            return f"# {py_file.stem.replace('_', ' ').title()}\n\n" + "\n\n".join(docstrings)
        return ""
        
    def _add_frontmatter(self, content: str, source_path: Path, project: str, file_type: str = 'documentation') -> str:
        """Add YAML frontmatter to content."""
        # Skip if already has frontmatter
        if content.startswith('---\n'):
            return content
            
        # Extract title from content or filename
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else source_path.stem.replace('-', ' ').title()
        
        # Determine tags based on content
        tags = [project.lower().replace('-', '_')]
        if 'multi-agent' in content.lower():
            tags.append('multi-agent')
        if 'single-agent' in content.lower():
            tags.append('single-agent')
        if 'context' in content.lower():
            tags.append('context-management')
        if 'cognition.ai' in content.lower():
            tags.append('cognition-ai')
        if file_type != 'documentation':
            tags.append(file_type)
            
        # Build frontmatter
        frontmatter = f"""---
title: {title}
project: {project}
type: {file_type}
tags: [{', '.join(tags)}]
created: {datetime.now().strftime('%Y-%m-%d')}
source: {source_path.name}
---

"""
        return frontmatter + content
        
    def _convert_links(self, content: str, project: str) -> str:
        """Convert internal links to Obsidian wiki links."""
        # Convert markdown links to wiki links
        def replace_link(match):
            text = match.group(1)
            link = match.group(2)
            
            # Skip external links
            if link.startswith(('http://', 'https://', 'ftp://')):
                return match.group(0)
                
            # Convert relative links to wiki links
            if link.endswith('.md'):
                link_name = Path(link).stem.replace('-', ' ').title()
                return f"[[{link_name}|{text}]]"
            else:
                return f"[[{text}]]"
                
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, content)
        
        # Add cross-project references where appropriate
        if project == 'Claude-UltraThink':
            # Add links to CAM and Contexify concepts
            content = re.sub(r'\b(multi-agent)\b', r'[[Multi-Agent-Orchestration|\1]]', content, flags=re.IGNORECASE)
            content = re.sub(r'\b(CAM)\b', r'[[Claude-AM|\1]]', content)
            content = re.sub(r'\b(context window)\b', r'[[Context-Window-Reality|\1]]', content, flags=re.IGNORECASE)
            
        return content
        
    def create_overview_notes(self):
        """Create high-level overview notes for each project."""
        print("📝 Creating project overview notes...")
        
        # UltraThink overview
        ultrathink_overview = """---
title: Claude-UltraThink Project Overview
project: Claude-UltraThink
type: overview
tags: [claude_ultrathink, single-agent, methodology, overview]
created: {date}
---

# Claude-UltraThink Project Overview

## What is UltraThink?

UltraThink is a **methodology** (not a framework) for effective single-agent development in Claude Code, based on [[Cognition-AI-Research|Cognition.ai's "Don't Build Multi-Agents"]] research.

## Core Philosophy

- **[[Single-Agent-Architecture]]** - One agent handles everything
- **[[Linear-Task-Processing]]** - Sequential execution, no parallelism
- **[[TodoWrite-Workflow]]** - Systematic task planning
- **[[Complete-Context-Preservation]]** - Full conversation history

## Key Differentiator

Unlike [[Claude-AM]] which uses 7+ specialized agents, UltraThink proves that a single agent with proper methodology outperforms complex multi-agent systems.

## Implementation

- **2 command files** vs CAM's 4,250+ lines
- **Zero dependencies** vs complex coordination systems
- **Immediate execution** vs coordination delays

## Research Foundation

Based on [[Cognition-AI-Research]] showing that current multi-agent systems create "fragile systems" with context fragmentation and coordination failures.

## Related Concepts

- Opposed to: [[Multi-Agent-Orchestration]]
- Complements: [[Context-Window-Reality]] strategies from [[Claude-Contexify]]
- Validates: [[Dont-Build-Multi-Agents]] principle
""".format(date=datetime.now().strftime('%Y-%m-%d'))

        # Write overview files
        overview_path = self.target_base / 'Projects' / 'Claude-UltraThink' / 'Project-Overview.md'
        overview_path.parent.mkdir(parents=True, exist_ok=True)
        with open(overview_path, 'w') as f:
            f.write(ultrathink_overview)
        print(f"  ✅ Created UltraThink project overview")
        
    def run(self):
        """Run the complete extraction process."""
        print("🚀 Starting documentation extraction...")
        self.extract_ultrathink()
        self.extract_cam()
        self.extract_contexify()
        self.create_overview_notes()
        print("✨ Documentation extraction complete!")


if __name__ == "__main__":
    source_base = "/Users/bioharz/git/2025_2"
    target_base = "/Users/bioharz/git/2025_2/knowledge-graphs/claude-ecosystem"
    
    extractor = ObsidianDocExtractor(source_base, target_base)
    extractor.run()
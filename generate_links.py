#!/usr/bin/env python3
"""
Generate and analyze links between notes in the Claude Ecosystem Knowledge Graph.

This script follows UltraThink's linear processing methodology:
1. Scan all markdown files
2. Extract existing links
3. Identify potential new connections
4. Generate bidirectional links
5. Find orphaned notes
6. Create comprehensive report
"""

import os
import re
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
from typing import Dict, List, Set, Tuple

class ObsidianLinkGenerator:
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.notes = {}  # filename -> content
        self.links = defaultdict(set)  # note -> set of linked notes
        self.backlinks = defaultdict(set)  # note -> set of notes linking to it
        self.potential_links = defaultdict(list)  # note -> list of (target, reason)
        self.orphaned_notes = set()
        
        # Key concepts to track for auto-linking
        self.key_concepts = {
            # Architecture patterns
            'single-agent': ['Single-Agent-Architecture', 'UltraThink', 'linear', 'unified'],
            'multi-agent': ['Multi-Agent-Orchestration', 'CAM', 'Claude-AM', 'distributed'],
            
            # Context management
            'unified-context': ['Unified-Context', 'single thread', 'complete history'],
            'distributed-context': ['Distributed-Context', 'fragmented', 'split context'],
            'context-window': ['Context-Window-Reality', 'Contexify', 'limitations'],
            
            # Task processing
            'linear-processing': ['Linear-Task-Processing', 'sequential', 'one at a time'],
            'parallel-processing': ['parallel', 'concurrent', 'simultaneous'],
            
            # Core projects
            'ultrathink': ['Claude-UltraThink', 'UltraThink', 'single agent methodology'],
            'cam': ['Claude-AM', 'CAM', 'Agentic Maestro', 'multi-agent system'],
            'contexify': ['Claude-Contexify', 'Contexify', 'context optimization'],
            
            # Philosophy
            'cognition-ai': ['Cognition-AI-Research', 'Cognition.ai', "Don't Build Multi-Agents"],
            'methodology': ['Methodology-Over-Framework', 'simplicity', 'enhancement'],
            
            # Specific agents (CAM)
            'maestro': ['Maestro-Agent', 'orchestrator', 'coordinator'],
            'seshy': ['Seshy-Agent', 'session management', 'handoffs'],
            'tasky': ['Tasky-Agent', 'task management', 'delegation'],
            'testy': ['Testy-Agent', 'testing', 'quality assurance'],
            'versio': ['Versio-Agent', 'version control', 'commits'],
            'docsy': ['Docsy-Agent', 'documentation', 'generation'],
        }
        
    def scan_vault(self):
        """Scan the vault for all markdown files."""
        print("📂 Scanning vault for markdown files...")
        
        for md_file in self.vault_path.rglob('*.md'):
            # Skip hidden directories
            if any(part.startswith('.') for part in md_file.parts):
                continue
                
            relative_path = md_file.relative_to(self.vault_path)
            note_name = md_file.stem
            
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            self.notes[note_name] = {
                'path': relative_path,
                'content': content,
                'file': md_file
            }
            
        print(f"  ✅ Found {len(self.notes)} markdown files")
        
    def extract_existing_links(self):
        """Extract all existing wiki links from notes."""
        print("🔗 Extracting existing links...")
        
        wiki_link_pattern = r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'
        
        for note_name, note_data in self.notes.items():
            content = note_data['content']
            
            # Find all wiki links
            for match in re.finditer(wiki_link_pattern, content):
                linked_note = match.group(1)
                self.links[note_name].add(linked_note)
                self.backlinks[linked_note].add(note_name)
                
        # Calculate link statistics
        total_links = sum(len(links) for links in self.links.values())
        print(f"  ✅ Found {total_links} links across {len(self.links)} notes")
        
    def identify_orphaned_notes(self):
        """Find notes with no incoming or outgoing links."""
        print("🔍 Identifying orphaned notes...")
        
        for note_name in self.notes:
            if note_name not in self.links and note_name not in self.backlinks:
                # Exclude some system files
                if note_name not in ['README', 'git_integration_plan']:
                    self.orphaned_notes.add(note_name)
                    
        print(f"  ⚠️  Found {len(self.orphaned_notes)} orphaned notes")
        
    def suggest_new_links(self):
        """Suggest potential new links based on content analysis."""
        print("💡 Analyzing content for potential links...")
        
        for note_name, note_data in self.notes.items():
            content = note_data['content'].lower()
            
            # Check for key concepts
            for concept, keywords in self.key_concepts.items():
                for keyword in keywords:
                    if keyword.lower() in content:
                        # Look for notes that might be related
                        for target_note in self.notes:
                            if target_note != note_name and target_note not in self.links[note_name]:
                                target_content = self.notes[target_note]['content'].lower()
                                
                                # Check if target is about this concept
                                if any(kw.lower() in target_content for kw in keywords[:2]):
                                    reason = f"Both discuss {concept}"
                                    self.potential_links[note_name].append((target_note, reason))
                                    
            # Check for direct name mentions without links
            for target_note in self.notes:
                if target_note != note_name:
                    # Create variations of the target note name
                    variations = [
                        target_note,
                        target_note.replace('-', ' '),
                        target_note.replace('_', ' '),
                        target_note.lower(),
                    ]
                    
                    for variation in variations:
                        if variation in content and target_note not in self.links[note_name]:
                            # Check it's not already linked with different text
                            if f"[[{target_note}" not in note_data['content']:
                                reason = f"Mentions '{variation}' without link"
                                self.potential_links[note_name].append((target_note, reason))
                                break
                                
        # Deduplicate suggestions
        for note in self.potential_links:
            unique_suggestions = {}
            for target, reason in self.potential_links[note]:
                if target not in unique_suggestions:
                    unique_suggestions[target] = reason
            self.potential_links[note] = list(unique_suggestions.items())
            
        total_suggestions = sum(len(suggestions) for suggestions in self.potential_links.values())
        print(f"  ✅ Generated {total_suggestions} link suggestions")
        
    def analyze_link_density(self):
        """Analyze the link density and connectivity of the graph."""
        print("📊 Analyzing link density...")
        
        # Calculate metrics
        total_notes = len(self.notes)
        total_possible_links = total_notes * (total_notes - 1)
        actual_links = sum(len(links) for links in self.links.values())
        link_density = (actual_links / total_possible_links * 100) if total_possible_links > 0 else 0
        
        # Find most connected notes
        connection_counts = Counter()
        for note in self.notes:
            connections = len(self.links.get(note, set())) + len(self.backlinks.get(note, set()))
            connection_counts[note] = connections
            
        return {
            'total_notes': total_notes,
            'total_links': actual_links,
            'link_density': link_density,
            'most_connected': connection_counts.most_common(10),
            'orphaned_count': len(self.orphaned_notes)
        }
        
    def generate_report(self):
        """Generate a comprehensive link analysis report."""
        print("📝 Generating link analysis report...")
        
        metrics = self.analyze_link_density()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        report = f"""---
title: Link Analysis Report
generated: {timestamp}
type: report
tags: [analysis, links, knowledge-graph]
---

# Obsidian Knowledge Graph Link Analysis

## Overview

This report analyzes the link structure of the Claude Ecosystem Knowledge Graph, identifying connections, orphaned notes, and suggesting new links to strengthen the graph.

## Summary Statistics

- **Total Notes**: {metrics['total_notes']}
- **Total Links**: {metrics['total_links']}
- **Link Density**: {metrics['link_density']:.2f}%
- **Orphaned Notes**: {metrics['orphaned_count']}

## Most Connected Notes

| Note | Connections |
|------|-------------|
"""
        
        for note, count in metrics['most_connected']:
            report += f"| [[{note}]] | {count} |\n"
            
        # Add orphaned notes section
        if self.orphaned_notes:
            report += "\n## Orphaned Notes\n\nThese notes have no incoming or outgoing links:\n\n"
            for note in sorted(self.orphaned_notes):
                report += f"- [[{note}]]\n"
                
        # Add suggested links section
        report += "\n## Suggested New Links\n\n"
        
        # Group suggestions by reason type
        suggestion_groups = defaultdict(list)
        for source, suggestions in self.potential_links.items():
            for target, reason in suggestions[:5]:  # Limit to top 5 per note
                suggestion_groups[reason.split()[0]].append((source, target, reason))
                
        for reason_type, suggestions in suggestion_groups.items():
            report += f"### {reason_type} References\n\n"
            for source, target, reason in suggestions[:20]:  # Limit each category
                report += f"- [[{source}]] → [[{target}]] ({reason})\n"
            report += "\n"
            
        # Add network analysis
        report += """## Network Analysis

### Key Observations

1. **Hub Notes**: The most connected notes serve as central concepts linking different areas
2. **Clustering**: Notes naturally cluster around projects (UltraThink, CAM, Contexify)
3. **Bridge Concepts**: Some notes bridge between different philosophical approaches

### Recommendations

1. **Connect Orphaned Notes**: Review orphaned notes and add relevant links
2. **Strengthen Cross-Project Links**: Add more connections between project boundaries
3. **Bidirectional Links**: Ensure important relationships have links in both directions
4. **Concept Definitions**: Link to concept definitions when terms are mentioned

## Implementation Guide

To implement suggested links:

1. Review each suggestion in context
2. Add wiki links where appropriate: `[[Target Note]]`
3. Consider adding context: `[[Target Note|descriptive text]]`
4. Update both directions for important relationships

## Next Steps

1. Process high-value link suggestions
2. Create "See Also" sections in orphaned notes
3. Add concept maps to visualize connections
4. Regular link audits to maintain graph health
"""
        
        # Write report
        report_path = self.vault_path / 'link-analysis-report.md'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
            
        print(f"  ✅ Report saved to: {report_path.name}")
        
        # Also create a quick fixes file
        self.generate_quick_fixes()
        
    def generate_quick_fixes(self):
        """Generate a file with quick link additions that can be easily applied."""
        print("🔧 Generating quick fixes file...")
        
        fixes = """---
title: Quick Link Fixes
type: guide
tags: [maintenance, links, fixes]
---

# Quick Link Fixes

Copy and paste these snippets to quickly add suggested links.

## High-Priority Additions

### Orphaned Notes
"""
        
        # Add fixes for orphaned notes
        for note in sorted(self.orphaned_notes)[:10]:
            fixes += f"\n#### {note}\n"
            fixes += "Add to bottom of note:\n```markdown\n## See Also\n"
            
            # Suggest related notes based on name/location
            note_path = str(self.notes[note]['path'])
            if 'UltraThink' in note_path:
                fixes += "- [[Claude-UltraThink]]\n- [[Single-Agent-Architecture]]\n"
            elif 'CAM' in note_path or 'Claude-AM' in note_path:
                fixes += "- [[Claude-AM]]\n- [[Multi-Agent-Orchestration]]\n"
            elif 'Contexify' in note_path:
                fixes += "- [[Claude-Contexify]]\n- [[Context-Window-Reality]]\n"
                
            fixes += "```\n"
            
        # Add top link suggestions
        fixes += "\n### Top Link Suggestions\n\n"
        
        added = 0
        for source, suggestions in self.potential_links.items():
            if added >= 20:
                break
                
            for target, reason in suggestions[:2]:
                if added >= 20:
                    break
                    
                fixes += f"**{source}** → [[{target}]]\n"
                fixes += f"- Reason: {reason}\n"
                fixes += f"- Add: `[[{target}]]` where relevant\n\n"
                added += 1
                
        # Write fixes file
        fixes_path = self.vault_path / 'quick-link-fixes.md'
        with open(fixes_path, 'w', encoding='utf-8') as f:
            f.write(fixes)
            
        print(f"  ✅ Quick fixes saved to: {fixes_path.name}")
        
    def run(self):
        """Run the complete link generation and analysis process."""
        print("🚀 Starting link analysis...")
        
        # Linear processing - one task at a time
        self.scan_vault()
        self.extract_existing_links()
        self.identify_orphaned_notes()
        self.suggest_new_links()
        self.generate_report()
        
        print("✨ Link analysis complete!")
        print(f"\n📋 Check these files:")
        print("  - link-analysis-report.md")
        print("  - quick-link-fixes.md")


if __name__ == "__main__":
    vault_path = "/Users/bioharz/git/2025_2/knowledge-graphs/claude-ecosystem"
    
    generator = ObsidianLinkGenerator(vault_path)
    generator.run()
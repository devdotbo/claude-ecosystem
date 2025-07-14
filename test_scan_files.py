#!/usr/bin/env python3
"""
Test scanning for markdown files in the vault.
"""

from pathlib import Path

def main():
    vault_path = Path(__file__).parent
    print(f"Scanning vault: {vault_path}")
    print("")
    
    # Count markdown files
    md_files = list(vault_path.rglob('*.md'))
    print(f"Found {len(md_files)} markdown files")
    
    # Show first 10
    print("\nFirst 10 files:")
    for i, md_file in enumerate(md_files[:10]):
        relative = md_file.relative_to(vault_path)
        print(f"  {i+1}. {relative}")
    
    # Count by directory
    print("\nFiles by directory:")
    dirs = {}
    for md_file in md_files:
        parent = md_file.parent.relative_to(vault_path)
        parent_str = str(parent) if str(parent) != '.' else 'root'
        dirs[parent_str] = dirs.get(parent_str, 0) + 1
    
    for dir_name, count in sorted(dirs.items()):
        print(f"  {dir_name}: {count} files")

if __name__ == "__main__":
    main()
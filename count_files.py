#!/usr/bin/env python3
from pathlib import Path

vault = Path.cwd()
md_files = list(vault.rglob('*.md'))
print(f"Total markdown files: {len(md_files)}")

# Count by directory
dirs = {}
for f in md_files:
    parent = f.parent.name
    dirs[parent] = dirs.get(parent, 0) + 1

print("\nBy directory:")
for d, count in sorted(dirs.items()):
    print(f"  {d}: {count}")
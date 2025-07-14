#!/usr/bin/env python3
"""
Simple test to verify scripts work.
Run this with: python3 simple_test.py
"""

import sys
import os

print("Testing Python environment...")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print("")

# Test 1: Can we import the scripts?
try:
    import extract_docs
    print("✅ extract_docs.py imports successfully")
except Exception as e:
    print(f"❌ Error importing extract_docs.py: {e}")

try:
    import generate_links
    print("✅ generate_links.py imports successfully")
except Exception as e:
    print(f"❌ Error importing generate_links.py: {e}")

# Test 2: Can we instantiate the classes?
try:
    from pathlib import Path
    vault_path = Path(__file__).parent
    
    # Test generate_links
    generator = generate_links.ObsidianLinkGenerator(str(vault_path))
    print(f"✅ Created link generator for vault: {vault_path}")
    
    # Test extract_docs
    source_base = "/Users/bioharz/git/2025_2"
    target_base = str(vault_path)
    extractor = extract_docs.ObsidianDocExtractor(source_base, target_base)
    print("✅ Created doc extractor")
    
except Exception as e:
    print(f"❌ Error creating instances: {e}")
    import traceback
    traceback.print_exc()

print("\nTo run the actual scripts:")
print("1. Delete existing reports: rm link-analysis-report.md quick-link-fixes.md")
print("2. Run link generator: python3 generate_links.py")
print("3. Check for generated reports")
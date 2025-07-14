#!/usr/bin/env python3
"""
Test harness for knowledge graph scripts.
Following UltraThink's linear processing - test one script at a time.
"""

import os
import sys
import subprocess
from pathlib import Path

def test_python_environment():
    """Test that Python environment is working."""
    print("=== Testing Python Environment ===")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Current directory: {os.getcwd()}")
    
    # Check if we can import standard libraries
    try:
        import re
        import json
        from collections import defaultdict
        print("✅ Standard library imports working")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_extract_docs():
    """Test the extract_docs.py script."""
    print("\n=== Testing extract_docs.py ===")
    
    script_path = Path(__file__).parent / "extract_docs.py"
    
    # Check if script exists
    if not script_path.exists():
        print(f"❌ Script not found: {script_path}")
        return False
        
    print(f"✅ Script found: {script_path}")
    
    # Try to run it
    try:
        # First, let's just try to import it to check for syntax errors
        import extract_docs
        print("✅ Script imports successfully")
        
        # Check if the source directories exist
        source_base = Path("/Users/bioharz/git/2025_2")
        for project in ['claude-ultrathink', 'claude-am', 'claude-contexify']:
            project_path = source_base / project
            if project_path.exists():
                print(f"✅ Source found: {project}")
            else:
                print(f"⚠️  Source missing: {project}")
                
        return True
        
    except Exception as e:
        print(f"❌ Error testing extract_docs: {e}")
        return False

def test_generate_links():
    """Test the generate_links.py script."""
    print("\n=== Testing generate_links.py ===")
    
    script_path = Path(__file__).parent / "generate_links.py"
    
    # Check if script exists
    if not script_path.exists():
        print(f"❌ Script not found: {script_path}")
        return False
        
    print(f"✅ Script found: {script_path}")
    
    # Try to run it
    try:
        # Delete existing manual reports if they exist
        report_files = ['link-analysis-report.md', 'quick-link-fixes.md']
        for report in report_files:
            report_path = Path(__file__).parent / report
            if report_path.exists():
                print(f"ℹ️  Found existing {report} - would be overwritten")
        
        # Import to check for errors
        import generate_links
        print("✅ Script imports successfully")
        
        # Check vault structure
        vault_path = Path(__file__).parent
        md_files = list(vault_path.rglob('*.md'))
        print(f"✅ Found {len(md_files)} markdown files in vault")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing generate_links: {e}")
        import traceback
        traceback.print_exc()
        return False

def run_script_with_output(script_name):
    """Actually run a script and capture output."""
    print(f"\n=== Running {script_name} ===")
    
    script_path = Path(__file__).parent / script_name
    
    try:
        # Use subprocess to run the script
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            cwd=str(Path(__file__).parent)
        )
        
        print("STDOUT:")
        print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
            
        if result.returncode == 0:
            print(f"✅ {script_name} executed successfully")
            return True
        else:
            print(f"❌ {script_name} failed with return code: {result.returncode}")
            return False
            
    except Exception as e:
        print(f"❌ Error running {script_name}: {e}")
        return False

def main():
    """Run all tests following UltraThink's linear processing."""
    print("🚀 Starting Knowledge Graph Script Tests")
    print("Following UltraThink's linear processing - one test at a time\n")
    
    # Test 1: Python environment
    if not test_python_environment():
        print("\n❌ Python environment test failed. Cannot proceed.")
        return
        
    # Test 2: Extract docs script
    if not test_extract_docs():
        print("\n❌ extract_docs.py test failed.")
    
    # Test 3: Generate links script  
    if not test_generate_links():
        print("\n❌ generate_links.py test failed.")
        
    # Now try to actually run the scripts
    print("\n" + "="*50)
    print("ATTEMPTING TO RUN SCRIPTS")
    print("="*50)
    
    # Don't run extract_docs as it would overwrite existing files
    print("\n⚠️  Skipping extract_docs.py execution (would overwrite existing files)")
    
    # Run generate_links
    if run_script_with_output("generate_links.py"):
        # Check if reports were generated
        report_files = ['link-analysis-report.md', 'quick-link-fixes.md']
        for report in report_files:
            report_path = Path(__file__).parent / report
            if report_path.exists():
                print(f"✅ Generated: {report}")
            else:
                print(f"❌ Missing: {report}")
    
    print("\n✨ Testing complete!")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Execute the knowledge graph scripts and verify outputs.
Following UltraThink's linear processing methodology.
"""

import os
import sys
from pathlib import Path

def run_command(cmd_name, cmd_func):
    """Run a command and report results."""
    print(f"\n{'='*60}")
    print(f"Running: {cmd_name}")
    print('='*60)
    try:
        result = cmd_func()
        print(f"✅ {cmd_name} completed successfully")
        return True
    except Exception as e:
        print(f"❌ {cmd_name} failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_environment():
    """Test Python environment."""
    print(f"Python version: {sys.version}")
    print(f"Current directory: {os.getcwd()}")
    
    # Test imports
    try:
        import generate_links
        import extract_docs
        print("✅ All modules import successfully")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_file_scanning():
    """Test scanning for markdown files."""
    from pathlib import Path
    vault_path = Path.cwd()
    md_files = list(vault_path.rglob('*.md'))
    print(f"Found {len(md_files)} markdown files in vault")
    
    # Show some examples
    print("\nSample files:")
    for f in md_files[:5]:
        print(f"  - {f.relative_to(vault_path)}")
    
    return len(md_files) > 0

def run_link_generator():
    """Run the link generator script."""
    # Remove old reports
    for report in ['link-analysis-report.md', 'quick-link-fixes.md']:
        if Path(report).exists():
            os.remove(report)
            print(f"Removed old {report}")
    
    # Import and run
    import generate_links
    generator = generate_links.ObsidianLinkGenerator(str(Path.cwd()))
    generator.run()
    
    # Verify outputs
    success = True
    for report in ['link-analysis-report.md', 'quick-link-fixes.md']:
        if Path(report).exists():
            size = Path(report).stat().st_size
            print(f"✅ Generated {report} ({size} bytes)")
        else:
            print(f"❌ Missing {report}")
            success = False
    
    return success

def main():
    """Run all tests in sequence."""
    print("🚀 Claude Ecosystem Knowledge Graph - Script Testing")
    print("Following UltraThink's linear processing methodology")
    
    tests = [
        ("Environment Test", test_environment),
        ("File Scanning Test", test_file_scanning),
        ("Link Generator", run_link_generator),
    ]
    
    results = []
    for test_name, test_func in tests:
        success = run_command(test_name, test_func)
        results.append((test_name, success))
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    total_pass = sum(1 for _, success in results if success)
    print(f"\nTotal: {total_pass}/{len(results)} tests passed")
    
    if total_pass == len(results):
        print("\n✨ All tests passed! Scripts are working correctly.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
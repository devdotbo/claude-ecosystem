#!/usr/bin/env python3
"""
Run the link generator script after removing old reports.
This follows UltraThink's linear processing - one task at a time.
"""

import os
import sys
from pathlib import Path

def main():
    print("🚀 Running Link Generator Script")
    print("Following UltraThink's linear processing methodology\n")
    
    # Step 1: Check current directory
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")
    
    # Step 2: Remove existing reports
    report_files = ['link-analysis-report.md', 'quick-link-fixes.md']
    
    for report in report_files:
        report_path = current_dir / report
        if report_path.exists():
            print(f"Removing existing {report}...")
            os.remove(report_path)
            print(f"  ✅ Removed {report}")
        else:
            print(f"  ℹ️  {report} not found (already removed)")
    
    print("")
    
    # Step 3: Import and run the generator
    try:
        print("Importing generate_links module...")
        import generate_links
        print("  ✅ Module imported successfully")
        
        print("\nCreating link generator...")
        generator = generate_links.ObsidianLinkGenerator(str(current_dir))
        print("  ✅ Generator created")
        
        print("\nRunning link analysis...")
        generator.run()
        
        print("\n" + "="*50)
        print("VERIFICATION")
        print("="*50)
        
        # Step 4: Verify outputs
        for report in report_files:
            report_path = current_dir / report
            if report_path.exists():
                size = report_path.stat().st_size
                print(f"✅ {report} created ({size} bytes)")
            else:
                print(f"❌ {report} not found!")
                
    except Exception as e:
        print(f"\n❌ Error running generate_links: {e}")
        import traceback
        traceback.print_exc()
        return 1
        
    print("\n✨ Link generator complete!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
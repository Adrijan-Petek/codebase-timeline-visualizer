#!/usr/bin/env python3
"""
Example usage of the Codebase Timeline Visualizer.
"""

import sys
import os
from pathlib import Path

# Add the backend src to the path
sys.path.insert(0, str(Path(__file__).parent / 'backend' / 'src'))

from main import analyze_repository

def main():
    """Example of analyzing a repository."""
    # Example: analyze the current directory if it's a git repo
    current_dir = Path.cwd()

    if not (current_dir / '.git').exists():
        print("Error: Current directory is not a Git repository.")
        print("Please run this script from within a Git repository.")
        return 1

    print(f"Analyzing repository: {current_dir}")

    try:
        # Analyze the repository
        timeline_data = analyze_repository(str(current_dir), 'example_timeline.json')

        # Print some statistics
        metadata = timeline_data['metadata']
        print("\nRepository Statistics:")
        print(f"  Total commits: {metadata['total_commits']}")
        print(f"  Total contributors: {metadata['total_contributors']}")
        print(f"  Total files: {metadata['total_files']}")

        if metadata['date_range']['start'] and metadata['date_range']['end']:
            print(f"  Date range: {metadata['date_range']['start']} to {metadata['date_range']['end']}")

        # Print top contributors
        contributors = timeline_data['contributors']
        print("\nTop Contributors:")
        sorted_contributors = sorted(contributors.items(),
                                   key=lambda x: x[1]['commits'],
                                   reverse=True)[:5]

        for i, (name, data) in enumerate(sorted_contributors, 1):
            print(f"  {i}. {name}: {data['commits']} commits, "
                  f"+{data['lines_added']} -{data['lines_removed']} lines")

        print("\nTimeline data saved to: example_timeline.json")
        print("You can now:")
        print("1. Open the data in the web interface: codevis serve")
        print("2. Use it for further analysis or visualization")

    except Exception as e:
        print(f"Error analyzing repository: {e}")
        return 1

    return 0

if __name__ == '__main__':
    exit(main())
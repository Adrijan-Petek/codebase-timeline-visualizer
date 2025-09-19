"""
Main module for codebase timeline visualization backend.
"""

from pathlib import Path
from typing import Dict, Any
from .analyzer import GitAnalyzer
from .exporter import DataExporter


def analyze_repository(repo_path: str, output_path: str = None) -> Dict[str, Any]:
    """Analyze a Git repository and generate timeline data."""
    if not Path(repo_path).exists():
        raise ValueError(f"Repository path does not exist: {repo_path}")

    if not Path(repo_path, '.git').exists():
        raise ValueError(f"Not a Git repository: {repo_path}")

    print(f"Analyzing repository: {repo_path}")

    # Initialize analyzer
    analyzer = GitAnalyzer(repo_path)

    # Analyze commits
    print("Extracting commit history...")
    commits = analyzer.analyze_commits()
    print(f"Found {len(commits)} commits")

    # Calculate statistics
    print("Calculating contributor statistics...")
    contributors = analyzer.get_contributor_stats(commits)

    print("Calculating file statistics...")
    files = analyzer.get_file_stats(commits)

    # Create timeline data
    print("Creating timeline data...")
    timeline_data = DataExporter.create_timeline_data(commits, contributors, files)

    # Export if output path provided
    if output_path:
        DataExporter.export_json(timeline_data, output_path)
        print(f"Analysis complete! Data saved to {output_path}")

    return timeline_data


def main():
    """Command-line interface for repository analysis."""
    import argparse

    parser = argparse.ArgumentParser(description='Analyze Git repository for timeline visualization')
    parser.add_argument('repo_path', help='Path to Git repository')
    parser.add_argument('-o', '--output', default='timeline.json',
                       help='Output file path (default: timeline.json)')

    args = parser.parse_args()

    try:
        analyze_repository(args.repo_path, args.output)
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
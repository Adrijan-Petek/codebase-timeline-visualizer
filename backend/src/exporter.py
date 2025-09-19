"""
Data export utilities for timeline visualization.
"""

import json
import csv
from typing import List, Dict, Any
from pathlib import Path


class DataExporter:
    """Handles exporting timeline data to various formats."""

    @staticmethod
    def export_json(data: Dict[str, Any], output_path: str) -> None:
        """Export timeline data to JSON format."""
        output_file = Path(output_path)

        # Ensure output directory exists
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Timeline data exported to {output_path}")

    @staticmethod
    def export_csv(commits: List[Dict[str, Any]], output_path: str) -> None:
        """Export commit data to CSV format."""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = [
                "hash",
                "author",
                "email",
                "timestamp",
                "datetime",
                "message",
                "lines_added",
                "lines_removed",
                "total_files",
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for commit in commits:
                writer.writerow(
                    {
                        "hash": commit["hash"],
                        "author": commit["author"],
                        "email": commit["email"],
                        "timestamp": commit["timestamp"],
                        "datetime": commit["datetime"],
                        "message": commit["message"],
                        "lines_added": commit["lines_added"],
                        "lines_removed": commit["lines_removed"],
                        "total_files": commit["total_files"],
                    }
                )

        print(f"Commit data exported to {output_path}")

    @staticmethod
    def create_timeline_data(
        commits: List[Dict[str, Any]],
        contributors: Dict[str, Any],
        files: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Create complete timeline data structure for visualization."""
        # Calculate cumulative statistics
        cumulative_lines = 0
        cumulative_files = 0
        timeline_events = []

        for commit in commits:
            cumulative_lines += commit["lines_added"] - commit["lines_removed"]
            cumulative_files = len(files)  # This is approximate

            event = {
                "timestamp": commit["timestamp"],
                "datetime": commit["datetime"],
                "commit_hash": commit["hash"],
                "author": commit["author"],
                "message": commit["message"],
                "files_changed": commit["files_changed"],
                "lines_added": commit["lines_added"],
                "lines_removed": commit["lines_removed"],
                "cumulative_lines": cumulative_lines,
                "cumulative_files": cumulative_files,
            }
            timeline_events.append(event)

        return {
            "metadata": {
                "total_commits": len(commits),
                "total_contributors": len(contributors),
                "total_files": len(files),
                "date_range": {
                    "start": commits[0]["datetime"] if commits else None,
                    "end": commits[-1]["datetime"] if commits else None,
                },
            },
            "timeline": timeline_events,
            "contributors": contributors,
            "files": files,
        }

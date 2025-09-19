"""
Git repository analyzer for codebase timeline visualization.
"""

from typing import List, Dict, Any
from git import Repo
from pydriller import Repository


class GitAnalyzer:
    """Analyzes Git repository history and extracts timeline data."""

    def __init__(self, repo_path: str):
        """Initialize analyzer with repository path."""
        self.repo_path = repo_path
        self.repo = Repo(repo_path)

    def analyze_commits(self) -> List[Dict[str, Any]]:
        """Analyze all commits in the repository."""
        commits_data = []

        for commit in Repository(self.repo_path).traverse_commits():
            commit_data = self._extract_commit_data(commit)
            commits_data.append(commit_data)

        # Sort by date (oldest first)
        commits_data.sort(key=lambda x: x["timestamp"])

        return commits_data

    def _extract_commit_data(self, commit) -> Dict[str, Any]:
        """Extract data from a single commit."""
        files_changed = []
        lines_added = 0
        lines_removed = 0

        for modification in commit.modifications:
            file_data = {
                "filename": modification.filename,
                "old_path": modification.old_path,
                "new_path": modification.new_path,
                "change_type": modification.change_type.name,
                "lines_added": modification.added_lines,
                "lines_removed": modification.removed_lines,
                "complexity": getattr(modification, "complexity", 0),
            }
            files_changed.append(file_data)

            lines_added += modification.added_lines
            lines_removed += modification.removed_lines

        return {
            "hash": commit.hash,
            "author": commit.author.name,
            "email": commit.author.email,
            "timestamp": commit.author_date.timestamp(),
            "datetime": commit.author_date.isoformat(),
            "message": commit.msg,
            "files_changed": files_changed,
            "lines_added": lines_added,
            "lines_removed": lines_removed,
            "total_files": len(files_changed),
        }

    def get_contributor_stats(self, commits: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate contributor statistics."""
        contributors = {}

        for commit in commits:
            author = commit["author"]
            email = commit["email"]

            if author not in contributors:
                contributors[author] = {
                    "email": email,
                    "commits": 0,
                    "lines_added": 0,
                    "lines_removed": 0,
                    "files_changed": 0,
                    "first_commit": commit["timestamp"],
                    "last_commit": commit["timestamp"],
                }

            contributors[author]["commits"] += 1
            contributors[author]["lines_added"] += commit["lines_added"]
            contributors[author]["lines_removed"] += commit["lines_removed"]
            contributors[author]["files_changed"] += commit["total_files"]
            contributors[author]["first_commit"] = min(
                contributors[author]["first_commit"], commit["timestamp"]
            )
            contributors[author]["last_commit"] = max(
                contributors[author]["last_commit"], commit["timestamp"]
            )

        return contributors

    def get_file_stats(self, commits: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate file-level statistics."""
        files = {}

        for commit in commits:
            for file_change in commit["files_changed"]:
                filename = file_change["filename"]

                if filename not in files:
                    files[filename] = {
                        "changes": 0,
                        "lines_added": 0,
                        "lines_removed": 0,
                        "authors": set(),
                        "first_change": commit["timestamp"],
                        "last_change": commit["timestamp"],
                    }

                files[filename]["changes"] += 1
                files[filename]["lines_added"] += file_change["lines_added"]
                files[filename]["lines_removed"] += file_change["lines_removed"]
                files[filename]["authors"].add(commit["author"])
                files[filename]["first_change"] = min(
                    files[filename]["first_change"], commit["timestamp"]
                )
                files[filename]["last_change"] = max(
                    files[filename]["last_change"], commit["timestamp"]
                )

        # Convert sets to lists for JSON serialization
        for file_data in files.values():
            file_data["authors"] = list(file_data["authors"])

        return files

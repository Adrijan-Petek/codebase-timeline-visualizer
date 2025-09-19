"""
Tests for Git analyzer module.
"""

import pytest
import tempfile
import os
import sys
from pathlib import Path
from git import Repo

# Add the backend src directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from analyzer import GitAnalyzer


@pytest.fixture
def sample_repo():
    """Create a temporary Git repository with some commits for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        repo = Repo.init(temp_dir)
        
        # Configure git user for commits
        with repo.config_writer() as git_config:
            git_config.set_value("user", "name", "Test User")
            git_config.set_value("user", "email", "test@example.com")

        # Create initial commit
        readme = Path(temp_dir) / 'README.md'
        readme.write_text('# Test Repository\n')
        repo.index.add(['README.md'])
        repo.index.commit('Initial commit')

        # Create second commit
        main_py = Path(temp_dir) / 'main.py'
        main_py.write_text('print("Hello World")')
        repo.index.add(['main.py'])
        repo.index.commit('Add main.py')

        # Create third commit
        main_py.write_text('print("Hello World")\nprint("Updated")')
        repo.index.add(['main.py'])
        repo.index.commit('Update main.py')

        yield temp_dir


def test_analyzer_initialization(sample_repo):
    """Test that analyzer can be initialized with a valid repo."""
    analyzer = GitAnalyzer(sample_repo)
    assert analyzer.repo_path == sample_repo
    assert analyzer.repo is not None


def test_commit_analysis(sample_repo):
    """Test that commits are properly analyzed."""
    analyzer = GitAnalyzer(sample_repo)
    commits = analyzer.analyze_commits()

    # Should have 3 commits
    assert len(commits) >= 3
    
    # Check that commits have required fields
    for commit in commits:
        assert 'hash' in commit
        assert 'author' in commit
        assert 'message' in commit
        assert 'timestamp' in commit
        assert 'files_changed' in commit
        assert isinstance(commit['files_changed'], list)
    
    # Check commit messages are present
    commit_messages = [c['message'] for c in commits]
    assert 'Initial commit' in commit_messages
    assert 'Add main.py' in commit_messages
    assert 'Update main.py' in commit_messages


def test_contributor_stats(sample_repo):
    """Test contributor statistics calculation."""
    analyzer = GitAnalyzer(sample_repo)
    commits = analyzer.analyze_commits()
    contributors = analyzer.get_contributor_stats(commits)

    # Should have one contributor (the test user)
    assert len(contributors) >= 1

    # Check that stats are calculated
    for contributor_data in contributors.values():
        assert 'commits' in contributor_data
        assert 'lines_added' in contributor_data
        assert 'lines_removed' in contributor_data
        assert contributor_data['commits'] > 0


def test_file_stats(sample_repo):
    """Test file statistics calculation."""
    analyzer = GitAnalyzer(sample_repo)
    commits = analyzer.analyze_commits()
    files = analyzer.get_file_stats(commits)

    assert 'README.md' in files
    assert 'main.py' in files

    # Check main.py has been modified
    assert files['main.py']['changes'] >= 2
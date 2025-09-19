"""
Command-line interface for Codebase Timeline Visualizer.
"""

import os
import sys
from pathlib import Path
import click
from flask import Flask, send_from_directory
from flask_cors import CORS

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'backend' / 'src'))

from main import analyze_repository


@click.group()
@click.version_option(version='1.0.0')
def cli():
    """Codebase Timeline Visualizer - Make Git history visual and interactive."""
    pass


@cli.command()
@click.argument('repo_path', type=click.Path(exists=True))
@click.option('-o', '--output', default='timeline.json',
              help='Output file path for timeline data')
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose output')
def analyze(repo_path, output, verbose):
    """Analyze a Git repository and generate timeline data."""
    try:
        if verbose:
            click.echo(f"Analyzing repository: {repo_path}")

        timeline_data = analyze_repository(repo_path, output)

        if verbose:
            click.echo(f"Analysis complete!")
            click.echo(f"  - Total commits: {timeline_data['metadata']['total_commits']}")
            click.echo(f"  - Total contributors: {timeline_data['metadata']['total_contributors']}")
            click.echo(f"  - Total files: {timeline_data['metadata']['total_files']}")
        else:
            click.echo(f"Repository analyzed successfully. Data saved to {output}")

    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@cli.command()
@click.option('-p', '--port', default=3001, help='Port to run the server on')
@click.option('-d', '--data', default='timeline.json',
              help='Path to timeline data file')
def serve(port, data):
    """Start the web interface server."""
    app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
    CORS(app)

    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/api/timeline')
    def get_timeline():
        if os.path.exists(data):
            return send_from_directory('.', data)
        return {'error': 'Timeline data not found'}, 404

    click.echo(f"Starting server on http://localhost:{port}")
    click.echo(f"Timeline data: {data}")
    app.run(port=port, debug=True)


@cli.command()
@click.argument('data_file', type=click.Path(exists=True))
@click.option('-f', '--format', type=click.Choice(['html', 'mp4', 'gif']),
              default='html', help='Export format')
@click.option('-o', '--output', help='Output file path')
def export(data_file, format, output):
    """Export timeline visualization to different formats."""
    if not output:
        base_name = Path(data_file).stem
        output = f"{base_name}_timeline.{format}"

    click.echo(f"Exporting {data_file} to {output} (format: {format})")

    # TODO: Implement actual export functionality
    click.echo("Export functionality coming soon!")


if __name__ == '__main__':
    cli()
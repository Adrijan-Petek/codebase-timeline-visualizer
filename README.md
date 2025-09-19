# Codebase Timeline Visualizer

A tool that animates the evolution of a codebase over time by parsing the Git history and showing how files, directories, and contributors change.

## Features

- **Repository Analysis**: Parse Git commit history and extract detailed commit data
- **Timeline Animation**: Interactive visualization of repo growth over time
- **Visualization Modes**: File tree, graph, and heatmap views
- **Contributor Tracking**: Show contributor activity and stats
- **Metrics Dashboard**: Commit activity, LOC growth, language breakdown
- **Export Options**: MP4/GIF animations and interactive HTML

## Quick Start

### Using Docker (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd codebase-timeline-visualizer

# Start all services
docker-compose up -d

# Access the web interface at http://localhost:3000
```

### Manual Installation

#### Step 1: Run Setup Check
```bash
# Windows (recommended)
.\setup.bat

# Or manually check setup
python check_setup.py
```

#### Step 2: Install Dependencies
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install Python dependencies
pip install -r requirements.txt

# Install frontend dependencies (optional)
cd frontend
npm install
cd ..
```

#### Step 3: Test Installation
```bash
# Run setup check again
python check_setup.py

# Try the example
python example.py
```

### Troubleshooting

If you encounter issues during setup:
- 📖 See [Setup Troubleshooting Guide](SETUP_TROUBLESHOOTING.md)
- 🔧 Run the setup helper: `.\setup.bat` (Windows)
- 💬 Check the [GitHub Issues](https://github.com/yourusername/codebase-timeline-visualizer/issues)

## Usage

### CLI Commands

```bash
# Analyze a repository
python -m cli.src.main analyze /path/to/repo

# Start web interface
python -m cli.src.main serve

# Export timeline (coming soon)
python -m cli.src.main export timeline.json --format html
```

### Web Interface

The web interface provides interactive timeline visualization with:
- Play/pause controls
- Scrubbing timeline
- Multiple visualization modes
- Contributor tracking
- Metrics dashboard

## GitHub Workflows

This project includes comprehensive CI/CD workflows:

### 🔄 CI Pipeline (`ci.yml`)
- **Multi-platform testing**: Ubuntu, Windows, macOS
- **Multi-Python testing**: Python 3.8, 3.9, 3.10, 3.11
- **Code quality checks**: flake8, black, mypy
- **Test coverage**: pytest with coverage reporting
- **Integration testing**: End-to-end CLI testing

### 🚀 Deployment (`deploy-frontend.yml`)
- **GitHub Pages deployment**: Automatic frontend deployment
- **Build optimization**: Production-ready builds
- **CDN integration**: Fast global content delivery

### 📦 Release Management (`release.yml`)
- **Automated releases**: Tag-based releases
- **PyPI publishing**: Automatic package distribution
- **Cross-platform builds**: Wheels for all platforms
- **Demo generation**: Live demo with sample data

### 🔒 Security & Quality (`security.yml`, `dependencies.yml`, `quality-gates.yml`)
- **CodeQL analysis**: Automated security scanning
- **Dependency vulnerability scanning**: Safety and audit-ci
- **Code quality gates**: Complexity, maintainability, security checks
- **SonarCloud integration**: Advanced code analysis

### 🌐 Cross-Platform (`cross-platform.yml`)
- **Performance testing**: Automated performance benchmarks
- **Compatibility testing**: Multiple OS and Python versions
- **Load testing**: Repository size and complexity testing

### 📚 Documentation (`docs.yml`)
- **Automated docs deployment**: GitHub Pages documentation
- **API documentation**: Auto-generated from code
- **Usage examples**: Interactive documentation

### 🐳 Containerization (`docker.yml`)
- **Multi-stage builds**: Optimized Docker images
- **Registry integration**: GitHub Container Registry
- **Demo deployment**: Containerized demo environment

### 🤖 Automation (`issue-management.yml`, `release-notes.yml`)
- **Issue triage**: Automatic labeling and categorization
- **Stale management**: Automatic cleanup of old issues/PRs
- **Release notes**: Auto-generated from commit messages
- **Changelog updates**: Automatic CHANGELOG.md maintenance

### 🔄 Dependency Management (`.github/dependabot.yml`)
- **Automated updates**: Weekly dependency updates
- **Security patches**: Priority security updates
- **Multi-ecosystem**: Python, Node.js, GitHub Actions

## Development

### Prerequisites

- Python 3.8+
- Node.js 18+
- Docker (optional)
- Git

### Local Development

```bash
# Clone the repository
git clone <repository-url>
cd codebase-timeline-visualizer

# Set up Python virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .[dev]
cd frontend && npm install && cd ..

# Run tests
pytest

# Start development servers
# Terminal 1: Backend
python -m cli.src.main serve

# Terminal 2: Frontend
cd frontend && npm start
```

### Code Quality

```bash
# Format code
black backend/src cli/src
isort backend/src cli/src

# Lint code
flake8 backend/src cli/src
mypy backend/src cli/src

# Run tests with coverage
pytest --cov=backend/src --cov-report=html
```

### Docker Development

```bash
# Build all services
docker-compose build

# Start development environment
docker-compose up

# Run tests in containers
docker-compose -f docker-compose.test.yml up --abort-on-container-exit
```

## Project Structure

```
codebase-timeline-visualizer/
├── backend/              # Python backend
│   ├── src/             # Source code
│   │   ├── analyzer.py  # Git analysis logic
│   │   ├── exporter.py  # Data export utilities
│   │   └── main.py      # Main analysis function
│   └── tests/           # Unit tests
├── frontend/            # React web application
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── App.js       # Main app component
│   │   └── index.js     # App entry point
│   └── public/          # Static assets
├── cli/                 # Command-line interface
├── docs/                # Documentation
├── .github/             # GitHub workflows and configs
│   ├── workflows/       # CI/CD pipelines
│   └── dependabot.yml   # Dependency updates
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Python project config
├── setup.py            # Package setup
├── Dockerfile          # Container definition
├── docker-compose.yml  # Multi-service setup
└── README.md           # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Workflow

- All PRs require CI checks to pass
- Code must be formatted with Black
- Tests must have >80% coverage
- Security scans must pass
- Documentation must be updated

## License

MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📖 [Documentation](https://yourusername.github.io/codebase-timeline-visualizer/)
- 🐛 [Issues](https://github.com/yourusername/codebase-timeline-visualizer/issues)
- 💬 [Discussions](https://github.com/yourusername/codebase-timeline-visualizer/discussions)

---

⭐ **Star this repo** if you find it useful!
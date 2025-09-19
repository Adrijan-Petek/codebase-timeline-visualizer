# Getting Started

This guide will help you get the Codebase Timeline Visualizer up and running.

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- Git

## Installation

1. **Clone or download the project:**
   ```bash
   git clone <repository-url>
   cd codebase-timeline-visualizer
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies:**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

## Quick Start

### Analyze a Repository

1. **Navigate to any Git repository:**
   ```bash
   cd /path/to/your/git/repo
   ```

2. **Run the analyzer:**
   ```bash
   python ../codebase-timeline-visualizer/example.py
   ```

   This will:
   - Analyze the Git history
   - Generate `example_timeline.json` with timeline data
   - Display repository statistics

### View the Timeline

1. **Start the web interface:**
   ```bash
   cd codebase-timeline-visualizer
   python -m cli.src.main serve
   ```

2. **Open your browser:**
   Navigate to `http://localhost:3001`

3. **Load timeline data:**
   The web interface will automatically load `timeline.json` if it exists in the project root.

## CLI Commands

The tool provides several CLI commands:

```bash
# Analyze a repository
python -m cli.src.main analyze /path/to/repo

# Start web server
python -m cli.src.main serve

# Export timeline (coming soon)
python -m cli.src.main export timeline.json --format html
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
│   └── src/
│       └── main.py      # CLI commands
├── requirements.txt     # Python dependencies
├── setup.py            # Python package setup
└── README.md           # Project documentation
```

## Development

### Running Tests

```bash
cd backend
python -m pytest tests/
```

### Building Frontend

```bash
cd frontend
npm run build
```

### Development Server

```bash
cd frontend
npm start
```

## Troubleshooting

### Common Issues

1. **"Module not found" errors:**
   - Make sure you've installed all dependencies
   - Check that you're in the correct directory

2. **Git repository not found:**
   - Ensure the path points to a valid Git repository
   - Check that `.git` directory exists

3. **Port already in use:**
   - Change the port with `codevis serve --port 3002`

### Getting Help

- Check the main README.md for detailed documentation
- Run commands with `--help` for usage information
- Check the console for error messages

## Next Steps

- Try analyzing different repositories
- Experiment with the timeline controls
- Explore the generated JSON data structure
- Contribute improvements or report issues
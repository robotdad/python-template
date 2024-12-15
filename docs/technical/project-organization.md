# Modern Python Project Template

This document describes the standardized structure for Python projects with modern tooling and development practices.

## Project Structure

```
project-name/
├── src/                     # Main package directory
│   └── your_package/        # Replace with your package name
│       ├── __init__.py      # Package initialization
│       └── core/            # Core functionality
├── tests/                   # Test directory
│   ├── __init__.py
│   ├── conftest.py          # Pytest fixtures
│   └── test_*.py            # Test modules
├── docs/                    # Documentation
│   ├── technical/           # Technical documentation
│   └── user/                # User documentation
├── scripts/                 # Utility scripts and tools
├── notebooks/               # Jupyter notebooks (if needed)
├── .env.template            # Template for environment variables
├── .gitignore               # Git ignore patterns
├── .pre-commit-config.yaml  # Pre-commit hooks configuration
├── pyproject.toml           # Project configuration and dependencies
├── README.md                # Project documentation
└── LICENSE                  # Project license
```
## Key Components

### src Directory
The `src` layout is used for better packaging practices:
- Prevents accidental imports of the development package
- Ensures testing against installed package
- Provides clean separation of package code
- Mirrors distribution structure

### scripts Directory
- Contains utility scripts and tools
- Development helper scripts
- Deployment scripts
- Data processing utilities
- Not included in the main package distribution

### Documentation Structure
- `docs/technical/`: Implementation details, architecture
- `docs/user/`: Usage guides, API documentation
- README.md: Project overview and quick start

### Development Tools
- Type checking: mypy
- Code formatting: black
- Import sorting: isort
- Linting: ruff
- Security: bandit, safety
- Pre-commit hooks for automated checks

### Testing
- pytest for test running
- Coverage reporting
- Fixtures in conftest.py
- Clear separation of unit and integration tests

## Best Practices

### Code Organization
- Use type hints consistently
- Follow PEP 8 style guidelines
- Keep modules focused and single-purpose
- Document public APIs

### Environment Management
- Use virtual environments
- Manage dependencies with pyproject.toml
- Use environment variables for configuration
- Never commit sensitive information

### Version Control
- Meaningful commit messages
- Feature branches for development
- Pre-commit hooks for quality checks
- Clear .gitignore rules

### Documentation
- Keep README.md updated
- Document all public APIs
- Include usage examples
- Maintain technical documentation

## Setup Instructions

1. Create new project:
   ```bash
   mkdir project-name
   cd project-name
   git init
   ```

2. Set up virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   uv pip install -e ".[dev]"
   ```

4. Initialize pre-commit:
   ```bash
   pre-commit install
   ```

## Development Workflow

1. Install in development mode
2. Run tests with pytest
3. Use pre-commit hooks
4. Update documentation
5. Regular dependency updates
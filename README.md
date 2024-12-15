# Modern Python Project Template

A comprehensive template for Python projects following modern development practices. This template includes a working example package (a simple calculator) to demonstrate project structure, testing patterns, and development workflows.

## Features

- **Modern Project Structure**
  - `src` layout for proper packaging
  - Clear separation of package code, tests, and documentation
  - Example scripts directory for utilities and tools

- **Development Tools**
  - Type checking with mypy
  - Code formatting with black
  - Import sorting with isort
  - Linting with ruff
  - Security checking with bandit and safety
  - Pre-commit hooks for automated checks

- **Testing Framework**
  - pytest configuration
  - Example tests with fixtures
  - Coverage reporting setup

- **Documentation**
  - Technical documentation structure
  - API documentation examples
  - Clean README template

## Using This Template

1. Create a new repository using this template
2. Clone your new repository
3. Make the following changes to customize for your project:

### Initial Setup

```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
uv pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Required Changes

1. Update `pyproject.toml`:
   - Change `name` to your project name
   - Update `description` and `authors`
   - Modify `packages` to point to your package name
   - Adjust dependencies as needed

2. Rename/modify source code:
   - Remove or replace the calculator example in `src/calculator/`
   - Create your own package structure under `src/`

3. Update documentation:
   - Modify this README.md for your project
   - Update or remove example documentation in `docs/`
   - Add your own documentation

4. Update tests:
   - Remove example calculator tests
   - Create your own tests in `tests/`
   - Update `conftest.py` with your fixtures

5. Update scripts:
   - Remove `example_calculation.py`
   - Add your own utility scripts as needed

6. Choose your license
   - This template is provided as MIT
   - You should choose and update the [LICENSE](.LICENSE) for your needs
   - Update `license` in `pyproject.toml` to match


### Example Code

The template includes a simple calculator package that demonstrates:

- Type hints and Pydantic models
- Custom exceptions
- History tracking
- Unit testing
- Pytest fixtures
- Documentation standards

You can run the example:
```bash
# Run tests
pytest

# Try the example script
python scripts/example_calculation.py
```

Review the example code to understand the conventions, then remove or replace it with your own package.

## Template Features in Detail

### Source Layout

```
project-name/
├── src/               # Main package directory
│   └── your_package/  # Your source code goes here
├── tests/             # Test directory
├── docs/              # Documentation
├── scripts/           # Utility scripts
└── notebooks/         # Jupyter notebooks (if needed)
```

### Quality Tools

- **black**: Code formatting
  - Line length: 88 characters
  - Configured in pyproject.toml

- **mypy**: Type checking
  - Strict type checking enabled
  - Pydantic plugin configured

- **isort**: Import sorting
  - Compatible with black
  - Structured import sections

- **ruff**: Fast linting
  - Configured to work with black
  - Common Python linting rules

- **pre-commit**: Automated checks
  - Runs before each commit
  - Ensures code quality

### Testing

- **pytest**: Testing framework
  - Example fixtures in conftest.py
  - Coverage reporting configured
  - Clear test organization

### Environment Management

- `.env.template` for configuration
- Virtual environment setup
- Dependency management in pyproject.toml

## Development Workflow

1. Create feature branch
2. Make changes
3. Run tests: `pytest`
4. Run pre-commit: `pre-commit run --all-files`
5. Commit and push
6. Create pull request

## Contributing

Contributions to improve this template are welcome! Please submit issues and pull requests on GitHub.

## License

This template is MIT licensed. See the [LICENSE](LICENSE) file for details.

## Credits

Created and maintained by [Your Name/Organization]. This template is designed to provide a solid foundation for Python projects while demonstrating best practices through working examples.
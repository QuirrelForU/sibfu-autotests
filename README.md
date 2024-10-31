# QA Automation Project

This repository is a QA Automation project for SibFU using Python 3.12, Pytest, and Playwright, managed with the UV package manager. It includes linters (`Ruff` and `MyPy`) and pre-commit hooks to maintain code quality.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- **Python 3.12**: [Download Python](https://www.python.org/downloads/)
- **UV Package Manager**: [UV Installation Guide](https://www.uv.dev/docs/installation)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Playwright Browsers**: Playwright manages browser installations. These will be installed during the setup.

> **Note**: Ensure `uv`, `git`, and `python` are added to your system's PATH.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/QuirrelForU/sibfu-autotests
   cd qa-automation-project
   ```

2. **Initialize UV and Install Dependencies**

   ```bash
   uv venv
   uv sync
   ```

3. **Set Up Pre-commit Hooks**

   ```bash
   pre-commit install
   ```

4. **Install Playwright Browsers**

   After installing Playwright via UV, install the necessary browsers:

   ```bash
   playwright install
   ```

## Running Tests

Execute the following command to run all tests:

```bash
pytest
```

For more verbose output:

```bash
pytest -v
```

## Project Structure

```
qa-automation-project/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_example.py
├── pages/
│   ├── __init__.py
│   └── example_page.py
├── pyproject.toml
├── .pre-commit-config.yaml
├── README.md
└── .gitignore
```

- **tests/**: Contains all your test cases.
- **pages/**: Page Object Models for Playwright.
- **conftest.py**: Configuration for pytest fixtures.
- **pyproject.toml**: Configuration for Ruff linter.
- **.pre-commit-config.yaml**: Pre-commit hooks configuration.
- **README.md**: Project documentation.
- **.gitignore**: Git ignore rules.


## License

This project is licensed under the [MIT License](LICENSE).

---


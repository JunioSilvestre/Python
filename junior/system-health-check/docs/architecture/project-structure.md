# Project Structure

## Overview

The `system-health-check` project follows a structured Python application layout designed to separate application code, tests, documentation, automation, configuration, and operational resources.

The structure follows common practices used in professional Python and DevOps projects.

---

## Directory Structure

```text
system-health-check/
│
├── .github/
│   └── workflows/
│
├── docs/
│   ├── architecture/
│   ├── decisions/
│   └── operations/
│
├── scripts/
│
├── src/
│   └── system_health_check/
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## `.github/`

Contains GitHub-specific configuration and automation.

### `.github/workflows/`

Contains GitHub Actions workflows.

These workflows will be responsible for automating tasks such as:

* Running automated tests
* Running code quality checks
* Running linting and formatting validation
* Building the Python package
* Validating pull requests
* Executing CI pipelines after Git pushes

Example future structure:

```text
.github/
└── workflows/
    ├── ci.yml
    └── release.yml
```

The application itself must not be placed inside this directory.

---

## `docs/`

Contains technical and operational documentation that is not appropriate for the main `README.md`.

The documentation is divided by responsibility.

```text
docs/
├── architecture/
├── decisions/
└── operations/
```

### `docs/architecture/`

Documents how the system is designed and organized.

Examples:

```text
docs/architecture/
├── project-structure.md
├── architecture.md
└── data-flow.md
```

Typical topics include:

* Application architecture
* Component responsibilities
* Data flow
* Project organization
* Dependencies between components
* Design principles

### `docs/decisions/`

Contains important technical decisions and their rationale.

This directory can be used to document decisions such as:

* Why `psutil` was selected
* Why the `src` layout is used
* Why a specific CLI approach was selected
* Why a particular logging strategy was adopted
* Why a dependency was intentionally avoided

Example:

```text
docs/decisions/
├── ADR-001-use-psutil.md
├── ADR-002-src-layout.md
└── ADR-003-cli-design.md
```

These documents should explain:

```text
Problem
    ↓
Options considered
    ↓
Decision
    ↓
Reasoning
    ↓
Consequences
```

### `docs/operations/`

Contains documentation required to install, operate, maintain, and troubleshoot the application.

Examples:

```text
docs/operations/
├── installation.md
├── configuration.md
├── troubleshooting.md
└── maintenance.md
```

Typical topics include:

* Installation
* Configuration
* Environment variables
* Execution
* Logging
* Troubleshooting
* Maintenance
* Operational procedures

---

## `scripts/`

Contains auxiliary scripts used to support development, maintenance, testing, or operational tasks.

Scripts in this directory are not the main application.

Examples:

```text
scripts/
├── setup.sh
├── clean.sh
└── development-check.sh
```

The distinction is important:

```text
src/
    → Application functionality

scripts/
    → Supporting automation
```

For example, a script that prepares a development environment belongs in `scripts/`.

A Python module responsible for checking system memory belongs in `src/system_health_check/`.

---

## `src/`

Contains the application's source code.

The `src` directory is intentionally separated from tests, documentation, and project configuration.

```text
src/
└── system_health_check/
```

The application package is:

```text
src/system_health_check/
```

This is where the actual System Health Check implementation will be developed.

Possible future structure:

```text
src/
└── system_health_check/
    ├── __init__.py
    ├── cli.py
    ├── cpu.py
    ├── memory.py
    ├── disk.py
    ├── network.py
    ├── processes.py
    ├── health.py
    └── logging.py
```

Each module should have a clear responsibility.

For example:

```text
cpu.py
    → CPU information

memory.py
    → Memory information

disk.py
    → Disk information

network.py
    → Network information

processes.py
    → Process information

health.py
    → Health evaluation

cli.py
    → Command-line interface
```

The application should not place tests, documentation, virtual environments, or generated files inside `src/`.

---

## `tests/`

Contains automated tests for the application.

```text
tests/
├── unit/
└── integration/
```

### `tests/unit/`

Contains unit tests.

Unit tests verify individual components independently.

Examples:

```text
tests/unit/
├── test_cpu.py
├── test_memory.py
├── test_disk.py
└── test_network.py
```

A unit test should ideally test one specific behavior without depending on unrelated components.

### `tests/integration/`

Contains integration tests.

Integration tests verify that multiple components work correctly together.

Example:

```text
tests/integration/
└── test_system_health_check.py
```

A simplified distinction is:

```text
Unit Test
    Component A
       ↓
    Expected result


Integration Test
    Component A
       ↓
    Component B
       ↓
    Component C
       ↓
    Expected system behavior
```

---

## `.gitignore`

Defines files and directories that should not be committed to Git.

Typical Python exclusions include:

```text
.venv/
__pycache__/
*.pyc
.pytest_cache/
.ruff_cache/
.env
```

The purpose is to prevent local environments, generated files, caches, secrets, and other unnecessary files from entering the repository.

The virtual environment is particularly important:

```text
.venv/
```

The environment belongs to the developer's machine.

The project configuration belongs in Git.

```text
Local machine
    └── .venv/

Git repository
    ├── pyproject.toml
    └── source code
```

Another developer should be able to clone the repository and recreate the environment from the project configuration.

---

## `pyproject.toml`

The `pyproject.toml` file is the central configuration file for this Python project.

It defines information such as:

* Project name
* Project version
* Python version requirement
* Runtime dependencies
* Development dependencies
* Package configuration
* Build configuration
* Pytest configuration
* Ruff configuration
* CLI entry points

For this project, it also defines the application command:

```text
system-health-check
```

and associates it with the Python CLI entry point.

The objective is to keep project configuration centralized instead of distributing configuration across multiple unrelated files.

---

## `README.md`

The `README.md` file is the primary entry point for anyone visiting the repository.

It should answer the most important questions quickly:

```text
What is this project?
        ↓
Why does it exist?
        ↓
What does it do?
        ↓
What are the requirements?
        ↓
How do I install it?
        ↓
How do I run it?
        ↓
How do I test it?
        ↓
How is it organized?
```

The README should provide enough information for a developer to understand and use the project without reading the entire source code.

Detailed technical and operational information should be moved into `docs/`.

---

## Separation of Responsibilities

The project follows this general principle:

```text
README.md
    → Introduction and quick usage

docs/
    → Detailed documentation

src/
    → Application code

tests/
    → Automated verification

scripts/
    → Supporting automation

.github/
    → Repository automation

pyproject.toml
    → Project configuration

.gitignore
    → Git exclusions
```

This separation prevents unrelated concerns from being mixed together.

---

## Development Principle

Each directory should have a clear responsibility.

A developer should be able to answer:

```text
Where is the application code?
    → src/

Where are the tests?
    → tests/

Where is the documentation?
    → docs/

Where are development scripts?
    → scripts/

Where is CI/CD configured?
    → .github/workflows/

Where are Python dependencies configured?
    → pyproject.toml/

Where is the project introduction?
    → README.md
```

This structure provides a predictable foundation for future development as the project grows.

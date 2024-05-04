# xUnit

A working and iteratively worked example of the xUnit testing tool described in Kent
Beck's "Test-Driven Development by Example" implemented in more modern Python code. The
intention is that you can step through the git history of the project to explore the
evolution of the codebase.

## Installation

Install the project in editable mode with development dependencies, such as `pytest-watcher`.

```shell
pip install -e '.[dev]'
```

## Usage

During development, you can keep running the tests with the following command, for
example:

```shell
ptw . --runner python tests/system/test_case_test.py --clear
```

That initiates `pytest-watcher` which will watch for changes in the project
directory (`.`) and invoke the given command.

## Unlicense

This is free and unencumbered software released into the public domain.


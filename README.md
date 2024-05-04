# xUnit

A working and iteratively worked example of the xUnit testing tool described in Kent
Beck's "Test-Driven Development by Example" implemented in more modern Python code. The
intention is that you can step through the git history of the project to explore the
evolution of the codebase.

## Installation

Install the project in editable mode

```shell
pip install -e .
```

Install `pytest-watcher` to easily execute a command whenever a change has occurred.

## Usage

During development, you can keep running the tests with the following command, for
example:

```shell
ptw . --runner python tests/system/test_case_test.py --clear
```

## Unlicense

This is free and unencumbered software released into the public domain.


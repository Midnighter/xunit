# xUnit

| |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/xunit.svg)](https://pypi.org/project/xunit/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/xunit.svg)](https://pypi.org/project/xunit/) [![Documentation](https://readthedocs.org/projects/xunit/badge/?version=latest)](https://xunit.readthedocs.io/en/latest/?badge=latest)                                                                                                                                                                         |
| Meta | [![MIT](https://img.shields.io/pypi/l/xunit.svg)](LICENSE) [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](.github/CODE_OF_CONDUCT.md) [![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)                                                                                                                                                          |
| Automation | [![GitHub Workflow](https://github.com/Midnighter/xunit/workflows/CI-CD/badge.svg)](https://github.com/Midnighter/xunit/workflows/CI-CD) [![Code Coverage](https://codecov.io/gh/Midnighter/xunit/branch/master/graph/badge.svg)](https://codecov.io/gh/Midnighter/xunit) |

A working example of the xUnit testing tool described in Kent Beck's "Test-Driven Development by Example".

## Installation

Install the project in editable mode

```shell
pip install -e .
```

Install `pytest-watcher` to easily execute a command whenever a change has occurred.

## Usage

During development, you can keep running the tests with the following command, for example:

```shell
ptw . --runner python tests/unit/test_was_run.py
```

## Copyright

* Copyright © 2024 Moritz E. Beber.
* Free software distributed under the [MIT License](../LICENSE).


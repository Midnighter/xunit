from .test_case import TestCase
from .test_result import TestResult


class TestSuite:
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.tests = []

    def add(self, test: TestCase) -> None:
        self.tests.append(test)

    def run(self, result: TestResult) -> None:
        for test in self.tests:
            test.run(result)

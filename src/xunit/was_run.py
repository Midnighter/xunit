from .test_case import TestCase


class WasRun(TestCase):
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(name=name, **kwargs)
        self.log = []

    def set_up(self) -> None:
        self.log.append("setup")

    def test_method(self) -> None:
        self.log.append("test_method")

    def test_broken_method(self) -> None:
        self.log.append("test_broken_method")
        raise AssertionError("Broken test.")

    def tear_down(self) -> None:
        self.log.append("teardown")

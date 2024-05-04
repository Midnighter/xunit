from .test_result import TestResult


class TestCase:
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def set_up(self) -> None:
        pass

    def run(self, result: TestResult) -> None:
        result.test_started()
        try:
            self.set_up()
        except Exception:
            result.setup_failed()
            self.tear_down()
            return
        try:
            getattr(self, self.name)()
        except Exception:
            result.test_failed()
        finally:
            self.tear_down()

    def tear_down(self) -> None:
        pass

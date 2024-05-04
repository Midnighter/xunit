class TestResult:
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.run_count = 0
        self.error_count = 0
        self.setup_error_count = 0

    def setup_failed(self) -> None:
        self.setup_error_count += 1

    def test_started(self) -> None:
        self.run_count += 1

    def test_failed(self) -> None:
        self.error_count += 1

    def summary(self) -> str:
        return (
            f"{self.run_count} run, {self.error_count} failed, "
            f"{self.setup_error_count} setup error"
        )

from xunit import TestCase, TestResult, TestSuite, WasRun


class TestCaseFailedSetupTest(TestCase):
    def set_up(self) -> None:
        raise RuntimeError("Failed setup.")

    def test_stub(self) -> None:
        pass


class TestCaseTest(TestCase):
    def set_up(self) -> None:
        self.result = TestResult()

    def test_template_method(self) -> None:
        test = WasRun("test_method")
        test.run(self.result)
        assert test.log == ["setup", "test_method", "teardown"]

    def test_failed_teardown(self) -> None:
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert test.log == ["setup", "test_broken_method", "teardown"]

    def test_result(self) -> None:
        test = WasRun("test_method")
        test.run(self.result)
        assert self.result.summary() == "1 run, 0 failed, 0 setup error"

    def test_failed_result(self) -> None:
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert self.result.summary() == "1 run, 1 failed, 0 setup error"

    def test_failed_result_formatting(self) -> None:
        self.result.test_started()
        self.result.test_failed()
        assert self.result.summary() == "1 run, 1 failed, 0 setup error"

    def test_suite(self) -> None:
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        suite.run(self.result)
        assert self.result.summary() == "2 run, 1 failed, 0 setup error"

    def test_failed_setup(self) -> None:
        suite = TestSuite()
        suite.add(TestCaseFailedSetupTest("test_stub"))
        suite.run(self.result)
        assert self.result.summary() == "1 run, 0 failed, 1 setup error"


if __name__ == "__main__":
    suite = TestSuite()
    suite.add(TestCaseTest("test_template_method"))
    suite.add(TestCaseTest("test_result"))
    suite.add(TestCaseTest("test_failed_teardown"))
    suite.add(TestCaseTest("test_failed_result_formatting"))
    suite.add(TestCaseTest("test_failed_result"))
    suite.add(TestCaseTest("test_suite"))
    suite.add(TestCaseTest("test_failed_setup"))
    result = TestResult()
    suite.run(result)
    print(result.summary())

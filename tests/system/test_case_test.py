# MIT License
#
# Copyright (c) 2024 Moritz E. Beber
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


""""""


from xunit import WasRun, TestCase, TestResult


class TestCaseTest(TestCase):

    def test_template_method(self) -> None:
        test = WasRun("test_method")
        test.run()
        assert test.log == ["setup", "test_method", "teardown"]

    def test_result(self) -> None:
        test = WasRun("test_method")
        result = test.run()
        assert result.summary() == "1 run, 0 failed"

    def test_failed_result(self) -> None:
        test = WasRun("test_broken_method")
        result = test.run()
        assert result.summary() == "1 run, 1 failed"

    def test_failed_result_formatting(self) -> None:
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert result.summary() == "1 run, 1 failed"


if __name__ == '__main__':
    print(TestCaseTest("test_template_method").run().summary())
    print(TestCaseTest("test_result").run().summary())
    print(TestCaseTest("test_failed_result_formatting").run().summary())
    print(TestCaseTest("test_failed_result").run().summary())

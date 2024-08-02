import pytest


class Test1:

    def setup_class(self):
        raise Exception("Setup Error")

    @pytest.mark.skip
    def test_report_pass(self):
        assert True

    @pytest.mark.parametrize("p",
                             [(1,), (2,)],
                             ids=["input_1", "input_2"])
    def test_report_fail(self, p):
        assert False

    def test_report_error(self):
        raise Exception("Error")


class Test2:

    def test_report_pass(self):
        assert True

    @pytest.mark.parametrize("p",
                             [(1,), (2,)],
                             ids=["input_1", "input_2"])
    def test_report_fail(self, p):
        assert False

    def test_report_error(self):
        raise Exception("Error")


class Test3:

    def teardown_class(self):
        raise Exception("Teardown Error")

    def test_report_pass(self):
        assert True

    @pytest.mark.parametrize("p",
                             [(1,), (2,)],
                             ids=["input_1", "input_2"])
    def test_report_fail(self, p):
        assert False

    def test_report_error(self):
        raise Exception("Error")

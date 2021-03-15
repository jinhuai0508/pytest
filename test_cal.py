import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        return datas


class TestCalc:

    def setup_method(self):
        print("\nsetup_method:调用方法开始计算")

    def teardown_method(self):
        print("\nteardown_method:方法调用完成计算结束")

    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a,b,expect", get_datas()["add"])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        print(result)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()["sub"])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        print(result)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()["mul"])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        print(result)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datas()["div"])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        print(result)
        assert result == expect

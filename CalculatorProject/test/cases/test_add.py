import allure
import pytest

from CalculatorProject.Scripts.calculator import Calculator
from CalculatorProject.utills.utills import get_add_data


@allure.feature("加法模块")
class TestAdd:
    def setup_class(self):
        self.calculator = Calculator()

    def teardown_class(self):
        print("【结束测试】")

    def setup(self):
        print("【开始计算】")

    def teardown(self):
        print("【结束计算】")

    @allure.story("两个数非空")
    @allure.title("{story}")
    @pytest.mark.parametrize("story, a, b, expected", get_add_data("../../data/add.xlsx"))
    def test_add(self, story, a, b, expected):
        assert self.calculator.add(a, b) == expected

    @allure.story("一个输入为空")
    @allure.title("【类型】输入为空，给出提示信息")
    def test_add_empty1(self):
        assert self.calculator.add("", 20.93) == "参数大小超出范围"

    @allure.story("一个输入为空")
    @allure.title("【类型】输入为空，给出提示信息")
    def test_add_empty2(self):
        assert self.calculator.add(-3, "") == "参数大小超出范围"

    @allure.story("一个输入为空格")
    @allure.title("【类型】输入空格，给出提示信息")
    def test_add_space1(self):
        assert self.calculator.add(" ", 3.14) == "参数大小超出范围"

    @allure.story("一个输入为空格")
    @allure.title("【类型】输入空格，给出提示信息")
    def test_add_space2(self):
        assert self.calculator.add(-90, " ") == "参数大小超出范围"
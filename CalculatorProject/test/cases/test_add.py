import allure
import pytest

from CalculatorProject.test.base.base import Base
from CalculatorProject.utills.utills import get_add_data


@allure.feature("加法模块")
class TestAdd(Base):

    @allure.story("【正向用例】【P0】整数相加")
    @allure.title("{title}")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.P0
    @pytest.mark.right
    @pytest.mark.parametrize("title, a, b, expected", get_add_data("../../data/add.xlsx", "【正向】2个整数相加，结果计算正确"))
    def test_add_001(self, title, a, b, expected):
        with allure.step(f"计算：{a} + {b}:"):
            result = self.calculator.add(a, b)
            self.log.info(f"计算：{a} + {b}，预期结果：{expected}，实际结果：{result}")
        with allure.step(f"断言测试结果【{result}】与预期结果【{expected}】是否相等"):
            assert result == expected

    @allure.story("【正向用例】【P0】浮点数相加")
    @allure.title("{title}")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.P0
    @pytest.mark.right
    @pytest.mark.parametrize("title, a, b, expected", get_add_data("../../data/add.xlsx", "【正向】2个浮点数相加，结果计算正确"))
    def test_add_002(self, title, a, b, expected):
        with allure.step(f"计算：{a} + {b}:"):
            result = self.calculator.add(a, b)
            self.log.info(f"计算：{a} + {b}，预期结果：{expected}，实际结果：{result}")
        with allure.step(f"断言测试结果【{result}】与预期结果【{expected}】是否相等"):
            assert result == expected

    @allure.story("【正向用例】【P0】整数与浮点数相加")
    @allure.title("{title}")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.P0
    @pytest.mark.right
    @pytest.mark.parametrize("title, a, b, expected", get_add_data("../../data/add.xlsx", "【正向】整数与浮点数相加，结果计算正确"))
    def test_add_003(self, title, a, b, expected):
        with allure.step(f"计算：{a} + {b}:"):
            result = self.calculator.add(a, b)
            self.log.info(f"计算：{a} + {b}，预期结果：{expected}，实际结果：{result}")
        with allure.step(f"断言测试结果【{result}】与预期结果【{expected}】是否相等"):
            assert result == expected

    @allure.story("【正向用例】【P1】有效边界值相加")
    @allure.title("{title}")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.P1
    @pytest.mark.right
    @pytest.mark.parametrize("title, a, b, expected", get_add_data("../../data/add.xlsx", "【边界】有效边界值相加，结果计算正确"))
    def test_add_004(self, title, a, b, expected):
        with allure.step(f"计算：{a} + {b}:"):
            result = self.calculator.add(a, b)
            self.log.info(f"计算：{a} + {b}，预期结果：{expected}，实际结果：{result}")
        with allure.step(f"断言测试结果【{result}】与预期结果【{expected}】是否相等"):
            assert result == expected

    @allure.story("【反向用例】【P1】无效边界值相加")
    @allure.title("{title}")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.P1
    @pytest.mark.wrong
    @pytest.mark.parametrize("title, a, b, expected", get_add_data("../../data/add.xlsx", "【边界】无效边界值相加，给出提示信息"))
    def test_add_005(self, title, a, b, expected):
        with allure.step(f"计算：{a} + {b}:"):
            result = self.calculator.add(a, b)
            self.log.info(f"计算：{a} + {b}，预期结果：{expected}，实际结果：{result}")
        with allure.step(f"断言测试结果【{result}】与预期结果【{expected}】是否相等"):
            assert result == expected

    @allure.story("【反向用例】【P1】输入中文")
    @allure.title("{title}")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.P1
    @pytest.mark.wrong
    @pytest.mark.parametrize("title, a, b, expected", get_add_data("../../data/add.xlsx", "【类型】输入中文，给出提示信息"))
    def test_add_006(self, title, a, b, expected):
        try:
            with allure.step(f"计算：{a} + {b}:"):
                result = self.calculator.add(a, b)
        except TypeError as e:
            result = "TypeError"
        with allure.step(f"断言测试结果【{result}】与预期结果【{expected}】是否相等"):
            self.log.info(f"计算：{a} + {b}，预期结果：{expected}，实际结果：{result}")
            assert result == expected

    @allure.story("【反向用例】【P1】输入英文")
    @allure.title("{title}")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.P1
    @pytest.mark.wrong
    @pytest.mark.parametrize("title, a, b, expected", get_add_data("../../data/add.xlsx", "【类型】输入英文，给出提示信息"))
    def test_add_007(self, title, a, b, expected):
        try:
            with allure.step(f"计算：{a} + {b}:"):
                result = self.calculator.add(a, b)
        except TypeError as e:
            result = "TypeError"
        with allure.step(f"断言测试结果【{result}】与预期结果【{expected}】是否相等"):
            self.log.info(f"计算：{a} + {b}，预期结果：{expected}，实际结果：{result}")
            assert result == expected

    @allure.story("【反向用例】【P1】输入特殊字符")
    @allure.title("{title}")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.P1
    @pytest.mark.wrong
    @pytest.mark.parametrize("title, a, b, expected", get_add_data("../../data/add.xlsx", "【类型】输入特殊字符，给出提示信息"))
    def test_add_008(self, title, a, b, expected):
        try:
            with allure.step(f"计算：{a} + {b}:"):
                result = self.calculator.add(a, b)
        except TypeError as e:
            result = "TypeError"
        with allure.step(f"断言测试结果【{result}】与预期结果【{expected}】是否相等"):
            self.log.info(f"计算：{a} + {b}，预期结果：{expected}，实际结果：{result}")
            assert result == expected

    @allure.story("【反向用例】【P2】输入为空")
    @allure.title("{title}")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.P2
    @pytest.mark.wrong
    @pytest.mark.parametrize("title, a, b, expected", get_add_data("../../data/add.xlsx", "【类型】输入为空，给出提示信息"))
    def test_add_009(self, title, a, b, expected):
        try:
            with allure.step(f"计算：{a} + {b}:"):
                result = self.calculator.add(a, b)
        except TypeError as e:
            result = "TypeError"
        with allure.step(f"断言测试结果【{result}】与预期结果【{expected}】是否相等"):
            self.log.info(f"计算：{a} + {b}，预期结果：{expected}，实际结果：{result}")
            assert result == expected

    @allure.story("【反向用例】【P2】输入空格")
    @allure.title("{title}")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.P2
    @pytest.mark.wrong
    @pytest.mark.parametrize("title, a, b, expected", get_add_data("../../data/add.xlsx", "【类型】输入空格，给出提示信息"))
    def test_add_010(self, title, a, b, expected):
        try:
            with allure.step(f"计算：{a} + {b}:"):
                result = self.calculator.add(a, b)
        except TypeError as e:
            result = "TypeError"
        with allure.step(f"断言测试结果【{result}】与预期结果【{expected}】是否相等"):
            self.log.info(f"计算：{a} + {b}，预期结果：{expected}，实际结果：{result}")
            assert result == expected

import logging
from time import sleep

import allure
import pytest

from calculator_project_2.test.base.base import Base
from calculator_project_2.utills.utill import Utills


class TestAdd(Base):
    @pytest.mark.P0
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=5)
    @pytest.mark.parametrize("a, b, expect", Utills.get_datas().get("add").get("P0").get("datas"),
                             ids=Utills.get_datas().get("add").get("P0").get("ids"))
    def test_add_p0(self, a, b, expect):
        sleep(0.5)
        print()
        print(f"{a} + {b} = {expect}")
        logging.info(f"{a} + {b} = {expect}")
        with allure.step("第一步"):
            result = self.calculator.add(a, b)
        with allure.step("第二步"):
            assert result == expect

    @pytest.mark.P1_1
    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=5)
    @pytest.mark.parametrize("a, b, expect", Utills.get_datas().get("add").get("P1_1").get("datas"),
                             ids=Utills.get_datas().get("add").get("P1_1").get("ids"))
    def test_add_p1_1(self, a, b, expect):
        sleep(0.5)
        print()
        print(f"{a} + {b} = {expect}")
        logging.info(f"{a} + {b} = {expect}")
        with allure.step("第一步"):
            result = self.calculator.add(a, b)
        with allure.step("第二步"):
            assert result == expect

    @pytest.mark.P1_2
    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=5)
    @pytest.mark.parametrize("a, b, expect", Utills.get_datas().get("add").get("P1_2").get("datas"),
                             ids=Utills.get_datas().get("add").get("P1_2").get("ids"))
    def test_add_p1_2(self, a, b, expect):
        sleep(0.5)
        print()
        print(f"{a} + {b} = {expect}")
        logging.info(f"{a} + {b} = {expect}")
        with allure.step("第一步"):
            with pytest.raises(eval(expect)) as f:
                result = self.calculator.add(a, b)
        with allure.step("第二步"):
            assert f.type == eval(expect)

    @pytest.mark.P2
    @pytest.mark.run(order=2)
    @pytest.mark.flaky(reruns=5)
    @pytest.mark.parametrize("a, b, expect", Utills.get_datas().get("add").get("P2").get("datas"),
                             ids=Utills.get_datas().get("add").get("P2").get("ids"))
    def test_add_p2(self, a, b, expect):
        sleep(0.5)
        print()
        print(f"{a} + {b} = {expect}")
        logging.info(f"{a} + {b} = {expect}")
        with allure.step("第一步"):
            with pytest.raises(eval(expect)) as f:
                result = self.calculator.add(a, b)
        with allure.step("第二步"):
            assert f.type == eval(expect)

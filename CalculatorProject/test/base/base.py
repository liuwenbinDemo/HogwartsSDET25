import logging

from CalculatorProject.Scripts.calculator import Calculator
from CalculatorProject.logs.log_utill import logger


class Base:
    def setup_class(self):
        self.calculator = Calculator()
        self.log = logger

    def teardown_class(self):
        print("【结束测试】")

    def setup(self):
        print("【开始计算】")

    def teardown(self):
        print("【结束计算】")
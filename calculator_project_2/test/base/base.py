from calculator_project_2.scripts.calculator import Calculator


class Base:
    def setup_class(self):
        self.calculator = Calculator()

    def setup_method(self):
        print("开始计算：")


    def teardown_method(self):
        print("计算结束！")
import os
import yaml


class Utills:
    BASEPATH = os.path.dirname(__file__)
    DATAPATH = os.path.join(BASEPATH, "..", "datas", "data.yaml")
    @staticmethod
    def get_datas():
        """

        :param cal: 运算类型（add or div）
        :param level: 用例等级（P0,P1_1,P1_2,P2）
        :return: datas及ids
        """
        with open(Utills.DATAPATH, "r", encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas


# print(Utills.get_datas("add", "P0"))
import pytest
import allure
from day05.P03_pytest框架.apirun6版本.Utils.yamlfileread import YamlFileRead


class TestRunner():
    # todo 1 读取yaml文件数据
    yaml_case_data = YamlFileRead().read_yaml(
        r"E:\华测讲师笔记\hctestcode\3.API--test\接口项目new\day05\P03_pytest框架\apirun6版本\data\yaml\api_yaml_V5.yaml")

    # todo 2  参数化
    @pytest.mark.parametrize("case_data", yaml_case_data)
    def test_case_execute(self, case_data):
        print("当前的测试用例数据：", case_data)

        # todo 3 动态生成当前的测试标题
        allure.dynamic.title(case_data["caseName"])

        # todo 4 基于用例步骤进行执行
        try:
            pass
        finally:
            print("当前用例执行完成")

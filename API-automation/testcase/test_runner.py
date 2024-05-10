import allure
import pytest
import json
from common.FileYamlRead import FileYamlRead
from api_keyword.api_keyword import ApiKeys


class TestCase:
    # 从文件中获取CaseData
    # 1.获取接口四要素 2.发送请求 3.获取响应数据 4.断言
    AllCaseData = FileYamlRead.read_yaml()
    ak = ApiKeys()
    all_value = {}

    def __dynamic_title(self, CaseData):
        #  TODO -----动态生成测试标题
        if CaseData["caseName"] is not None:
            # 将获取到的ID和caseName拼接起来，为一个测试标题
            caseName = f"CASEID:{CaseData['id']}---{CaseData['caseName']}"
            allure.dynamic.title(caseName)

        if CaseData["storyName"] is not None:
            # 获取用例里面的小模块名称storyName
            allure.dynamic.story(CaseData["storyName"])

        if CaseData["featureName"] is not None:
            # 获取用例里面的大模块名称featureName
            allure.dynamic.feature(CaseData["featureName"])

        if CaseData["remark"] is not None:
            # 动态获取用例的备注信息
            allure.dynamic.description(CaseData["remark"])

        if CaseData["rank"] is not None:
            # 动态获取用例的级别信息
            allure.dynamic.severity(CaseData["rank"])

    def __json_extraction(self, CaseData, res):
        """
        提取响应之后的数据
        :param CaseData: 当前的Case,获取需要提取数据的字段：jsonExData
        :param res: 响应得到的对应的结果
        :return:
        """
        try:
            if CaseData["jsonExData"]:
                Exdata = eval(CaseData["jsonExData"])
                print(type(Exdata))
                print("需要提取的数据：>>>", Exdata)
                for key, value in Exdata.items():
                    # 通过已经封装的api-keyword中的get_data_from_response方法获取具体数据
                    new_value = self.ak.get_data_from_response(res.json(), value)
                    self.all_value.update({key: new_value})
                    print("响应提取出来的数据为：", self.all_value)
            else:
                print("需要提取的数据为空")
        except Exception:
            print("检查数据格式的正确性")

    def __sql_extraction(self,CaseData):
        """
        从数据库里面提取数据
        :param CaseData: 当前的Case,获取的是需要提取数据的字段：sqlExData
        :return:
        """
        try:
            if CaseData["sqlExData"]:
                Exdata = eval(CaseData["sqlExData"])
                print(type(Exdata))
                print("需要提取的数据：>>>", Exdata)
                for key, value in Exdata.items():
                    # 通过对应的sql语句获取数据
                    new_value = self.ak.get_data_from_database(value)
                    self.all_value.update({key: new_value})
                    print("sql-提取出来的数据为：", self.all_value)
            else:
                print("sql-需要提取的数据为空")
        except Exception:
            print("sql-检查数据格式的正确性")



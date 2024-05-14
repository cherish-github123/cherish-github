import allure
import pytest
import json
from common.FileYamlRead import FileYamlRead
from common.FileExcelRead import FileExcelRead
from api_keyword.api_keyword import ApiKeys
from config import *


class TestCase:
    # 从excel文件中获取CaseData
    CaseData = FileExcelRead.read_excel()
    # 1.获取接口四要素 2.发送请求 3.获取响应数据 4.断言

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


    @pytest.mark.parametrize("CaseData",CaseData)
    def testcase(self,CaseData):
        # 调用动态生成测试标题函数
        global res
        self.__dynamic_title(CaseData)
        # 文件读取后，需要获取接口的四要素url、params、header、data,获取出来的都是字符串格式的，需要转换为字典格式
        # TODO eval()方法是将字符串格式的字典转为字典格式
        try:
            # 接口请求四要素
            dict_data={"url":CaseData["url"]+CaseData["path"],
                       "params":eval(CaseData["params"]),
                       "headers":eval(CaseData["headers"]),
                       "data":eval(CaseData["data"])}
            # 发送请求
            if CaseData["method"]=="Get":
                res=self.ak.get(url=dict_data["url"],params=dict_data["params"])

            elif CaseData["method"]=="post":
                 if CaseData["type"] == "json":
                    # 判断接口参数的格式为json，是json格式，需要使用json.dumps()方法将参数data转换为json格式,参数放在json中
                    dict_data["data"] = json.dumps(dict_data["data"])
                    res=self.ak.post(url=dict_data["url"],params=dict_data["params"],json=dict_data["data"])
                 else:
                     # 如果接口的参数不是json格式，直接使用data参数发送请求
                     res=self.ak.post(url=dict_data["url"],params=dict_data["params"],data=dict_data["data"])
            else:
                print("请检查请求方式的正确性")

        except Exception:
            value= REQUEST_ERROR

        # 断言
        try:
            actual_value=self.ak.get_data_from_response(res.json(),CaseData["actualResult"])
        except Exception:
            value=MSG_DATA_ERROR
        else:
            if actual_value==CaseData["expectResult"]:
                value=ASSERT_PASS
            else:
                value=ASSERT_FAIL















import allure
import  pytest
import json
from common.FileYamlRead import FileYamlRead
from api_keyword.api_keyword import ApiKeys


class TestCase:
    # 从文件中获取CaseData
    # 1.获取接口四要素 2.发送请求 3.获取响应数据 4.断言
    AllCaseData=FileYamlRead.read_yaml()
    ak=ApiKeys()


    def __dynamic_title(self,CaseData):
        # 动态生成测试标题
        if CaseData["caseName"] is not None:
            # 将获取到的ID和caseName拼接起来，为一个测试标题
            caseName=f"CASEID:{CaseData['id']}---{CaseData['caseName']}"
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






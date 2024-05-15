import allure
import pytest
import json

from jinja2 import Template   # 变量渲染

from common.FileYamlRead import FileYamlRead
from common.FileExcelRead import FileExcelRead
from api_keyword.api_keyword import ApiKeys
from config import *


class TestCase:
    # 从excel文件中获取AllCaseData,是excel的每一行数据
    AllCaseData = FileExcelRead.read_excel()
    # 1.获取接口四要素 2.发送请求 3.获取响应数据 4.断言
    ak = ApiKeys()
    # 定义一个空字典
    all_value = {}

    def __dynamic_title(self, CaseData):
        """
        :param CaseData: 当前的case,就是excel文件中的每一行数据
        :return:
        """
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
        提取响应之后的数据,可以提取多个数据
        :param CaseData: 当前的Case,获取需要提取数据的字段：文件中是jsonExData（第三个excel文件）{"VAR_TOKEN":"$..data.token","MSG":"$.msg"}
        :param res: 响应得到的对应的结果
        :return:
        """
        try:
            if CaseData["jsonExData"]:
                # 判断jsonExdata的值不为空时，再进行提取
                Exdata = eval(CaseData["jsonExData"])
                print(type(Exdata))
                print("需要提取的数据：>>>>>>", Exdata)
                for key, value in Exdata.items():     # 遍历字典中的键值对
                    # 通过已经封装的api-keyword中的get_data_from_response方法获取具体数据，value是json path表达式，new_value是json path提取后具体的数据
                    new_value = self.ak.get_data_from_response(res.json(), value)
                    print("new_value的值：",new_value)
                    self.all_value.update({key: new_value})
                    print("响应提取出来的数据为：", self.all_value)   # 结果：{'VAR_TOKEN': 'bd7aaca540b50cc6093e638c772381e1', 'MSG': '登录成功'}
            else:
                print("需要提取的数据为空")
        except Exception:
            print("检查数据格式的正确性")

    def __sql_extraction(self,CaseData):
        """
        从数据库里面提取数据
        :param CaseData: 当前的Case,获取的是需要提取数据的字段：sqlExData,{"name":"SELECT username FROM sxo_user WHERE username='hami'","id":"SELECT id FROM sxo_user WHERE username='hami'"}
        :return:
        """
        try:
            if CaseData["sqlExData"]:
                Exdata = eval(CaseData["sqlExData"])
                print(type(Exdata))
                print("文件中需要提取的数据sql：>>>", Exdata)
                for key, value in Exdata.items():
                    # 通过对应的sql语句获取数据,value是从文件中获取的sql语句，new_value是执行sql语句后得到的具体数据
                    new_value = self.ak.get_data_from_database(value)
                    self.all_value.update({key: new_value})
                    print("sql-提取出来的数据为：", self.all_value)
            else:
                print("sql-需要提取的数据为空")
        except Exception:
            print("sql-检查数据格式的正确性")

    def __sql_assertion(self,CaseData):
        # 数据库断言
        res=True   # 如果有用例不需要断言，则默认为True
        if CaseData["sqlAssertData"] and CaseData["sqlExpectResult"]:
                # 判断excel文件中sqlAssertData和sqlExpectData的值不为空时，再进行断言
                realityData=eval(CaseData["sqlAssertData"])
                expectData=json.loads(CaseData["sqlExpectResult"])
                # 定义一个空字典，用来存放实际结果
                reality_value={}
                for key,value in realityData.items():
                    # value是从文件中获取到的sql语句，new_value是执行sql之后得到的具体数据
                    new_value=self.ak.get_data_from_database(value)
                    reality_value.update({key:new_value})
                if expectData!=reality_value:
                    res=False
        return res



    @pytest.mark.parametrize("CaseData",AllCaseData)
    def testcase(self, CaseData): # Casedata是字典格式的，是excel文件的每一行数据
        # 调用动态生成测试标题函数
        self.__dynamic_title(CaseData)
        """
        这里用到变量渲染，将变量渲染到用例的数据中，然后进行测试(有点像格式化)
        Template(str(CaseData)),从文件中获取的CaseData是字典格式的，Template方法只能处理字符串格式的，所以先把字典格式的转换为字符串格式，字符串格式才能使用格式化
        render(self.all_value)，是从字典中获取的变量的具体值，然后渲染到用例数据
        eval()方法，当用例渲染完成后，再将字符串格式的用例数据转为字典格式
        使用场景：例如有一个URL里面需要使用token的值，token是从响应结果中获取的，那么可以在URL中使用{{token}},然后使用变量渲染的方法将token的值给到token变量中
        """
        CaseData=eval(Template(str(CaseData))).render(self.all_value)

        # 写入excel文件的行和列
        row=CaseData["id"]
        column=11

        # 初始化对应的值
        res=None
        actual_value=None
        value=None

        # 文件读取后，需要获取接口的四要素url、params、header、data,获取出来的都是字符串格式的，需要转换为字典格式
        # TODO eval()方法是将字符串格式的字典转为字典格式
        try:
            # 接口请求四要素,dict_data是请求参数字典，将接口四要素进行封装
            dict_data={"url":CaseData["url"]+CaseData["path"],
                       "params":eval(CaseData["params"]),
                       "headers":eval(CaseData["headers"]),
                       "data":eval(CaseData["data"])}
            # 发送请求
            if CaseData["type"] == "json":
                # 判断接口参数的格式为json，是json格式，需要使用json.dumps()方法将参数data转换为json格式,参数放在json中
                dict_data["data"] = json.dumps(dict_data["data"])

        except Exception:
            value= REQUEST_ERROR
            # 将结果写入excel文件
            FileExcelRead.write_excel(row=row,column=column,value=value)
        else:
            # 得到对应的响应结果，反射
            res = getattr(self.ak,CaseData["method"])(**dict_data)

            # ------------------------------数据库提取数据------------------------
        self.__sql_extraction(CaseData)

        # json path断言
        try:
            # 实际结果,提取数据：
            actual_value=self.ak.get_data_from_response(res.json(),CaseData["actualResult"])
        except Exception:
            # 提取数据失败
            value=MSG_DATA_ERROR
            FileExcelRead.write_excel(row=row, column=column, value=value)
        else:
            # 判断实际结果和预期结果是否一致，并写入文件
            if actual_value==CaseData["expectResult"]:
                value=ASSERT_PASS   # 断言成功
                # api_key中的get_data_from_response一次只能提取一个数据，如果需要提取多个数据，需要使用__json_extraction()方法
                self.__json_extraction(CaseData,res)
            else:
                value=ASSERT_FAIL   # 断言失败
            # 不管是断言成功或者失败，都需要将结果写入excel文件
            FileExcelRead.write_excel(row=row, column=column, value=value)
        finally:
            assert actual_value == CaseData["expectResult"], value















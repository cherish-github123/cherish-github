# DS_022 登录接口-使用用户名能正确的登录用户
import copy

import allure
import jsonpath
import pytest
import requests
from api_allframe_yaml.apirun8版本.keywords.keyword import Keyword
import allure
from api_allframe_yaml.apirun8版本.Utils.VarRender import var_render
from api_allframe_yaml.apirun8版本.Global_var.global_var import GlobalVar
from api_allframe_yaml.apirun8版本.Utils.yamlfileread import YamlFileRead
from api_allframe_yaml.apirun8版本.Utils.dynamictitle import dynamic_title



class TestRunner():
    # TODO 1.读取yaml文件，获取用例信息,每一条用例信息就是一个字典
    case_info = YamlFileRead().read_yaml(r"E:\华测讲师笔记\hctestcode\apitestframe-new\api_allframe_yaml\apirun8版本\data\yaml\登录接口测试用例.yaml")

    # TODO 2.进行参数化
    @pytest.mark.parametrize("caseinfo", case_info)
    def test_case_execute(self, caseinfo):
        global key_function
        keyword = Keyword()
        print("当前的测试数据yaml：",
              caseinfo)  # {'desc': 'test-登录测试用例', 'steps': [{'发送Post请求': {'DATA': {'accounts': '{{username}}', 'pwd': '{{password}}', 'type': 'u...nData'}}, {'通过JSONPATH提取数据-TOKEN': {'EXVALUE': '$..token', 'INDEX': 0, 'VARNAME': 'msg_token', '关键字': 'ex_jsonData'}}]}

        # TODO 3.动态生成当前用例的测试标题
        # allure.dynamic.title(caseinfo["desc"])
        dynamic_title(caseinfo)   # 调用生成测试标题的方法，将读取出来的测试数据传入函数
        # TODO 4.根据yaml文件中的步骤进行执行
        try:
            # 获取测试步骤，并且遍历每一步
            steps = caseinfo.get("steps", None)
            for step in steps:  # 获取到的step是一个字典
                # 获取到每一步的步骤名称和值
                step_name = list(step.keys())[0]
                step_value = list(step.values())[0]
                print(f"开始执行步骤：{step_name}-{step_value}")

                # TODO 进行变量渲染
                # 先将yaml数据的全局变量获取出来，使用深拷贝进行复制
                context=copy.deepcopy(GlobalVar().show_dict())
                # 将全局变量的中的值渲染为测试步骤里面 {{}}包裹的变量值
                step_value=eval(var_render(step_value,context))

                # TODO 5.根据步骤名称执行相应的操作，基于每个步骤的关键字,找到对应我们封装好的是哪个方法，并给与参数执行[反射]
                with allure.step(step_name):
                    key = step_value["关键字"]  # 具体的方法名，request_post_form_urlencoded
                    print("关键字方法是：", key)
                try:
                    # 利用反射获取到具体的keyword里面的方法，request_post_form_urlencoded
                    key_function = keyword.__getattribute__(key)
                    print("对应keyword的关键字方法是:", key_function)
                except Exception as e:
                    print(f"关键字的方法{key}不存在")

                key_function(**step_value)  # 步骤的值作为参数传入具体的方法中，执行具体的操作，ex_jsonData方法


        finally:
            print("该条用例步骤执行完毕")

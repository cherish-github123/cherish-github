# DS_022 登录接口-使用用户名能正确的登录用户
import allure
import jsonpath
import requests
from allframe.apirun5版本.keywords.keyword import Keyword
import allure
from allframe.apirun5版本.Utils.VarRender import var_render
from allframe.apirun5版本.Global_context.global_context import GlobalContext

keyword = Keyword()


@allure.title("登录ok")
def test_01_login3():
    url = "http://shop-xo.hctestedu.com?s=api/user/login"
    pub_params = {"application": "app", "application_client_type": "weixin"}
    data = {"accounts": "17812345678", "pwd": "tyl151006", "type": "username"}

    # 将请求数据拼接成一个字典
    request_data = {"url": url, "params": pub_params, "data": data}
    # 将请求数据进行渲染,渲染之后是字符串，使用eval()转为字典,使用不定长参数传参
    request_data = eval(var_render(request_data, GlobalContext().show_dict()))
    print("渲染后的值：",request_data)

    # 发送请求
    response = keyword.request_post(**request_data)

    with allure.step("提取登录的msg值"):
        msg = keyword.ex_jsonData(expression="$..msg", var_name="msg_result")
        print("提取的msg值为:", msg)

    with allure.step("提取登录的token值"):
        # expression和var_name是存放在全局变量中的变量名
        token = keyword.ex_jsonData(expression="$..token", var_name="token_result")
        print("获取到的token值为：", token)

    return token

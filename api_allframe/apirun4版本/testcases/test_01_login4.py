# DS_022 登录接口-使用用户名能正确的登录用户
import allure
import jsonpath
import requests
from allframe.apirun4版本.keywords.keyword import Keyword
import allure

keyword = Keyword()


@allure.title("登录ok")
def test_01_login3():
    url = "http://shop-xo.hctestedu.com?s=api/user/login"
    pub_params = {"application": "app", "application_client_type": "weixin"}
    data = {"accounts": "17812345678", "pwd": "tyl151006", "type": "username"}
    response = keyword.request_post(url=url, params=pub_params, data=data)

    with allure.step("提取登录的msg值"):
        # 将提取的msg数据存储到全局变量，变量名为msg_result
        msg = keyword.ex_jsonData(expression="$..msg", var_name="msg_result")
        print("提取的msg值为:", msg)

    assert msg == "登录成功", f"当前msg信息是{msg}"

    with allure.step("提取登录的token值"):
        # expression和var_name是存放在全局变量中的变量名,将token存储到全局变量中，变量名为token_result
        token = keyword.ex_jsonData(expression="$..token", var_name="token_result")
        print("获取到的token值为：", token)

    return token

# DS_022 登录接口-使用用户名能正确的登录用户
import allure
import jsonpath
import requests
from allframe.apirun3版本.keywords.keyword import Keyword

keyword = Keyword()


@allure.title("DS_022 登录接口-使用用户名能正确的登录用户")
def test_01_login3():
    url = "http://shop-xo.hctestedu.com?s=api/user/login"
    pub_params = {"application": "app", "application_client_type": "weixin"}
    data = {"accounts": "17812345678", "pwd": "tyl151006", "type": "username"}
    response = keyword.request_post(url=url, params=pub_params, json=data)

    value=jsonpath.jsonpath(response.json(),"$..msg")[0]
    print("提取的msg值为:",value)

    assert value=="登录成功",f"当前msg信息是{value}"

    token = jsonpath.jsonpath(response.json(), "$..token")[0]
    print("获取到的token值为：", token)
    return response


print(test_01_login3().json())

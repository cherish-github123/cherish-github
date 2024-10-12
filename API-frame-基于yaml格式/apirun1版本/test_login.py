import allure
import jsonpath
import requests


@allure.title("DS_022 登录接口-使用用户名能正确的登录用户")
def test_login():
    url = "http://shop-xo.hctestedu.com?s=api/user/login"
    pub_params = {"application": "app", "application_client_type": "weixin"}
    data = {"accounts": "17812345678", "pwd": "tyl151006", "type": "username"}
    response = requests.post(url, params=pub_params, json=data)

    value = jsonpath.jsonpath(response.json(), "$..msg")[0]
    print("提取的值为:", value)

    assert value == "登录成功", f"当前msg信息是{value}"


"""
requests是python的第三方库，用来发送http请求，jsonpath是用来解析json数据的库，allure是用来生成测试报告的库

"""
import allure
import jsonpath
import requests


@allure.title("DS_033 加入购物车验证无规格值可以加入到对应商品")
@allure.step("流程：登录---->获取token值---->添加购物车")
def test_addcart():
    # todo 1 登录
    with allure.step("第一步：登录"):
        url = "http://shop-xo.hctestedu.com?s=api/user/login"
        pub_params = {"application": "app", "application_client_type": "weixin"}
        data = {"accounts": "17812345678", "pwd": "tyl151006", "type": "username"}
        response = requests.post(url, params=pub_params, json=data)

    # todo 2 获取token值
    with allure.step("第二步：获取登录后的token值"):
        token = jsonpath.jsonpath(response.json(), "$..token")[0]
        print("获取到的token值为：", token)

    # todo 3 调用需要token的接口,添加购物车
    with allure.step("第三步：加入购物车"):
        url_cart = f"http://shop-xo.hctestedu.com?s=api/cart/save&token={token}"
        pub_params = {"application": "app", "application_client_type": "weixin"}
        data1 = {
            "goods_id": "11",
            "spec": "",
            "stock": 5
        }
        res = requests.post(url_cart, params=pub_params, json=data1)
        print(res.json())

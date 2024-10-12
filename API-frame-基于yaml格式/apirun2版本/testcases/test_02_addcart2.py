# DS_033	加入购物车	验证无规格值可以加入到对应商品

#  todo 1 登录
import allure
import jsonpath
import requests

from api_allframe_yaml.apirun2版本.keywords.keyword import Keyword

keyword = Keyword()


@allure.title("DS_033 加入购物车验证无规格值可以加入到对应商品")
@allure.step("先进行登录--获取token值--添加购物车")
def test_addcart():
    # todo 1 登录
    with allure.step("第一步：登录"):
        url = "http://shop-xo.hctestedu.com?s=api/user/login"
        pub_params = {"application": "app", "application_client_type": "weixin"}
        data = {"accounts": "17812345678", "pwd": "tyl151006", "type": "username"}
        response = keyword.request_post(url=url, params=pub_params, data=data)

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
        response = keyword.request_post(url=url_cart, params=pub_params, json=data1)

    return response.json()


print(test_addcart())

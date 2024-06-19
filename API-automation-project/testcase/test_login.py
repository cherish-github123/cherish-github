
import requests
import pytest
import jsonpath
from api_keyword.api_keyword import ApiKeys
import allure

@allure.title("登录--->加入购物车")
def test_login():
    apikey = ApiKeys()
    with allure.step("第一步：登录的接口"):
        # 1.登录
        url = "http://shop-xo.hctestedu.com/?s=api/user/login"
        public_params = {"application": "app", "application_client_type": "weixin"}
        data = {"accounts": "tyl151006", "pwd": "123456", "type": "username"}
        res=apikey.post(url,params=public_params,data=data)

        # 2.提取数据
        sjdata=apikey.get_data_from_response(res.json(),"$.msg")
        token=apikey.get_data_from_response(res.json(),"$..token")

        # 3. 断言
        assert "登录成功"==sjdata,"期望结果与实际结果不一致"

    with allure.step("第二步：加入购物车的接口"):
        # 4.加入购物车
        url = "http://shop-xo.hctestedu.com/index.php?s=/api/cart/save"
        public_data = {"application": "app", "application_client_type": "weixin", "token": token}
        data = {
            "goods_id": "11",
            "spec": [
                {
                    "type": "尺寸",
                    "value": "M"
                }
            ],
            "stock": "10"
        }

        res = apikey.post(url=url, params=public_data, data=data)
        print("响应结果：",res.json())
        # 5.提取msg
        sj_res=apikey.get_data_from_response(res.json(),"$.msg")
        # 6.断言
        assert "加入成功" ==sj_res,"期望与预期结果不一致"





test_login()

# def test_add_cart(login_fixture):
#     api_key,token=login_fixture  # 夹具也是一个函数需要调用，返回两个值：apikey和token
#     url = "http://shop-xo.hctestedu.com/index.php?s=/api/cart/save"
#     public_data = {"application": "app", "application_client_type": "weixin", "token": token}
#     data = {
#         "goods_id": "11",
#          "spec": [
#              {
#                  "type": "尺寸",
#                  "value": "M"
#              }
#          ],
#           "stock": "10"
#     }
#     res = api_key.post(url=url, params=public_data, data=data)
#     print("响应结果：" ,res.json())
#     # 5.提取msg
#     sj_res =api_key.get_data_from_response(res.json() ,"$.msg")
#     # 6.断言
#     assert "加入成功" ==sj_res ,"期望与预期结果不一致"


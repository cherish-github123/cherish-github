# DS_033	加入购物车	验证无规格值可以加入到对应商品

#  todo 1 登录
import token

import allure
import jsonpath
import requests
from allframe.apirun3版本.keywords.keyword import Keyword

keyword = Keyword()


@allure.title("DS_033 加入购物车验证无规格值可以加入到对应商品")
def test_02_addcart3(login_fixture):
    # todo 登录
    token_value = login_fixture
    print("token_value的值为：", token_value)

    # todo 1 调用登录夹具后返回token值，,添加购物车
    url_cart = "http://shop-xo.hctestedu.com?s=api/cart/save"
    pub_params = {"application": "app", "application_client_type": "weixin", "token": token_value}
    data1 = {
        "goods_id": "11",
        "spec": "",
        "stock": 5
    }

    response = keyword.request_post(url=url_cart, params=pub_params, json=data1)  # 调用request_post方法，返回的是response的json数据
    return response.json()



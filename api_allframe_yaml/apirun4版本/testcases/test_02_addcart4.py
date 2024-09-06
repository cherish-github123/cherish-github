# DS_033	加入购物车	验证无规格值可以加入到对应商品

#  todo 1 登录
import allure
import jsonpath
import requests

from api_allframe_yaml.apirun4版本.keywords.keyword import Keyword
from api_allframe_yaml.apirun4版本.Global_var.global_var import GlobalVar
keyword = Keyword()


@allure.title("DS_033 加入购物车验证无规格值可以加入到对应商品")
def test_02_addcart3():
    # 登录操作后，已经将token值存入全局变量，调用全局变量GlobalVar的get_dict方法，直接获取token值，然后赋值给变量token_value后续使用
    token_value=GlobalVar().get_dict("token_result")

    url_cart = "http://shop-xo.hctestedu.com?s=api/cart/save"
    pub_params = {"application": "app", "application_client_type": "weixin", "token": token_value}
    data1 = {
        "goods_id": "11",
        "spec": "",
        "stock": 5
    }

    response = keyword.request_post(url=url_cart, params=pub_params, json=data1)  # 调用request_post方法，返回的是response对象
    msg=keyword.ex_jsonData(expression="$..msg",var_name="msg_result")
    print("添加购物车提取到的msg信息：",msg)
    return response.json()




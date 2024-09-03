# DS_033	加入购物车	验证无规格值可以加入到对应商品

#  todo 1 登录
import allure
import jsonpath
import requests

from allframe.apirun6版本.Utils.VarRender import var_render
from allframe.apirun6版本.keywords.keyword import Keyword
from allframe.apirun6版本.Global_context.global_context import GlobalContext
keyword = Keyword()


@allure.title("DS_033 加入购物车验证无规格值可以加入到对应商品")
def test_02_addcart3():

    url_cart = "http://shop-xo.hctestedu.com?s=api/cart/save"
    pub_params = {"application": "app", "application_client_type": "weixin", "token": "{{token_result}}"}
    data1 = {
        "goods_id": "11",
        "spec": "",
        "stock": 5
    }
    request_data = {"url": url_cart, "params": pub_params, "data": data1}
    request_data = eval(var_render(request_data, GlobalContext().show_dict()))

    response = keyword.request_post(**request_data)
    msg=keyword.ex_jsonData(expression="$..msg",var_name="msg_result")
    print("添加购物车提取到的msg信息：",msg)
    return response.json()




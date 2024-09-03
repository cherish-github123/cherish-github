# DS_033	加入购物车	验证无规格值可以加入到对应商品

#  todo 1 登录
import allure
import jsonpath
import requests

from allframe.apirun5版本.Utils.VarRender import var_render
from allframe.apirun5版本.keywords.keyword import Keyword
from allframe.apirun5版本.Global_context.global_context import GlobalContext

keyword = Keyword()


@allure.title("DS_033 加入购物车验证无规格值可以加入到对应商品")
def test_02_addcart3():
    url_cart = "http://shop-xo.hctestedu.com?s=api/cart/save"
    pub_params = {"application": "app", "application_client_type": "weixin", "token": "{{token_result}}"}
    # 这里的token_result是从上一个登录接口获取的token值，存储在全局变量token_result，可以直接引用
    data1 = {
        "goods_id": "11",
        "spec": "",
        "stock": 5
    }
    # 将请求数据进行拼接  渲染
    request_data = {"url": url_cart, "params": pub_params, "data": data1}
    request_data = eval(var_render(request_data, GlobalContext().show_dict()))
    print("渲染后的值：", request_data)

    # 发送请求
    response = keyword.request_post(**request_data)

    # 为什么不用写response参数？
    # 因为request_post发送请求的方法已经将响应数据存放到了全局变量，且在ex_jsondata方法中已经将response返回了
    msg = keyword.ex_jsonData(expression="$..msg", var_name="msg_result")
    print("添加购物车提取到的msg信息：", msg)
    return response.json()

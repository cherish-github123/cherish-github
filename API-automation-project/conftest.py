import allure
import jsonpath
import pytest
import logging
import requests


#
# @pytest.fixture(scope="session")    # 指定fixture的作用域为session，在整个测试运行期间只执行一次
# def login_fixture():
#     # 定义一个用户登录的夹具
#     api_key=ApiKeys()
#     login_url=PROJECT_URL+"s=/api/user/login"
#     public_params=PUBLIC_PARAMS
#     data={"accounts":USER_NAME,"pwd":PASSWORD,"type":USER_TYPE}
#     res=api_key.post(url=login_url,params=public_params,data=data)
#     token =api_key.get_data_from_response(res.json(),"$..token")
#     return api_key,token


# 钩子函数，在测试用例之前执行，打印用例ID,测试结果，故障表示，异常，用例执行耗时等信息，需要结合pytest.ini文件使用
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 通过 out = yield 定义了一个生成器。在生成器中，res = out.get_result() 获取了测试结果对象。
    out = yield
    res = out.get_result()
    #  res.when == "call"：表示正在运行调用测试函数的阶段，不包括setup和teardown阶段
    if res.when == "call":
        logging.info(f"用例ID：{res.nodeid}")
        logging.info(f"测试结果：{res.outcome}")
        logging.info(f"故障表示：{res.longrepr}")
        logging.info(f"异常：{call.excinfo}")
        logging.info(f"用例耗时：{res.duration}")
        logging.info("**************************************")



@pytest.fixture(scope="session")    # 指定fixture的作用域为session，在整个测试运行期间只执行一次
def login_fixture():
    with allure.step("第一步：登录"):
        url = "http://shop-xo.hctestedu.com?s=api/user/login"
        pub_params = {"application": "app", "application_client_type": "weixin"}
        data = {"accounts": "17812345678", "pwd": "tyl151006", "type": "username"}
        response = requests.post(url=url, params=pub_params, json=data)

    # todo 2 获取token值
    with allure.step("第二步：获取登录后的token值"):
        token = jsonpath.jsonpath(response.json(), "$..token")[0]
        print("获取到的token值为：", token)

    return token
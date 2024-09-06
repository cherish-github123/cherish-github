import allure
import jsonpath
import pytest
import logging

from api_allframe_yaml.apirun5版本.keywords.keyword import Keyword


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


@pytest.fixture(scope="session")  # 指定fixture的作用域为session，在整个测试运行期间只执行一次
def login_fixture_token():
    keyword = Keyword()
    url = "http://shop-xo.hctestedu.com?s=api/user/login"
    pub_params = {"application": "app", "application_client_type": "weixin"}
    data = {"accounts": "17812345678", "pwd": "tyl151006", "type": "username"}
    response = keyword.request_post(url=url, params=pub_params, data=data)

    # todo 2 获取token值
    token = jsonpath.jsonpath(response.json(), "$..token")[0]
    print("获取到的token值为：", token)

    return token

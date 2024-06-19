import pytest
import logging

from api_keyword.api_keyword import ApiKeys
from config import *

@pytest.fixture(scope="session")
def login_fixture():
    # 定义一个用户登录的夹具
    api_key=ApiKeys()
    login_url=PROJECT_URL+"s=/api/user/login"
    public_params=PUBLIC_PARAMS
    data={"accounts":USER_NAME,"pwd":PASSWORD,"type":USER_TYPE}
    res=api_key.post(url=login_url,params=public_params,data=data)
    token =api_key.get_data_from_response(res.json(),"$..token")
    return api_key,token


# 钩子函数，在测试用例之前执行，打印用例ID,测试结果，故障表示，异常，用例执行耗时等信息，需要结合pytest.ini文件使用
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 通过 out = yield 定义了一个生成器。在生成器中，res = out.get_result() 获取了测试结果对象。
    out = yield
    res = out.get_result()
    #  res.when == "call"：表示正在运行调用测试函数的阶段
    if res.when == "call":
        logging.info(f"用例ID：{res.nodeid}")
        logging.info(f"测试结果：{res.outcome}")
        logging.info(f"故障表示：{res.longrepr}")
        logging.info(f"异常：{call.excinfo}")
        logging.info(f"用例耗时：{res.duration}")
        logging.info("**************************************")
import pytest
import logging


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
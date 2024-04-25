import logging

import allure
import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    global driver
    # 01 用例的前置步骤，初始化浏览器对象
    driver = webdriver.Chrome()

    # 02 用例执行，返回driver
    yield driver

    # 03 用例的后置步骤，关闭浏览器
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取测试用例的执行结果，yield，返回给out对象，然后再去转化为result对象
    out = yield

    """
        从result对象out获取调用结果的测试报告，返回一个report对象

        report对象的属性:
        包括when(setup，call，teardown等三个值)、nodeid(测试用例的名称)、
        outcome(用例的执行结果, passed, failed)
    """
    report = out.get_result()  # 返回一个report对象

    # 仅仅获取用例call阶段的执行结果，不包含setup、teardown
    if report.when == "call":
        # 修改之后的版本：
        allure.attach("--------->日志的头部<---------")
        allure.attach(f"用例ID：{report.nodeid}", name="用例ID")
        allure.attach(f"测试结果：{report.outcome}", name="测试结果")
        allure.attach(f"故障标识：{report.longrepr}", name="故障标识")
        allure.attach(f"异常信息：{call.excinfo}", name="异常信息")
        allure.attach(f"用例耗时：{report.duration}", name="用例耗时")
        allure.attach("--------->日志的尾部<---------")

        # 获取用例call执行结果为失败的情况
        xfail = hasattr(report, "wasxfail")  # hasattr方法会：返回对象是否具有给定名称的属性

        # 如果测试用例被跳过且标记为预期失败，或者测试用例执行失败且不是预期失败
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 添加allure报告截图
            with allure.step("添加失败的截图 ---> "):
                allure.attach(driver.get_screenshot_as_png(), "失败的截图",
                              allure.attachment_type.PNG)

        elif report.passed:
            # 如果测试用例执行通过，添加allure报告截图
            with allure.step("添加成功的截图 ---> "):
                allure.attach(driver.get_screenshot_as_png(), "成功的截图",
                              allure.attachment_type.PNG)



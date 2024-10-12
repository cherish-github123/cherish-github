import os

import pytest

if __name__ == '__main__':
    # todo  1 最基础的用法
    # pytest.main(["-vs"])
    # todo 2.1 结合allure测试报告，给main方法添加参数
    args = ["-vs", "--capture=sys",  # 用于显示输出调试信息，设置级别为sys,即输出到控制台
            "--clean-alluredir",  # 每次运行用例之前先清除之前的allure报告
            "--alluredir=allure-results",  # 执行过程中的数据存放到allure_results目录下
            ]
    pytest.main(args)

    # todo 2.2 结合产生的allure测试报告，产生HTML报告
    os.system("allure generate -c -o allure-report-html")

# TODO 注：allure报告需要以服务的形式打开，如果是本地打开，页面上是没有信息展示的，如果需要查看电脑上本地报告，需要导入allure-combine
from allure_combine import combine_allure
combine_allure("./allure-report-html")
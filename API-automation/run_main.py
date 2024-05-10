import os
import pytest
import allure_pytest


if __name__ == '__main__':
    # -v 显示详细信息，可以显示是哪一个文件里面的用例被执行
    # -s：打开终端（输出/输入）交互，在控制台输出要打印的内容（如果用例里面有input函数，不加-s执行会报错）
    # pytest.main(["-vs","./testcases/test_DS_022_使用用户名能正确的登录用户.py"])
    # TODO 通过pytest运行 并且生成allure报告【默认】
    # todo  第一步：指定运行文件，通过文件会生成数据，./result，当前文件夹下面的result目录下，--clean-alluredir（每次运行之前清空这个文件夹里面的历史数据）
    pytest.main(["-vs","--alluredir","./result","--clean-alluredir"])
    # todo  第二步：把生成的数据转成测试报告，allure generate ./result -o ./report_allure --clean
    os.system("allure generate ./result -o ./report-allure --clean")
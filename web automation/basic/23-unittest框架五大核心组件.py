"""
1.测试用例  Test_case
2.测试套件 Test_Suite  批量执行多个测试用例
3.测试运行器  Test_Runner
4.测试夹具 Test_fixture
5.断言方法  Assert

  规则：测试类需要继承unittest.TestCase
  测试用例以test_开头
  必须使用unittest.main()方法运行
"""

import unittest

# TODO 1 第一组件：测试用例类
class TestCase(unittest.TestCase):
    # TODO 4 第四大组件：测试夹具
    def setUp(self) -> None:
        print("---------->已获取到正确的用户名和密码")

    def tearDown(self) -> None:
        print("----------->关闭浏览器")

    def test_login(self):
        print("进行登录操作")

    def test_register(self):
        print("进行注册操作")

    def test_get_info(self):
        print("获取用户信息操作")
    # TODO 5 第五大组件：断言
        ex_result="信息正确"
        sj_result="信息"
        assert ex_result==sj_result,"断言失败"



# TODO  2 第二组件：测试套件
def suite():
    suite=unittest.TestSuite()
    suite.addTest(TestCase("test_login"))
    suite.addTest(TestCase("test_register"))
    suite.addTest(TestCase("test_get_info"))
    return suite



if __name__ == '__main__':
    # TODO 3 第三大组件：测试运行器
    runner=unittest.TextTestRunner()
    test_suite=suite()
    runner.run(test_suite)

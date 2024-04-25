import pytest
import os

if __name__ == '__main__':
    pytest.main(["-vs","--alluredir","./result","--clean-alluredir"])
    os.system("allure generate ./reult -o ./report/ --clean")
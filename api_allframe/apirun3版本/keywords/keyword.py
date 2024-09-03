
import jsonpath
import requests
import allure


class Keyword():
    @allure.step("发送get请求-------->")
    def request_get(self, **kwargs):
        response = requests.get(**kwargs)
        return response

    @allure.step("发送post请求-------->")
    def request_post(self, **kwargs):
        response = requests.post(**kwargs)
        return response





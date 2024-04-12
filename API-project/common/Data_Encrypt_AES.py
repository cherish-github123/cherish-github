"""
对称加密：加密和解密使用的是同一把钥匙
常用的加密方法：AES、DES、3DES
需安装  pip install pycryptodome
"""

import base64
import requests
from Cryptodome.Cipher import AES


class Data_Encrypt():
    def __init__(self,key):
        self.key=key.encode("utf-8")   # 初始化一个密钥，将字符串按照指定的编码格式转换为字节串，用于网络传输或者存储
        self.length=AES.block_size    # 获取AES加密算法的块大小，块大小是固定的，取决于密钥的长度，通常为16字节（128位 ）
        self.aes=AES.new(self.key,AES.MODE_ECB)   # 使用AES加密算法的ECB模式创建AES加密器
        self.unpad = lambda data: data[0:-ord(data[-1])]

    #  缺几位数据就补齐多少位数据：要补到16的倍数
    def pad(self, text):  # text == tony
        """ #填充函数，使被加密数据的字节码长度是block_size的整数倍  """
        count = len(text.encode('utf-8'))  # count = 4
        add = self.length - (count % self.length)  # 求它们相差的位数
        # add = 16- （4%16）  === 16 - 4 == 12
        entext = text + (chr(add) * add)
        #  entext = “tony” + （chr(add) * 12  ）  === entext == tony
        # print("entext的数据是:",entext)
        return entext

    # 加密函数
    def encrypt(self, encrData):  # 加密函数   encrData == tony （16位）
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))  # self.aes.encrypt(tony)
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg


     # 解密函数
    def decrypt(self, decrData):  # 解密函数XbXHJrNLwoTVcyfqM9eTgQ==
        # 从base64编码转回来
        res = base64.decodebytes(decrData.encode("utf8"))
        # 将数据进行对应的解密：XbXHJrNLwoTVcyfqM9eTgQ==
        msg = self.aes.decrypt(res).decode("utf8")
        # print("msg的值：",msg)
        return self.unpad(msg)           #  把转回来的数据后面的字符去掉


def login(username,password):
    url="http://127.0.0.1:8080/login_safe"
    # 需要将传入的账号和密码进行加密
    key="1234567812345678"
    ec=Data_Encrypt(key)
    new_username=ec.encrypt(username)
    new_password = ec.encrypt(password)
    data={"username":username,"password":password}
    res=requests.post(url=url,data=data)
    print("响应数据：",res.json())
if __name__ == '__main__':
            #  加密 ：会补位
            # key = "1234567812345678"  # key 密码
            # data = "tony"  # 数据
            # eg = Encrypt(key)  # 这里密钥的长度必须是16的倍数，并且设置对应的【模式】
            # res = eg.encrypt(str(data))
            # print(f"加密后的数据为：{res}")
            #
            # #  解密 ： 把后面的数据进行去除
            # key = "1234567812345678"  # key 密码
            # data = "XbXHJrNLwoTVcyfqM9eTgQ=="  # 数据
            # eg = Encrypt(key)  # 这里密钥的长度必须是16的倍数
            # res = eg.decrypt(str(data))
            # print(f"解密后的数据为：{res}")
            login("tony","123456")






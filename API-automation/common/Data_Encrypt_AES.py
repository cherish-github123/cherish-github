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
        self.length=AES.block_size    # 获取AES加密算法的块大小，块大小是固定的，取决于密钥的长度，通常为16字节（128位 ）  16位
        self.aes=AES.new(self.key,AES.MODE_ECB)   # 使用AES加密算法的ECB模式创建AES加密器
        # 截断函数，去除填充的字符，只保留有效数据
        """
        类似于字符串切片操作，data[-1]是最后一个字符
        ord(data[-1])是最后一个字符的ASCII码（数字） ,负的说明是0：-12，也就是后面补充的那部分字符，进行切片，只保留有效数据
        """
        self.unpad = lambda data: data[0:-ord(data[-1])]



    #  缺几位数据就补齐多少位数据：要补到16的倍数
    def pad(self, text):  # text = tyl151006
        """
        :param text: 需要加密的文本信息
        :return: 返回已经补齐16位的需要加密的文本entext
        填充函数，使被加密数据的字节码长度是block_size的整数倍  """
        count = len(text.encode('utf-8'))  # count 长度=9,text文本的长度是9
        add = self.length - (count % self.length)  # 取余是为了求它们相差的位数，count % self.length,9对16取余是9
        # add = 16- （9%16）  === 16 - 9== 7    text文本现在是9位，需要补齐7位才能到16位
        entext = text + (chr(add) * add)
        # chr(add)是将数字转换为字符，*add 是将add个自字符进行重复
        #  entext = “tyl151006” + （chr(add) * 7  ）  === entext == tony
        print("entext填充之后的数据是:",entext)
        return entext

    # 加密函数
    def encrypt_data(self, encrData):
        """
        :param encrData:需要加密的数据
        :return:   返回加密结果
        """
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))  # self.aes.encrypt(tyl151006
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg


     # 解密函数
    def decrypt_data(self, decrData):
        """
        :param decrData: 需要解密的数据
        :return: 解密结果
        """
        # 在加密的时候转换成了base64位，所以从base64编码转回来
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        # print("msg的值：",msg)
        return self.unpad(msg)           #  把转回来的数据后面没有用的字符去掉



def login(username,password):
    url="http://127.0.0.1:8080/login_safe"
    # 需要将传入的账号和密码进行加密
    key="1234567812345678"
    ec=Data_Encrypt(key)
    new_username = ec.encrypt_data(username)
    print("加密后的账号：",new_username)
    new_password = ec.encrypt_data(password)
    print("加密后的密码：",new_password)
    data={"username":new_username,"password":new_password}
    res=requests.post(url,data=data)
    print("响应数据：",res.json())


if __name__ == '__main__':
        login("tyl151006", "123456")
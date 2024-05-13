
"""
MD5加密是不可逆的，只能进行加密，不能进行解密
"""
import hashlib

def md5_encrypt(text):
    # 创建一个MD5对象
    md5 = hashlib.md5()
    # 更新对象的值
    md5.update(text.encode("utf-8"))
    # 返回加密后的字符串
    res = md5.hexdigest()
    return res


print(md5_encrypt("tyl151006"))
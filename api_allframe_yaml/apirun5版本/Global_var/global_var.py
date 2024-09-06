"""
在一个项目中，不是只有一个变量(token)需要全局共享，而是多个变量都需要全局共享，可以通过全局变量实现
具体实现：
1.字典格式存储
2.内置属性--只能在类里面访问的属性
3.提供对应的方法，可以对这个属性进行增加/修改/显示

设置完成后，在进行接口关联时，需要使用jsonpath提取数据然后放到全局变量中，所以封装一个方法在关键字中（keyword.py）
"""


class GlobalVar(object):
    _dict = {}

    # TODO 1 ；通过key进行设置（新增）
    def set_dict(self, key, value):
        self._dict[key] = value

    # TODO 2 :通过可以key获取数据
    def get_dict(self, key):
        # return self._dict(key)   #如果可以不存在的话，会报错，就使用下面的get方法，如果可以不存在，会返回None
        return self._dict.get(key, None)

    # TODO 3 ：通过传入字典设置数据
    def update_by_dict(self, data_dict):
        """
        :param data_dict: 字典格式的数据
        :return:
        """
        self._dict.update(data_dict)

    # TODO 4:显示对应的全局变量
    def show_dict(self):
        return self._dict


# 测试：
if __name__ == '__main__':
    global_context = GlobalVar()
    global_context.set_dict("dguegfu", "也会打电话")
    print(global_context.get_dict(("dguegfu")))

    data = {"name": "1123", "dguegfu": "UR号规定", "rt": "fdeuyf"}
    global_context.update_by_dict(data)
    print(global_context.show_dict())

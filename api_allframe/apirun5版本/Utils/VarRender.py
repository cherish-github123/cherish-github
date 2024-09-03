"""
字符串模板，进行变量渲染，渲染后返回的是字符串
"""

from jinja2 import Template


def var_render(target, context):
    """

    :param target: 需要渲染的初始数据---请求数据
    :param context: 需要渲染的变量----全局变量
    :return:
    """

    if target is None:
        return None
    return Template(str(target)).render(context)


def ven():
    target="hello {{token}},{{name}},{{age}}"
    context={"token":"bduevhuerdufihgueiw5457h1","age":"15"}
    # 将context中的token值渲染到target中，并返回渲染后的字符串，如果context中没有name值，就渲染成空字符串
    res=var_render(target, context)
    return res


print(ven())    # hello bduevhuerdufihgueiw5457h1,,15

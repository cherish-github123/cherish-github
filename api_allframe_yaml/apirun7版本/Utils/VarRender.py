"""
字符串模板，进行变量渲染
"""

from jinja2 import Template


def var_render(target, context):
    """

    :param target: 需要渲染的数据
    :param context: 需要渲染的变量，也就是根据target的值渲染成context变量的值
    :return:
    """

    if target is None:
        return None
    return Template(str(target)).render(context)

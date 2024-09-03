"""
读取yaml文件的方法,yaml文件里面直接存放的就是测试用例
"""
import yaml


class YamlFileRead():
    # todo 1 读取yaml文件的所有数据
    @staticmethod
    def read_yaml(file_path):
        with open(file_path,mode="r",encoding="utf-8"):
            yaml_data=yaml.full_load(file_path)

        return yaml_data






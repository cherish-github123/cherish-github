import yaml

from config import *

class FileYamlRead():
    # 读取yaml文件,静态方法可以直接使用类名调用，不需要创建实例化对象
    @staticmethod
    def read_yaml(yamlfile_path=YAML_FILE_PATH):
        """
        :param yamlfile_path:  yaml文件的路径,YAML_FILE_PATH是维护在config.py文件中的常量，可以直接导入后使用
        :return:   读取的结果
        """
        with open(yamlfile_path,mode="r",encoding='UTF-8') as file:
            data=yaml.safe_load(file)
        return data

   # 写入yaml文件
    @staticmethod
    def write_yaml(data,yamlfile_path=YAML_FILE_PATH):
        """
        :param data: 需要写入的数据
        :param yamlfile_path:  yaml文件的路径,YAML_FILE_PATH是维护在config.py文件中的常量，可以直接导入后使用
        :return:
        """

        with open(yamlfile_path,mode="w",encoding='UTF-8') as file:
            yaml.dump(data, file)


if __name__ == '__main__':
    print(FileYamlRead.read_yaml())        # 返回的是列表
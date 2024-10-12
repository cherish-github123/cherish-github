"""
读取yaml文件的方法,yaml文件里面直接存放的就是测试用例
"""
import yaml


class YamlFileRead():
    # todo 1 读取yaml文件的所有数据
    @staticmethod
    def read_yaml(file_path):
        case_infos=[]    # 定义一个空列表，用来存放yaml文件读取的数据
        with open(file_path, mode="r", encoding="utf-8")as file:
            # 读取yaml文件
            yaml_data = yaml.full_load(file)
            case_infos.append(yaml_data)    # yaml_data是每一条用例信息，添加到列表中
            print("yaml文件读取的数据info:", case_infos)

        return case_infos


if __name__ == '__main__':
    file_path = "../data/yaml/登录接口测试用例.yaml"
    YamlFileRead().read_yaml(file_path)

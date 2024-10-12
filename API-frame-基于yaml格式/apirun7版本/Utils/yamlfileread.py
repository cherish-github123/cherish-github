"""
读取yaml文件的方法,yaml文件里面直接存放的就是测试用例
"""
import yaml
from api_allframe_yaml.apirun7版本.Global_var.global_var import GlobalVar
import os




class YamlFileRead():
    # todo 1 读取yaml文件的所有数据
    def read_yaml(self, file_path):
        # 调用yaml全局变量数据更新到全局变量字典的方法
        self.yaml_write_to_global_var("../data/yaml/yaml_global.yaml")
        case_infos = []  # 定义一个空列表，用来存放yaml文件读取的数据
        with open(file_path, mode="r", encoding="utf-8") as file:
            # 读取yaml文件
            yaml_data = yaml.full_load(file)
            case_infos.append(yaml_data)  # yaml_data是每一条用例信息，添加到列表中
            print("yaml文件读取的数据info:", case_infos)

        return case_infos

    def yaml_write_to_global_var(self,yaml_path):
        try:
            # 将定义的yaml全局变量的数据写入全局变量字典中
            with open(yaml_path, mode="r", encoding="utf-8") as file:
                data = yaml.load(file, Loader=yaml.FullLoader)  # 读取yaml文件，data是字典类型
                print("读取yaml全局变量数据为：", data)
                if data:  # 判断data不为空,不为空时将数据更新到全局变量中
                    GlobalVar().update_by_dict(data)
        except Exception as e:
            print("yaml文件读取失败")
            print(e)





if __name__ == '__main__':
    file_path = "../data/yaml/登录接口测试用例.yaml"
    # YamlFileRead().read_yaml(file_path)


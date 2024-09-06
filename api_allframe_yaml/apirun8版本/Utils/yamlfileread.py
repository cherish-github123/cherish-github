"""
读取yaml文件的方法,yaml文件里面直接存放的就是测试用例
"""
import os

import yaml
from api_allframe_yaml.apirun8版本.Global_var.global_var import GlobalVar


class YamlFileRead():
    # todo 1 读取yaml文件的所有数据
    def read_yaml(self, file_path):
        # 调用yaml数据更新到全局变量的方法
        self.yaml_write_to_global_var("../data/yaml/yaml_global.yaml")
        case_infos = []  # 定义一个空列表，用来存放yaml文件读取的数据
        with open(file_path, mode="r", encoding="utf-8") as file:
            # 读取yaml文件
            yaml_data = yaml.full_load(file)
            case_infos.append(yaml_data)  # yaml_data是每一条用例信息，添加到列表中
            print("yaml文件读取的数据info:", case_infos)

        return case_infos

    def yaml_write_to_global_var(self,yaml_path):
        # 将全局变量文件写入到全局变量字典中的方法,yaml_path是存放yaml全局变量文件的路径
        try:
            with open(yaml_path, mode="r", encoding="utf-8") as file:
                data = yaml.load(file, Loader=yaml.FullLoader)  # 读取yaml文件，data是字典类型
                print("读取yaml全局变量数据为：", data)
                if data:  # 判断data不为空,不为空时将数据更新到全局变量中
                    GlobalVar().update_by_dict(data)

        except Exception as e:
            print("yaml文件读取失败，无法添加到全局变量字典")
            return False

    def load_yaml_case(self,load_yaml_path):
        # 加载某个文件夹下所有符合条件的用例yaml文件的方法
        #  TODO 1.获取存放yaml测试用例的文件夹路径
        load_yaml_path = "../data/yaml"
        # 获取文件夹下的所有yaml测试文件
        all_yaml_case = os.listdir(load_yaml_path)

        # TODO 2.定义一个空列表，用来存放符合条件的yaml测试用例
        file_list_data = []
        # 遍历这个文件夹下的所有yaml测试文件
        for file_name in all_yaml_case:
            # 判断文件名以.yaml结尾 同时使用_分割后前面是不是数字,将符合条件的测试用例添加到file_list_data中
            if file_name.endswith(".yaml") and file_name.split("_")[0].isdigit():
                file_list_data.append(file_name)

        return file_list_data



    def define_yaml_type(self):
        # 规范yaml文件数据格式的方法
        pass


if __name__ == '__main__':
    file_path = "../data/yaml/登录接口测试用例.yaml"
    # YamlFileRead().read_yaml(file_path)
    print(YamlFileRead().load_yaml_case())

import os

from api_allframe_yaml.apirun8版本.Global_var.global_var import GlobalVar
import pandas as pd
import openpyxl


class ExcelFileRead():

    def read_excel(self, file_path):
        pass

    def load_excel_case(self, load_excel_path):
        # 加载某个文件夹下所有符合条件的excel用例的方法
        #  TODO 1.获取存放yaml测试用例的文件夹路径
        load_excel_path = "../data/excel"
        # 获取文件夹下的所有yaml测试文件
        all_excel_case = os.listdir(load_excel_path)

        # TODO 2.定义一个空列表，用来存放符合条件的yaml测试用例
        file_list_data = []
        # 遍历这个文件夹下的所有yaml测试文件
        for file_name in all_excel_case:
            # 判断文件名以.yaml结尾 同时使用_分割后前面是不是数字,将符合条件的测试用例添加到file_list_data中
            if file_name.endswith(".excel") and file_name.split("_")[0].isdigit():
                file_list_data.append(file_name)

        return file_list_data

    def excel_write_to_global_var(self, excel_path):
        # 将excel全局变量文件添加到全局变量字典的方法
        try:
            with open(excel_path, mode="r", encoding="utf-8") as file:
                data = pd.read_excel(file)
                print("读取excel全局变量数据为：", data)
                for index, row in data.iterrows():  # 遍历每一行数据
                    pass



        except Exception as e:
            print("excel文件读取失败,无法添加到全局变量字典")
            return False

    def define_excel_type(self):
        # 规范yaml文件数据格式的方法
        pass

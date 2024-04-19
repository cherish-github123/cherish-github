import openpyxl


from config import *
class FileExcelRead():
    @staticmethod
    # 读取excel文件
    def read_excel(excel_file_path=EXCEL_FILE_PATH,sheet_name=SHEET_NAME):
        """
        :param excel_file_path:   excel文件的路径，EXCEL_FILE_PATH是维护在config.py的常量
        :param sheet_name:  excel要操作的sheet页名，SHEET_NAME是维护在config.py的常量
        :return:  返回读取的结果
        """
        try:
            # 打开现有的excel文件或者创建一个新的文件
            # openpyxl.load_workbook(),用于加载excel文件并且返回一个Workbook对象，在python中对excel文件进行操作
            workbook=openpyxl.load_workbook(excel_file_path)
            print("返回的workbook:",workbook)
        except:
            # 如果文件不存在，就创建一个新的excel对象
            workbook=openpyxl.Workbook()
            raise FileNotFoundError("找不到excel文件")

        # 选择或者创建新的sheet页
        # 先判断传入的sheet_name是不是在excel文件中,如果存在，就加载数据，work.sheetnames是获取excel的所有sheet页
        if sheet_name in workbook.sheetnames:
            worksheet=workbook[sheet_name]
        else:
            # 没有该sheet就创建一个新的sheet页
            worksheet=workbook.create_sheet(sheet_name)

        # 获取列名，把sheet页第2行的数据拿到当做key值
        headers=[cell.value for cell in worksheet[2]]   # 对第二行的每个单元格获取它的值，并将这些值放在一个列表中
        # 将excel的每一行数据存储为一个字典，并且放在data中
        data=[]

        """
        1.worksheet.iter_rows() 用于按行迭代工作表中的数据
        2.min=3 指定迭代的起始行
        3.values_only=True,指定只返回单元格中的值
        4.dict(zip(headers,row)),将headers列表中的元素作为键，row列表中的对应元素作为值，创建一个键值对应的字典
        """
        for row in worksheet.iter_rows(min_row=3,values_only=True):
            # 用例过滤机制：如果excel文件中有用例不需要执行，可以添加一个字段为is_true,为True执行，为False时不执行
            new_data=dict(zip(headers,row))
            if new_data["is_true"] is True:
                data.append(new_data)

        workbook.close()
        print("从excel读取的数据为：",data)
        return data

    @staticmethod
    def write_excel(excel_file_path=EXCEL_FILE_PATH,sheet_name=SHEET_NAME,column=None,row=None,value=None):
        # 打开已经存在的excel文件或者创建新的excel文件
        try:
            workbook=openpyxl.load_workbook(excel_file_path)
        except FileNotFoundError:
            workbook=openpyxl.Workbook()

        # 选择或者创建指定的工作表
        if sheet_name in workbook.sheetnames:
            worksheet=workbook[sheet_name]
        else:
            worksheet=workbook.create_sheet(sheet_name)

        # 写入数据到指定的行或者列
        worksheet.cell(column=column,row=row).value=value

        # 写入完成后保存文件
        workbook.save(excel_file_path)







if __name__ == '__main__':
    FileExcelRead.read_excel()


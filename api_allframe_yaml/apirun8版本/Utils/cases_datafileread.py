
from api_allframe_yaml.apirun8版本.Utils.yamlfileread import YamlFileRead
from api_allframe_yaml.apirun8版本.Utils.excelfileread import ExcelFileRead
import os

class CaseDataFileRead():

    def case_data_file_read(self ,case_type ,case_dir):
        """

        :param case_type: 传入的用例数据文件类型，excel/yaml
        :param case_dir:存放excel/yaml的文件夹
        :return:
        """
        config_path =os.path.abspath(case_dir)

        if case_type=="yaml":
            return YamlFileRead().load_yaml_case(config_path)

        if case_type=="excel":
            return ExcelFileRead().load_excel_case(config_path)

        else:
            return {"case_name":[],"case_info":[]}


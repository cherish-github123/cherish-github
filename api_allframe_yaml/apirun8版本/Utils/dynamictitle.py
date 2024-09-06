import allure


def dynamic_title(caseData):
    allure.dynamic.parameter("caseinfo","")

    # 动态获取测试标题
    if caseData.get("_case_name", None) is not None:
        allure.dynamic.title(caseData["_case_name"])

    # 动态获取测试模块名
    if caseData.get("storyName", None) is not None:
        allure.dynamic.story(caseData["storyName"])

    # 动态获取测试模块名下面的子名
    if caseData.get("featureName", None) is not None:
        allure.dynamic.feature(caseData["featureName"])

    # 动态获取测试备注信息
    if caseData.get("remark", None) is not None:
        allure.dynamic.description(caseData["remark"])

    # 动态获取测试用例级别信息
    if caseData.get("rank",None) is not None:
        allure.dynamic.severity(caseData["rank"])

import base64
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.CreateFlowUtils import BuildPersonApprover

# BuildApprovers 构造签署人 - 以个人为例, 实际请根据自己的场景构造签署方、控件
def BuildApprovers():
    # 个人签署方参数
    person_name = "***"
    person_mobile = "**********"

    # 企业签署方参数
    # organization_name = "***"
    # organization_open_id = "**********"
    # open_id = "**********"

    # 用列表存储(此处根据自己签署的类型选择对应的传入参数，如单c就只传入一次个人签署方，BtoC就传入一个个人签署方，一个企业签署方)
    # 传入个人签署方
    flow_approver_info_list = [BuildPersonApprover(person_name, person_mobile)]

    # 传入企业签署方
    # flow_approver_info_list.append(BuildOrganizationApprover(organization_name, organization_open_id, open_id))
    
    # 传入企业静默签署
    # flow_approver_info_list.append(BuildServerSignApprover())

    return flow_approver_info_list


# 将文件处理为Base64编码后的文件内容
def convertImageFileToBase64(file_path):
    with open(file_path, 'rb') as f:
        a = base64.b64encode(f.read())
    return str(a, encoding='utf-8')

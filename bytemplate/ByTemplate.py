import os
import sys

from tencentcloud.essbasic.v20210526.models import FormField

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.DescribeTemplates import describeTemplates
from common.CreateFlowUtils import fillAgent, BuildPersonApprover

# BuildApprovers 构造签署人 - 以单C为例, 实际请根据自己的场景构造签署方、控件
def BuildApprovers(recipient_id):
    # 个人签署方参数
    person_name = "***"
    person_mobile = "**********"

    # 企业签署方参数
    # organization_name = "***"
    # organization_open_id = "**********"
    # open_id = "**********"

    # 用列表存储(此处根据自己签署的类型选择对应的传入参数，如单c就只传入一次个人签署方，BtoC就传入一个个人签署方，一个企业签署方)
    # 传入个人签署方
    flow_approver_infos = [BuildPersonApprover(person_name, person_mobile)]

    # 传入企业签署方
    # flow_approver_infos.append(BuildOrganizationApprover(organization_name, organization_open_id, open_id))
    # 传入企业静默签署
    # flow_approver_infos.append(BuildServerSignApprover())

    # 设置模版中的参与方RecipientId
    for i in flow_approver_infos:
        i.RecipientId = recipient_id

    return flow_approver_infos

# 从模板中获取参与人信息，用于模板发起合同
def GetRecipients(template_id):
    agent = fillAgent()
    templates_response = describeTemplates(agent, template_id)
    return templates_response.Templates[0].Recipients[0].RecipientId

# 内容控件填充结构，详细说明参考
# https://cloud.tencent.com/document/api/1420/61525#FormField
def BuildFormField(component_name, component_value):
    form_field = FormField()
    form_field.ComponentName = component_name
    form_field.ComponentValue = component_value
    return form_field

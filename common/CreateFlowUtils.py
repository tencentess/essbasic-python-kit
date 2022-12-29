from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.essbasic.v20210526 import essbasic_client
from tencentcloud.essbasic.v20210526.models import Agent, UserInfo
from tencentcloud.essbasic.v20210526.models import FlowApproverInfo, Component
from tencentcloud.essbasic.v20210526.models import FlowInfo

from config.Config import *


def fillAgent():
    agent = Agent()
    user_info = UserInfo()
    agent.AppId = AppId
    agent.ProxyAppId = ProxyAppId
    agent.ProxyOrganizationOpenId = ProxyOrganizationOpenId
    user_info.OpenId = ProxyOperatorOpenId
    agent.ProxyOperator = user_info
    return agent


def fillFlowInfo(template_id, flow_name, flow_approver_infos):
    flow_info = FlowInfo()
    flow_info.TemplateId = template_id
    flow_info.FlowName = flow_name
    flow_info.FlowApprovers = flow_approver_infos
    flow_info.FlowType = "合同"
    return flow_info


def initClient():
    # 实例化一个认证对象，入参需要传入腾讯云账户SecretId，SecretKey,此处还需注意密钥对的保密
    # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
    cred = credential.Credential(SecretId, SecretKey)
    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    http_profile = HttpProfile()
    http_profile.endpoint = EndPoint

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    client_profile = ClientProfile()
    client_profile.httpProfile = http_profile
    # 实例化要请求产品的client对象,clientProfile是可选的
    client = essbasic_client.EssbasicClient(cred, "", client_profile)
    return client


# 打包个人签署方信息
def BuildPersonApprover(person_name, person_mobile):
    # 签署方参与信息
    flow_approver_info = FlowApproverInfo()

    # 签署人类型
    # PERSON-个人/自然人；
    # ORGANIZATION-企业（企业签署方或模版发起时的企业静默签）；
    # ENTERPRISESERVER-企业静默签（文件发起时的企业静默签字）。
    flow_approver_info.ApproverType = "PERSON"

    # 签署人姓名，最大长度50个字符
    flow_approver_info.Name = person_name
    # 签署人手机号，脱敏显示。大陆手机号为11位，暂不支持海外手机号
    flow_approver_info.Mobile = person_mobile
    
    #  控件，包括填充控件、签署控件，具体查看
	# https://cloud.tencent.com/document/api/1420/61525#Component

    #这里简单定义一个个人手写签名的签署控件
    component = BuildComponent(146.15625, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flow_approver_info.SignComponents = [component]

    return flow_approver_info

# 打包企业签署方参与者信息
def BuildOrganizationApprover(organization_name, organization_open_id, open_id):
    # 签署方参与信息
    flow_approver_info = FlowApproverInfo()

    # 签署人类型
    # PERSON-个人/自然人；
    # ORGANIZATION-企业（企业签署方或模版发起时的企业静默签）；
    # ENTERPRISESERVER-企业静默签（文件发起时的企业静默签字）。
    flow_approver_info.ApproverType = "ORGANIZATION"

    # 企业签署方工商营业执照上的企业名称，签署方为非发起方企业场景下必传，最大长度64个字符；
    flow_approver_info.OrganizationName = organization_name

	# 如果签署方是子客企业，此处需要传子客企业的OrganizationOpenId
	# 企业签署方在同一渠道下的其他合作企业OpenId，签署方为非发起方企业场景下必传，最大长度64个字符；
    flow_approver_info.OrganizationOpenId = organization_open_id
	# 如果签署方是子客企业，此处需要传子客企业经办人的OpenId
	# 当签署方为同一渠道下的员工时，该字段若不指定，则发起【待领取】的流程
    flow_approver_info.OpenId = open_id
    
    #  控件，包括填充控件、签署控件，具体查看
	# https://cloud.tencent.com/document/api/1420/61525#Component

    # 这里简单定义一个个人手写签名的签署控件
    component = BuildComponent(146.15625, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flow_approver_info.SignComponents = [component]

    return flow_approver_info

# 打包企业静默签署方参与者信息
def BuildServerSignApprover():
    flow_approver_info = FlowApproverInfo()

    # 签署人类型
    # PERSON-个人/自然人；
    # ORGANIZATION-企业（企业签署方或模版发起时的企业静默签）；
    # ENTERPRISESERVER-企业静默签（文件发起时的企业静默签字）。
    flow_approver_info.ApproverType = "ENTERPRISESERVER"

    #  控件，包括填充控件、签署控件，具体查看
	# https://cloud.tencent.com/document/api/1420/61525#Component

    # 这里简单定义一个个人手写签名的签署控件
    component = BuildComponent(146.15624, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flow_approver_info.SignComponents = [component]

    return flow_approver_info

# BuildComponent 构建（签署）控件信息
# 详细参考 https://cloud.tencent.com/document/api/1420/61525#Component

# 在通过文件发起合同时，对应的component有三种定位方式
# 绝对定位方式
# 表单域(FIELD)定位方式
# 关键字(KEYWORD)定位方式
# 可以参考官网说明
# https://cloud.tencent.com/document/product/1323/78346#component-.E4.B8.89.E7.A7.8D.E5.AE.9A.E4.BD.8D.E6.96.B9.E5.BC.8F.E8.AF.B4.E6.98.8E
def BuildComponent(component_pos_x, component_pos_y, component_width, component_height, file_index, component_type,
                   component_page, component_value):
    component = Component()

    # 位置信息 包括：
    # 参数控件X位置，单位px
    component.ComponentPosX = component_pos_x
    # 参数控件Y位置，单位px
    component.ComponentPosY = component_pos_y
    # 参数控件宽度，默认100，单位px，表单域和关键字转换控件不用填
    component.ComponentWidth = component_width
    # 参数控件高度，默认100，单位px，表单域和关键字转换控件不用填
    component.ComponentHeight = component_height
    # 控件所属文件的序号(文档中文件的排列序号，从0开始)
    component.FileIndex = file_index
    # 参数控件所在页码，从1开始
    component.ComponentPage = component_page

    # 控件类型与对应值，这里以官网说明为准
	# https://cloud.tencent.com/document/api/1420/61525#Component
    component.ComponentType = component_type
    component.ComponentValue = component_value

    return component

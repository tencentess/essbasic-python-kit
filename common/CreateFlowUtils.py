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

    flow_approver_info.ApproverType = "PERSON"

    flow_approver_info.Name = person_name

    flow_approver_info.Mobile = person_mobile
    

    #这里简单定义一个个人手写签名的签署控件
    component = BuildComponent(146.15625, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flow_approver_info.SignComponents = [component]

    return flow_approver_info

# 打包企业签署方参与者信息
def BuildOrganizationApprover(organization_name, organization_open_id, open_id):
    # 签署方参与信息
    flow_approver_info = FlowApproverInfo()

    flow_approver_info.ApproverType = "ORGANIZATION"

    flow_approver_info.OrganizationName = organization_name

    flow_approver_info.OrganizationOpenId = organization_open_id

    flow_approver_info.OpenId = open_id

    # 这里简单定义一个个人手写签名的签署控件
    component = BuildComponent(146.15625, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flow_approver_info.SignComponents = [component]

    return flow_approver_info

# 打包企业静默签署方参与者信息
def BuildServerSignApprover():
    flow_approver_info = FlowApproverInfo()

    flow_approver_info.ApproverType = "ENTERPRISESERVER"

    # 这里简单定义一个个人手写签名的签署控件
    component = BuildComponent(146.15624, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flow_approver_info.SignComponents = [component]

    return flow_approver_info

# BuildComponent 构建（签署）控件信息
def BuildComponent(component_pos_x, component_pos_y, component_width, component_height, file_index, component_type,
                   component_page, component_value):
    component = Component()

    component.ComponentPosX = component_pos_x

    component.ComponentPosY = component_pos_y

    component.ComponentWidth = component_width

    component.ComponentHeight = component_height

    component.FileIndex = file_index

    component.ComponentPage = component_page

    component.ComponentType = component_type
    component.ComponentValue = component_value

    return component

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

    # 操作人的名字
    flow_approver_info.Name = person_name
    # 操作人的手机号
    flow_approver_info.Mobile = person_mobile
    # 签署人类型，PERSON - 个人；
    # ORGANIZATION - 企业；
    # ENTERPRISESERVER - 企业静默签;
    # 注：ENTERPRISESERVER
    # 类型仅用于使用文件创建流程（ChannelCreateFlowByFiles）接口；并且仅能指定发起方企业签署方为静默签署；
    flow_approver_info.ApproverType = "PERSON"
    #  模板控件信息
    #  签署人对应的签署控件
    component = BuildComponent(146.15625, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flow_approver_info.SignComponents = [component]
    return flow_approver_info


# 打包企业签署方参与者信息
def BuildOrganizationApprover(organization_name, organization_open_id, open_id):
    # 签署方参与信息
    flow_approver_info = FlowApproverInfo()

    flow_approver_info.OrganizationName = organization_name
    flow_approver_info.OrganizationOpenId = organization_open_id
    flow_approver_info.OpenId = open_id
    # 签署人类型，PERSON - 个人；
    # ORGANIZATION - 企业；
    # ENTERPRISESERVER - 企业静默签;
    # 注：ENTERPRISESERVER
    # 类型仅用于使用文件创建流程（ChannelCreateFlowByFiles）接口；并且仅能指定发起方企业签署方为静默签署；
    flow_approver_info.ApproverType = "ORGANIZATION"
    #  模板控件信息
    #  签署人对应的签署控件
    component = BuildComponent(146.15625, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flow_approver_info.SignComponents = [component]

    return flow_approver_info


# 打包企业静默签署方参与者信息
def BuildServerSignApprover():
    flow_approver_info = FlowApproverInfo()

    # 签署人类型，PERSON - 个人；
    # ORGANIZATION - 企业；
    # ENTERPRISESERVER - 企业静默签;
    # 注：ENTERPRISESERVER
    # 类型仅用于使用文件创建流程（ChannelCreateFlowByFiles）接口；并且仅能指定发起方企业签署方为静默签署；
    flow_approver_info.ApproverType = "ENTERPRISESERVER"
    #  模板控件信息
    #  签署人对应的签署控件
    component = BuildComponent(146.15624, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flow_approver_info.SignComponents = [component]

    return flow_approver_info


def BuildComponent(component_pos_x, component_pos_y, component_width, component_height, file_index, component_type,
                   component_page, component_value):
    component = Component()
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
    # 如果是Component控件类型，则可选的字段为：
    # TEXT - 普通文本控件；
    # DATE - 普通日期控件；跟TEXT相比会有校验逻辑
    # DYNAMIC_TABLE - 动态表格控件
    # 如果是SignComponent控件类型，则可选的字段为
    # SIGN_SEAL - 签署印章控件；
    # SIGN_DATE - 签署日期控件；
    # SIGN_SIGNATURE - 用户签名控件；
    # SIGN_PERSONAL_SEAL - 个人签署印章控件；
    # 表单域的控件不能作为印章和签名控件
    component.ComponentType = component_type
    # 参数控件所在页码，从1开始
    component.ComponentPage = component_page
    # 印章ID，传参DEFAULT_COMPANY_SEAL表示使用默认印章。
    # 控件填入内容，印章控件里面，如果是手写签名内容为PNG图片格式的base64编码。
    component.ComponentValue = component_value

    return component

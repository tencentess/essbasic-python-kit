from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.essbasic.v20210526 import essbasic_client
from tencentcloud.essbasic.v20210526.models import Agent, UserInfo
from config.Config import *
from tencentcloud.essbasic.v20210526.models import FlowInfo


def fillAgent():
    agent = Agent()
    userInfo = UserInfo()
    agent.AppId = AppId
    agent.ProxyAppId = ProxyAppId
    agent.ProxyOrganizationOpenId = ProxyOrganizationOpenId
    userInfo.OpenId = ProxyOperatorOpenId
    agent.ProxyOperator = userInfo
    return agent


def fillFlowInfo(TemplateId, FlowName, FlowApproverInfos):
    flowInfo = FlowInfo()
    flowInfo.TemplateId = TemplateId
    flowInfo.FlowName = FlowName
    flowInfo.FlowApprovers = FlowApproverInfos
    flowInfo.FlowType = "合同"
    return flowInfo


def initClient():
    # 实例化一个认证对象，入参需要传入腾讯云账户SecretId，SecretKey,此处还需注意密钥对的保密
    # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
    cred = credential.Credential(SecretId, SecretKey)
    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    httpProfile = HttpProfile()
    httpProfile.endpoint = EndPoint

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # 实例化要请求产品的client对象,clientProfile是可选的
    client = essbasic_client.EssbasicClient(cred, "", clientProfile)
    return client

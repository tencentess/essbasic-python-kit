from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def prepareFlows(agent, flow_infos, jump_url):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.PrepareFlowsRequest()

        req.Agent = agent

        req.FlowInfos = flow_infos

        req.JumpUrl = jump_url

        # 返回的resp是一个PrepareFlowsResponse的实例，与请求对象对应
        return client.PrepareFlows(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    flowInfo = models.FlowInfo()
    flowInfo.FlowName = "合同名称"
    flowInfo.Deadline = 0
    flowInfo.TemplateId = "******************"

    flowApprover = models.FlowApproverInfo()
    flowApprover.Name = "******************"
    flowApprover.IdCardType = ""
    flowApprover.IdCardNumber = ""
    flowApprover.Mobile = "******************"
    flowApprover.OrganizationName = ""
    flowApprover.OpenId = ""
    flowApprover.OrganizationOpenId = ""
    flowApprover.ApproverType = "PERSON"
    flowApprover.RecipientId = ""
    flowApprover.CallbackUrl = ""
    flowInfo.FlowApprovers = [flowApprover]

    formField = models.FormField()
    formField.ComponentValue = ""
    formField.ComponentName = ""
    flowInfo.FormFields = [formField]

    flowInfo.CallbackUrl = ""
    flowInfo.FlowType = ""
    flowInfo.FlowDescription = ""
    flowInfo.CustomerData = ""
    flowInfo.CustomShowMap = ""
    flowInfo.CcInfos = None
    flowInfo.NeedSignReview = False
    FlowInfos = [flowInfo]

    JumpUrl = "******************"

    resp = prepareFlows(Agent, FlowInfos, JumpUrl)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

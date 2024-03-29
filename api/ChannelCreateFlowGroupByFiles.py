from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateFlowGroupByFiles(agent, flow_file_infos, flow_group_name):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateFlowGroupByFilesRequest()

        req.Agent = agent

        req.FlowFileInfos = flow_file_infos

        req.FlowGroupName = flow_group_name

        # 返回的resp是一个ChannelCreateFlowGroupByFilesResponse的实例，与请求对象对应
        return client.ChannelCreateFlowGroupByFiles(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    FlowGroupName = "合同组名称"

    flowFileInfo = models.FlowFileInfo()
    flowFileInfo.FileIds = ["******************"]
    flowFileInfo.FlowName = "子合同名称"

    flowApprover = models.FlowApproverInfo()
    flowApprover.Name = "******************"
    flowApprover.IdCardType = ""
    flowApprover.IdCardNumber = ""
    flowApprover.Mobile = "******************"
    flowApprover.OrganizationName = ""
    flowApprover.NotChannelOrganization = False
    flowApprover.OpenId = ""
    flowApprover.OrganizationOpenId = ""
    flowApprover.ApproverType = "PERSON"
    flowApprover.RecipientId = ""
    flowApprover.Deadline = 0
    flowApprover.CallbackUrl = ""

    signComponent = models.Component()
    signComponent.ComponentId = ""
    signComponent.ComponentType = ""
    signComponent.ComponentName = ""
    signComponent.ComponentRecipientId = ""
    signComponent.FileIndex = 0
    signComponent.GenerateMode = ""
    signComponent.ComponentWidth = 100.00
    signComponent.ComponentHeight = 100.00
    signComponent.ComponentPage = 1
    signComponent.ComponentPosX = 100.00
    signComponent.ComponentPosY = 100.00
    flowApprover.SignComponents = [signComponent]

    flowFileInfo.FlowApprovers = [flowApprover]
    flowFileInfo.Deadline = 0
    flowFileInfo.FlowDescription = "子合同描述"
    flowFileInfo.FlowType = "合同类型"
    flowFileInfo.CallbackUrl = ""
    flowFileInfo.CustomerData = ""
    flowFileInfo.Unordered = True
    flowFileInfo.CustomShowMap = ""
    flowFileInfo.NeedSignReview = False

    FlowFileInfos = [flowFileInfo, flowFileInfo]

    resp = channelCreateFlowGroupByFiles(Agent, FlowFileInfos, FlowGroupName)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

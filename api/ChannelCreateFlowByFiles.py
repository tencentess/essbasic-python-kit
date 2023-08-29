from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models
from tencentcloud.essbasic.v20210526.models import FlowApproverInfo, Component

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateFlowByFiles(agent, flow_approver_infos, flow_name, file_id):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateFlowByFilesRequest()

        req.FlowName = flow_name

        req.FileIds = [file_id]

        req.Agent = agent

        req.FlowApprovers = flow_approver_infos

        # 返回的resp是一个ChannelCreateFlowByFilesResponse的实例，与请求对象对应
        return client.ChannelCreateFlowByFiles(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':

    FileId = "********************************"

    FlowName = "我的第一份文件合同"
    # 第三方平台应用相关信息。
    Agent = fillAgent()
    FlowApproverInfos = []

    # 签署方参与信息
    flowApproverInfo = FlowApproverInfo()

    flowApproverInfo.ApproverType = "PERSON"

    flowApproverInfo.Name = "*****"

    flowApproverInfo.Mobile = "**************"
    component = Component()

    component.ComponentPosX = 146.15625

    component.ComponentPosY = 472.78125

    component.ComponentWidth = 112

    component.ComponentHeight = 40

    component.FileIndex = 0

    component.ComponentType = "SIGN_SIGNATURE"

    component.ComponentPage = 1

    component.ComponentValue = ""
    
    FlowApproverInfo.SignComponents = [component]
    FlowApproverInfos.append(flowApproverInfo)

    resp = channelCreateFlowByFiles(Agent, FlowApproverInfos, FlowName, FileId)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

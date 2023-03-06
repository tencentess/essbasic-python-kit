from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def createChannelFlowEvidenceReport(agent, flow_id):
    """
        创建出证报告，返回报告 ID
        详细参考 https://cloud.tencent.com/document/api/1420/79688
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.CreateChannelFlowEvidenceReportRequest()

        # 传入相关参数
        # 第三方平台应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        req.Agent = agent
        # 合同Id，流程Id
        req.FlowId = flow_id

        # 返回的resp是一个CreateChannelFlowEvidenceReportResponse的实例，与请求对象对应
        return client.CreateChannelFlowEvidenceReport(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()
    FlowId = "******************"

    resp = createChannelFlowEvidenceReport(Agent, FlowId)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

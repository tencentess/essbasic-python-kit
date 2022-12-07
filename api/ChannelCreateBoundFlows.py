from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateBoundFlows(agent, flow_ids):
    """
        此接口（CreateConsoleLoginUrl）用于渠道子客领取合同，经办人需要有相应的角色，领取后的合同不能重复领取
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateBoundFlowsRequest()

        # 传入相关参数
        # 渠道应用相关信息
        req.Agent = agent
        # 领取的合同id列表
        req.FlowIds = flow_ids

        # 返回的resp是一个ChannelCreateBoundFlowsResponse的实例，与请求对象对应
        return client.ChannelCreateBoundFlows(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 渠道应用相关信息
    Agent = fillAgent()
    FlowIds = ["******************"]

    resp = channelCreateBoundFlows(Agent, FlowIds)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

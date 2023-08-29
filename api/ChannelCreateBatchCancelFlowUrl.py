from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateBatchCancelFlowUrl(agent, flow_ids):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateBatchCancelFlowUrlRequest()

        req.Agent = agent

        req.FlowIds = flow_ids

        # 返回的resp是一个ChannelCreateBatchCancelFlowUrlResponse的实例，与请求对象对应
        return client.ChannelCreateBatchCancelFlowUrl(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()
    FlowIds = ["******************"]

    resp = channelCreateBatchCancelFlowUrl(Agent, FlowIds)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

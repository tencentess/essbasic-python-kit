from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelDescribeOrganizationSeals(agent, info_type, seal_id, limit, offset):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelDescribeOrganizationSealsRequest()

        req.Agent = agent

        req.InfoType = info_type

        req.SealId = seal_id

        req.Limit = limit

        req.Offset = offset

        # 返回的resp是一个ChannelDescribeOrganizationSealsResponse的实例，与请求对象对应
        return client.ChannelDescribeOrganizationSeals(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    InfoType = 1
    SealId = ""
    Limit = 10
    Offset = 0

    resp = channelDescribeOrganizationSeals(Agent, InfoType, SealId, Limit, Offset)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

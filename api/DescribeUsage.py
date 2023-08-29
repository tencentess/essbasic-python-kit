from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def describeUsage(agent, start_date, end_date, need_aggregate, limit, offset):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeUsageRequest()

        req.Agent = agent

        req.StartDate = start_date

        req.EndDate = end_date

        req.NeedAggregate = need_aggregate

        req.Limit = limit

        req.Offset = offset

        # 返回的resp是一个DescribeUsageResponse的实例，与请求对象对应
        return client.DescribeUsage(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    StartDate = "2022-06-01"
    EndDate = "2022-06-30"
    NeedAggregate = True
    Limit = 10
    Offset = 0

    resp = describeUsage(Agent, StartDate, EndDate, NeedAggregate, Limit, Offset)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

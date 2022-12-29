from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def describeUsage(agent, start_date, end_date, need_aggregate, limit, offset):
    """
        此接口（DescribeUsage）用于获取渠道所有合作企业流量消耗情况。
        注: 此接口每日限频2次，若要扩大限制次数,请提前与客服经理或邮件至e-contract@tencent.com进行联系。
        详细参考 https://cloud.tencent.com/document/api/1420/61520
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeUsageRequest()

        # 传入相关参数
        # 渠应用信息，此接口Agent.AppId必填
        req.Agent = agent
        # 开始时间，例如：2021-03-21
        req.StartDate = start_date
        # 结束时间，例如：2021-06-21；
        # 开始时间到结束时间的区间长度小于等于90天。
        req.EndDate = end_date
        # 是否汇总数据，默认不汇总。
        # 不汇总：返回在统计区间内渠道下所有企业的每日明细，即每个企业N条数据，N为统计天数；
        # 汇总：返回在统计区间内渠道下所有企业的汇总后数据，即每个企业一条数据；
        req.NeedAggregate = need_aggregate
        # 单次返回的最多条目数量。默认为1000，且不能超过1000。
        req.Limit = limit
        # 偏移量，默认是0。
        req.Offset = offset

        # 返回的resp是一个DescribeUsageResponse的实例，与请求对象对应
        return client.DescribeUsage(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 渠道应用相关信息
    Agent = fillAgent()

    StartDate = "2022-06-01"
    EndDate = "2022-06-30"
    NeedAggregate = True
    Limit = 10
    Offset = 0

    resp = describeUsage(Agent, StartDate, EndDate, NeedAggregate, Limit, Offset)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelDescribeEmployees(agent, filters, limit, offset):
    """
        查询企业员工列表
        详细参考 https://cloud.tencent.com/document/api/1420/81119
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelDescribeEmployeesRequest()

        # 传入相关参数
        # 第三方平台应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        req.Agent = agent
        # 查询过滤实名用户，Key为Status，Values为["IsVerified"]
        # 根据第三方系统openId过滤查询员工时,Key为StaffOpenId,Values为["OpenId","OpenId",...]
        # 查询离职员工时，Key为Status，Values为["QuiteJob"]
        req.Filters = filters
        # 返回最大数量，最大为20
        req.Limit = limit
        # 偏移量，默认为0，最大为20000
        req.Offset = offset

        # 返回的resp是一个ChannelDescribeEmployeesResponse的实例，与请求对象对应
        return client.ChannelDescribeEmployees(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    Filter = models.Filter()
    Filter.Key = "IsVerified"
    Filter.Values = []

    Filters = [Filter]
    Limit = 10
    Offset = 0

    resp = channelDescribeEmployees(Agent, Filters, Limit, Offset)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

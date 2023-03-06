from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelDescribeOrganizationSeals(agent, info_type, seal_id, limit, offset):
    """
        查询子客企业电子印章，需要操作者具有管理印章权限
        客户指定需要获取的印章数量和偏移量，数量最多100，超过100按100处理；
        入参InfoType控制印章是否携带授权人信息，为1则携带，为0则返回的授权人信息为空数组。
        接口调用成功返回印章的信息列表还有企业印章的总数。
        详细参考 https://cloud.tencent.com/document/api/1420/82455
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelDescribeOrganizationSealsRequest()

        # 传入相关参数
        # 第三方平台应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        req.Agent = agent
        # 查询信息类型，为1时返回授权用户，为其他值时不返回
        req.InfoType = info_type
        # 印章id（没有输入返回所有）
        req.SealId = seal_id
        # 返回最大数量，最大为100
        req.Limit = limit
        # 偏移量，默认为0，最大为20000
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

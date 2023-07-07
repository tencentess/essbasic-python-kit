from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def describeResourceUrlsByFlows(agent, flow_ids):
    """
        根据签署流程信息批量获取资源下载链接，可以下载签署中、签署完的合同，需合作企业先进行授权。
        此接口直接返回下载的资源的url，与接口GetDownloadFlowUrl跳转到控制台的下载方式不同。
        详细参考 https://cloud.tencent.com/document/api/1420/63220
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeResourceUrlsByFlowsRequest()

        # 第三方平台应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        req.Agent = agent
        # 查询资源所对应的签署流程Id，最多支持50个
        req.FlowIds = flow_ids

        # 返回的resp是一个DescribeResourceUrlsByFlowsResponse的实例，与请求对象对应
        return client.DescribeResourceUrlsByFlows(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()
    # 资源所对应的签署流程Id
    FlowIds = ["****************"]
    resp = describeResourceUrlsByFlows(Agent, FlowIds)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

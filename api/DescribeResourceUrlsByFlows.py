from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models
from common.CreateFlowUtils import initClient, fillAgent


def describeResourceUrlsByFlows(Agent, FlowIds):
    """
        根据签署流程信息批量获取资源下载链接，需合作企业先进行授权
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeResourceUrlsByFlowsRequest()

        # 渠道应用相关信息
        req.Agent = Agent
        # 资源所对应的签署流程Id
        req.FlowIds = FlowIds

        # 返回的resp是一个DescribeResourceUrlsByFlowsResponse的实例，与请求对象对应
        resp = client.DescribeResourceUrlsByFlows(req)

        return resp
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 渠道应用相关信息
    Agent = fillAgent()
    # 资源所对应的签署流程Id
    FlowIds = ["****************"]
    resp = describeResourceUrlsByFlows(Agent, FlowIds)
    # 输出json格式的字符串回包
    print(resp.to_json_string())
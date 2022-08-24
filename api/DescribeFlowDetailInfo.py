from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def describeFlowDetailInfo(Agent, FlowIds):
    """
        此接口用于查询合同(签署流程)的详细信息。
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeFlowDetailInfoRequest()

        # 渠道应用相关信息
        req.Agent = Agent
        # 资源所对应的签署流程Id
        req.FlowIds = FlowIds

        # 返回的resp是一个DescribeFlowDetailInfoResponse的实例，与请求对象对应
        resp = client.DescribeFlowDetailInfo(req)

        return resp

    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 渠道应用相关信息
    Agent = fillAgent()
    # 发起合同成功的签署流程Id
    FlowIds = ["****************"]
    resp = describeFlowDetailInfo(Agent, FlowIds)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

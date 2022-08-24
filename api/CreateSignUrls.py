from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def createSignUrls(Agent, FlowIds):
    """
        创建跳转小程序查看或签署的链接；自动签署的签署方不创建签署链接；
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.CreateSignUrlsRequest()

        # 渠道应用相关信息
        req.Agent = Agent
        # 资源所对应的签署流程Id
        req.FlowIds = FlowIds

        # 返回的resp是一个CreateSignUrlsResponse的实例，与请求对象对应
        resp = client.CreateSignUrls(req)

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
    resp = createSignUrls(Agent, FlowIds)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

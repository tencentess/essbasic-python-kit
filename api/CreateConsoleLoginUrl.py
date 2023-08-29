from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def createConsoleLoginUrl(agent, proxy_organization_name):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.CreateConsoleLoginUrlRequest()

        agent.ProxyAppId = ""
        req.Agent = agent

        req.ProxyOrganizationName = proxy_organization_name

        # 返回的resp是一个CreateConsoleLoginUrlResponse的实例，与请求对象对应
        return client.CreateConsoleLoginUrl(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    Agent = fillAgent()
    ProxyOrganizationName = "**************"
    resp = createConsoleLoginUrl(Agent, ProxyOrganizationName)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

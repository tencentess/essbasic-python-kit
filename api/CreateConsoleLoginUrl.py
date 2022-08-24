from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def createConsoleLoginUrl(Agent, ProxyOrganizationName):
    """
      用于创建电子签控制台登录链接。若企业未激活，调用同步企业信息、同步经办人信息
    """

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.CreateConsoleLoginUrlRequest()

        # 渠道应用相关信息
        req.Agent = Agent
        # 渠道侧合作企业名称，最大长度64个字符
        req.ProxyOrganizationName = ProxyOrganizationName

        # 返回的resp是一个CreateConsoleLoginUrlResponse的实例，与请求对象对应
        resp = client.CreateConsoleLoginUrl(req)

        return resp
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

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from byfile.Byfile import convertImageFileToBase64
from common.CreateFlowUtils import initClient, fillAgent


def syncProxyOrganization(agent, proxy_organization_name, business_license,
                          uniform_social_credit_code, proxy_legal_name):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.SyncProxyOrganizationRequest()

        req.Agent = agent

        req.ProxyOrganizationName = proxy_organization_name

        req.BusinessLicense = business_license

        req.UniformSocialCreditCode = uniform_social_credit_code

        req.ProxyLegalName = proxy_legal_name

        # 返回的resp是一个SyncProxyOrganizationResponse的实例，与请求对象对应
        return client.SyncProxyOrganization(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    ProxyOrganizationName = "******************"
    BusinessLicense = convertImageFileToBase64("../test/test_businessLicense.png")
    UniformSocialCreditCode = "******************"
    ProxyLegalName = "******************"

    resp = syncProxyOrganization(Agent, ProxyOrganizationName, BusinessLicense,
                                 UniformSocialCreditCode, ProxyLegalName)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

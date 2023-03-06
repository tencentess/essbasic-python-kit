from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from byfile.Byfile import convertImageFileToBase64
from common.CreateFlowUtils import initClient, fillAgent


def syncProxyOrganization(agent, proxy_organization_name, business_license,
                          uniform_social_credit_code, proxy_legal_name):
    """
        用于同步子客企业信息，主要是子客企业的营业执照，便于子客企业开通过程中不用手动上传。
        若有需要调用此接口，需要在创建控制链接CreateConsoleLoginUrl之后即刻进行调用。
        详细参考 https://cloud.tencent.com/document/api/1420/61518
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.SyncProxyOrganizationRequest()

        # 传入相关参数
        # 第三方平台应用相关信息
        # 此接口Agent.AppId、Agent.ProxyOrganizationOpenId必填
        req.Agent = agent
        # 子客企业名称，最大长度64个字符
        req.ProxyOrganizationName = proxy_organization_name
        # 营业执照正面照(PNG或JPG)
        # base64格式, 大小不超过5M
        req.BusinessLicense = business_license
        # 子客企业统一社会信用代码，最大长度200个字符
        req.UniformSocialCreditCode = uniform_social_credit_code
        # 子客企业法人/负责人姓名
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

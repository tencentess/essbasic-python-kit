from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from byfile.Byfile import convertImageFileToBase64
from common.CreateFlowUtils import initClient, fillAgent


def syncProxyOrganization(agent, proxy_organization_name, business_license,
                          uniform_social_credit_code, proxy_legal_name):
    """
        此接口（SyncProxyOrganization）用于针对渠道模板库中的模板对子客企业可见性的查询和设置，不会直接分配渠道模板给子客企业。
        1、OperateType=select时：
        查询渠道模板库
        2、OperateType=update或者delete时：
        对子客企业进行模板库中模板可见性的修改、删除操作。
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.SyncProxyOrganizationRequest()

        # 传入相关参数
        # 渠道应用相关信息
        req.Agent = agent
        # 渠道侧合作企业名称，最大长度64个字符
        req.ProxyOrganizationName = proxy_organization_name
        # 营业执照正面照(PNG或JPG)
        # base64格式, 大小不超过5M
        req.BusinessLicense = business_license
        # 渠道侧合作企业统一社会信用代码，最大长度200个字符
        req.UniformSocialCreditCode = uniform_social_credit_code
        # 渠道侧合作企业法人 / 负责人姓名
        req.ProxyLegalName = proxy_legal_name

        # 返回的resp是一个SyncProxyOrganizationResponse的实例，与请求对象对应
        return client.SyncProxyOrganization(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 渠道应用相关信息
    Agent = fillAgent()

    ProxyOrganizationName = "******************"
    BusinessLicense = convertImageFileToBase64("../test/test_businessLicense.png")
    UniformSocialCreditCode = "******************"
    ProxyLegalName = "******************"

    resp = syncProxyOrganization(Agent, ProxyOrganizationName, BusinessLicense,
                                 UniformSocialCreditCode, ProxyLegalName)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

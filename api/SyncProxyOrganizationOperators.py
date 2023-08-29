from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def syncProxyOrganizationOperators(agent, operator_type, proxy_organization_operators):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.SyncProxyOrganizationOperatorsRequest()

        req.Agent = agent

        req.OperatorType = operator_type

        req.ProxyOrganizationOperators = proxy_organization_operators

        # 返回的resp是一个SyncProxyOrganizationOperatorsResponse的实例，与请求对象对应
        return client.SyncProxyOrganizationOperators(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    OperatorType = "CREATE"

    proxyOrganizationOperator = models.ProxyOrganizationOperator()
    proxyOrganizationOperator.Id = "******************"
    proxyOrganizationOperator.Name = "******************"
    proxyOrganizationOperator.IdCardType = "******************"
    proxyOrganizationOperator.IdCardNumber = "******************"
    proxyOrganizationOperator.Mobile = "******************"
    ProxyOrganizationOperators = [proxyOrganizationOperator]

    resp = syncProxyOrganizationOperators(Agent, OperatorType, ProxyOrganizationOperators)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

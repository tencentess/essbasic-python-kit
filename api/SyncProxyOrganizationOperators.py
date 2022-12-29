from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def syncProxyOrganizationOperators(agent, operator_type, proxy_organization_operators):
    """
        用于同步渠道子客企业经办人列表，主要是同步经办人的离职状态。
        子客Web控制台的组织架构管理，是依赖于渠道平台的，无法针对员工做新增/更新/离职等操作。
        若经办人信息有误，或者需要修改，也可以先将之前的经办人做离职操作，然后重新使用控制台链接CreateConsoleLoginUrl让经办人重新实名。
        详细参考 https://cloud.tencent.com/document/api/1420/61517
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.SyncProxyOrganizationOperatorsRequest()

        # 传入相关参数
        # 渠道应用相关信息
        # 此接口Agent.AppId 和 Agent.ProxyOrganizationOpenId必填。
        req.Agent = agent
        # 操作类型，新增: "CREATE"，修改: "UPDATE"，离职: "RESIGN"
        req.OperatorType = operator_type
        # 经办人信息列表，最大长度200
        req.ProxyOrganizationOperators = proxy_organization_operators

        # 返回的resp是一个SyncProxyOrganizationOperatorsResponse的实例，与请求对象对应
        return client.SyncProxyOrganizationOperators(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 渠道应用相关信息
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

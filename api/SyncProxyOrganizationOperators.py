from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def syncProxyOrganizationOperators(agent, operator_type, proxy_organization_operators):
    """
        此接口（SyncProxyOrganizationOperators）用于针对渠道模板库中的模板对子客企业可见性的查询和设置，不会直接分配渠道模板给子客企业。
        1、OperateType=select时：
        查询渠道模板库
        2、OperateType=update或者delete时：
        对子客企业进行模板库中模板可见性的修改、删除操作。
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.SyncProxyOrganizationOperatorsRequest()

        # 传入相关参数
        # 渠道应用相关信息
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

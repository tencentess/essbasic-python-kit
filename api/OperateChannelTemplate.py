from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def operateChannelTemplate(agent, operate_type, template_id, proxy_organization_open_ids, auth_tag):
    """
        用于针对平台企业模板库中的模板对子客企业可见性的查询和设置，不会直接分配平台企业模板给子客企业。
        1、OperateType=select时：
        查询平台企业模板库
        2、OperateType=update或者delete时：
        对子客企业进行模板库中模板可见性的修改、删除操作。
        详细参考 https://cloud.tencent.com/document/api/1420/66367
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.OperateChannelTemplateRequest()

        # 传入相关参数
        # 第三方平台应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        req.Agent = agent
        # 操作类型，查询:"SELECT"，删除:"DELETE"，更新:"UPDATE"
        req.OperateType = operate_type
        # 平台企业模板库模板唯一标识
        req.TemplateId = template_id
        # 合作企业方第三方机构唯一标识数据，支持多个， 用","进行分隔
        req.ProxyOrganizationOpenIds = proxy_organization_open_ids
        # 模板可见性, 全部可见-"all", 部分可见-"part"
        req.AuthTag = auth_tag

        # 返回的resp是一个OperateChannelTemplateResponse的实例，与请求对象对应
        return client.OperateChannelTemplate(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    OperateType = "SELECT"
    TemplateId = "******************"
    ProxyOrganizationOpenIds = "******************"
    AuthTag = "all"

    resp = operateChannelTemplate(Agent, OperateType, TemplateId, ProxyOrganizationOpenIds, AuthTag)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

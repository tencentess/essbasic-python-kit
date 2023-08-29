from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def operateChannelTemplate(agent, operate_type, template_id, proxy_organization_open_ids, auth_tag):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.OperateChannelTemplateRequest()

        req.Agent = agent

        req.OperateType = operate_type

        req.TemplateId = template_id

        req.ProxyOrganizationOpenIds = proxy_organization_open_ids

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

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def describeTemplates(agent, template_id):
    """
        DescribeTemplates 查询该子客企业在电子签拥有的有效模板，不包括平台企业模板
        详细参考 https://cloud.tencent.com/document/api/1420/61521
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeTemplatesRequest()

        # 第三方平台应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        req.Agent = agent
        # 模板唯一标识，查询单个模板时使用
        req.TemplateId = template_id

        # 其他查询参数参考官网文档
        # https://cloud.tencent.com/document/api/1420/61521

        # 返回的resp是一个DescribeTemplatesResponse的实例，与请求对象对应
        return client.DescribeTemplates(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 模板唯一标识
    TemplateId = "***************"
    # 第三方平台应用相关信息
    Agent = fillAgent()
    resp = describeTemplates(Agent, TemplateId)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

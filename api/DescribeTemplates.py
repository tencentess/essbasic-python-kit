from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def describeTemplates(agent, template_id):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeTemplatesRequest()

        req.Agent = agent

        req.TemplateId = template_id

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

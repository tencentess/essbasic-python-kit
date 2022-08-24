from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from api.DescribeTemplates import describeTemplates
from bytemplate.ByTemplate import BuildApprovers
from common.CreateFlowUtils import initClient, fillAgent, fillFlowInfo


def createFlowsByTemplates(Agent, FlowInfos):
    """
        用于使用多个模板批量创建签署流程。当前可批量发起合同（签署流程）数量最大为20个。
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.CreateFlowsByTemplatesRequest()

        # 渠道应用相关信息
        req.Agent = Agent
        # 多个合同（签署流程）信息
        req.FlowInfos = FlowInfos

        # 返回的resp是一个CreateFlowsByTemplatesResponse的实例，与请求对象对应
        resp = client.CreateFlowsByTemplates(req)

        return resp

    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    TemplateId = "***************"
    FlowName = "我的第一份合同"
    Agent = fillAgent()
    templatesResponse = describeTemplates(Agent, TemplateId)
    RecipientId = templatesResponse.Templates[0].Recipients[0].RecipientId
    FlowInfos = []

    flowApproverInfos = BuildApprovers(RecipientId)
    FlowInfos.append(fillFlowInfo(TemplateId, FlowName, flowApproverInfos))

    resp = createFlowsByTemplates(Agent, FlowInfos)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

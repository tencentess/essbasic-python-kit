from api.CreateFlowsByTemplates import createFlowsByTemplates
from api.CreateSignUrls import createSignUrls
from api.DescribeResourceUrlsByFlows import describeResourceUrlsByFlows
from bytemplate.ByTemplate import BuildApprovers, BuildFormField
from common.CreateFlowUtils import fillFlowInfo, fillAgent
from config.Config import COUNT


def createFlowByTemplateDirectly(FlowName, TemplateId, FlowApproverInfos):
    """
        通过合同名和模板Id直接发起签署流程
    """
    resp = {}

    # 创建签署流程
    # 签署数量
    count = COUNT
    FlowInfos = []
    for i in range(count):
        # 构建内容控件填充结构(根据自己需求使用)
        # FlowInfos[i].FormFields = [BuildFormField("姓名", "张三")]
        FlowInfos.append(fillFlowInfo(TemplateId, FlowName, FlowApproverInfos))

    # 设置渠道应用相关信息
    Agent = fillAgent()

    # 发起签署
    flowResponse = createFlowsByTemplates(Agent, FlowInfos)
    FlowIds = flowResponse.FlowIds
    resp['FlowIds'] = FlowIds
    # 获取签署链接
    createSignUrlsRes = createSignUrls(Agent, FlowIds)
    SignUrlInfos = createSignUrlsRes.SignUrlInfos
    Urls = []
    for i in SignUrlInfos:
        Urls.append(i.SignUrl)
    resp['Urls'] = Urls

    urlResp = describeResourceUrlsByFlows(Agent, FlowIds)
    FlowResourceUrlInfos = urlResp.FlowResourceUrlInfos
    DownloadUrls = []
    for i in FlowResourceUrlInfos:
        DownloadUrls.append(i.ResourceUrlInfos[0].Url)
    resp['DownloadUrls'] = DownloadUrls
    return resp

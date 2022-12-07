from api.CreateFlowsByTemplates import createFlowsByTemplates
from api.CreateSignUrls import createSignUrls
from api.DescribeResourceUrlsByFlows import describeResourceUrlsByFlows
from common.CreateFlowUtils import fillFlowInfo, fillAgent
from config.Config import COUNT


def createFlowByTemplateDirectly(flow_name, template_id, flow_approver_infos):
    """
        通过合同名和模板Id直接发起签署流程
    """
    resp = {}

    # 创建签署流程
    # 签署数量
    count = COUNT
    flow_infos = []
    for i in range(count):
        # 构建内容控件填充结构(根据自己需求使用)
        # FlowInfos[i].FormFields = [BuildFormField("姓名", "张三")]
        flow_infos.append(fillFlowInfo(template_id, flow_name, flow_approver_infos))

    # 设置渠道应用相关信息
    agent = fillAgent()

    # 发起签署
    flow_response = createFlowsByTemplates(agent, flow_infos)
    flow_ids = flow_response.FlowIds
    resp['FlowIds'] = flow_ids
    # 获取签署链接
    create_sign_urls_res = createSignUrls(agent, flow_ids)
    sign_url_infos = create_sign_urls_res.SignUrlInfos
    urls = []
    for i in sign_url_infos:
        urls.append(i.SignUrl)
    resp['Urls'] = urls

    url_resp = describeResourceUrlsByFlows(agent, flow_ids)
    flow_resource_url_infos = url_resp.FlowResourceUrlInfos
    download_urls = []
    for i in flow_resource_url_infos:
        download_urls.append(i.ResourceUrlInfos[0].Url)
    resp['DownloadUrls'] = download_urls
    return resp

from api.CreateConsoleLoginUrl import createConsoleLoginUrl
from api.DescribeTemplates import describeTemplates
from common.CreateFlowUtils import fillAgent


def describeConsoleUrlRecIdAndTemplateId(ProxyOrganizationName, TemplateId):
    """
        获取创建控制台链接和RecipientId
    """
    RecipientIdAndConsoleUrl = {}

    # 设置渠道应用相关信息
    Agent = fillAgent()

    # 创建控制台链接
    loginUrlResponse = createConsoleLoginUrl(Agent, ProxyOrganizationName)
    ConsoleUrl = loginUrlResponse.ConsoleUrl
    RecipientIdAndConsoleUrl['ConsoleUrl'] = ConsoleUrl

    # 查询模板信息列表
    templatesResponse = describeTemplates(Agent, TemplateId)
    RecipientId = templatesResponse.Templates[0].Recipients[0].RecipientId
    RecipientIdAndConsoleUrl['RecipientId'] = RecipientId

    return RecipientIdAndConsoleUrl

import os
import sys

from api.CreateConsoleLoginUrl import createConsoleLoginUrl
from common.CreateFlowUtils import fillAgent

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.CreateFlowByTemplateDirectly import createFlowByTemplateDirectly
from bytemplate.ByTemplate import GetRecipients, BuildApprovers
from config.Config import *

'''
    使用模板发起合同QuickStart
'''


def ByTemplateQuickStart():
    # Step 1
    # 定义合同名
    FlowName = "我的第一个合同"
    # 渠道侧合作企业名称
    ProxyOrganizationName = "好企业"

    # 此处为快速发起；如果是正式接入，构造签署人，请参考函数内说明，构造需要的场景参数
    # Step 2
    # 获取RecipientId
    RecipientId = GetRecipients(TemplateId)
    # 构造签署人信息
    FlowApproverInfos = BuildApprovers(RecipientId)
    # 创建控制台链接
    loginUrlResponse = createConsoleLoginUrl(fillAgent(), ProxyOrganizationName)
    # 发起合同
    resp = createFlowByTemplateDirectly(FlowName, TemplateId, FlowApproverInfos)

    # 设置数量
    count = COUNT

    #  返回相关信息
    print("您的控制台入口为：")
    print(loginUrlResponse.ConsoleUrl)
    print("\r\n\r\n")
    for i in range(count):
        print("您创建的合同id为：")
        print(resp.get("FlowIds")[i])
        print("\r\n\r\n")
        # 返回签署的链接
        print("签署链接为：")
        print(resp.get("Urls")[i])
        print("\r\n\r\n")
        # Step 3
        # 下载合同
        # 返回合同下载链接
        print("请访问以下地址下载您的合同：")
        print(resp.get("DownloadUrls")[0])
        print("\r\n\r\n")


if __name__ == '__main__':
    ByTemplateQuickStart()

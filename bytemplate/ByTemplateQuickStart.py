import os
import sys

from ByTemplate import GetRecipients, BuildApprovers

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.CreateFlowUtils import fillAgent
from api.CreateConsoleLoginUrl import createConsoleLoginUrl
from api.CreateFlowByTemplateDirectly import createFlowByTemplateDirectly
from config.Config import *

'''
本示例用于渠道版接口对接，通过模板快速发起第一份合同
建议配合文档进行操作，先修改config里的基本参数以及对应环境域名，然后跑一次
渠道版主要针对渠道企业-代理子客发起合同，简要步骤主要是
    1. 通过CreateConsoleLoginUrl引导子客企业完成电子签的实名认证 - 子客企业在电子签配置印章等
    2. 通过简单封装的CreateFlowByTemplateDirectly接口快速发起一份合同，并得到签署链接
    3. 在小程序签署合同，通过API下载合同
    基于具体业务上的参数调用，可以参考官网的接口说明 
https://cloud.tencent.com/document/product/1420/61534
每个API的封装在api目录下可以自己配合相关参数进行调用
'''
def ByTemplateQuickStart():
    # Step 1 登录子客控制台
    # 渠道子客企业真实名称
    ProxyOrganizationName = "好企业"

    # 创建控制台链接
    loginUrlResponse = createConsoleLoginUrl(fillAgent(), ProxyOrganizationName)

    # Step 2 发合同
     # 此处为快速发起；如果是正式接入，构造签署人，请参考函数内说明，构造需要的场景参数

     # 定义合同名
    FlowName = "我的第一个合同"

    # 获取模板里面的参与方RecipientId
    RecipientId = GetRecipients(TemplateId)

    # 构造签署人信息
    FlowApproverInfos = BuildApprovers(RecipientId)
    
    # 发起合同
    resp = createFlowByTemplateDirectly(FlowName, TemplateId, FlowApproverInfos)

    #  返回相关信息
    print("您的控制台入口为：")
    print(loginUrlResponse.ConsoleUrl)
    print("\r\n\r\n")

    count = COUNT
    for i in range(count):
        print("您创建的合同id为：")
        print(resp.get("FlowIds")[i])
        print("\r\n\r\n")

        # 返回签署的链接
        print("签署链接为：")
        print(resp.get("Urls")[i])
        print("\r\n\r\n")

        # Step 3 下载合同
        # 返回合同下载链接
        print("请访问以下地址下载您的合同：")
        print(resp.get("DownloadUrls")[0])
        print("\r\n\r\n")


if __name__ == '__main__':
    ByTemplateQuickStart()

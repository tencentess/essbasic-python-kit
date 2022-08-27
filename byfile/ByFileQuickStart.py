import os
import sys

from api.CreateConsoleLoginUrl import createConsoleLoginUrl
from common.CreateFlowUtils import fillAgent

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.CreateFlowByFileDirectly import createFlowByFileDirectly
from Byfile import BuildApprovers, convertImageFileToBase64

'''
    使用文件发起合同QuickStart
'''


def ByFileQuickStart():
    # Step 1
    # 定义文件所在的路径
    FilePath = "test/blank.pdf"
    # 合同名
    FlowName = "我的第一个合同"
    # 渠道侧合作企业名称
    ProxyOrganizationName = "好企业"

    # 此处为快速发起；如果是正式接入，构造签署人，请参考函数内说明，构造需要的场景参数
    FlowApproverInfos = BuildApprovers()
    # 创建控制台链接
    loginUrlResponse = createConsoleLoginUrl(fillAgent(), ProxyOrganizationName)

    # Step 2
    # 将文件处理为Base64编码后的文件内容
    fileBase64 = convertImageFileToBase64(FilePath)

    # 发起合同
    resp = createFlowByFileDirectly(fileBase64, FlowApproverInfos, FlowName)

    print("您的控制台入口为：")
    print(loginUrlResponse.ConsoleUrl)
    print("\r\n\r\n")
    # 返回合同Id
    print("您创建的合同id为：")
    print(resp.get("FlowId"))
    print("\r\n\r\n")
    # 返回签署的链接
    print("签署链接为：")
    print(resp.get("Url"))
    print("\r\n\r\n")
    # Step 3
    # 下载合同
    # 返回合同下载链接
    print("请访问以下地址下载您的合同：")
    print(resp.get("downloadUrl"))
    print("\r\n\r\n")


if __name__ == '__main__':
    ByFileQuickStart()

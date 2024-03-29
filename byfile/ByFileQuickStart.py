import os
import sys

from Byfile import BuildApprovers, convertImageFileToBase64

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.CreateFlowUtils import fillAgent
from api.CreateConsoleLoginUrl import createConsoleLoginUrl
from api.CreateFlowByFileDirectly import createFlowByFileDirectly

'''
本示例用于第三方应用集成接口对接，通过文件快速发起第一份合同
建议配合文档进行操作，先修改config里的基本参数以及对应环境域名，然后跑一次
第三方应用集成主要针对平台企业-代理子客发起合同，简要步骤主要是
	1. 通过CreateConsoleLoginUrl引导子客企业完成电子签的实名认证 - 子客企业在电子签配置印章等
	2. 通过简单封装的CreateFlowByFileDirectly接口上传文件并快速发起一份合同，并得到签署链接
	3. 在小程序签署合同，通过API下载合同
基于具体业务上的参数调用，可以参考官网的接口说明 
https://cloud.tencent.com/document/product/1420/61534
每个API的封装在api目录下可以自己配合相关参数进行调用
'''
def ByFileQuickStart():
    # Step 1 登录子客控制台
    # 子客企业真实名称
    proxy_organization_name = "好企业"

    # 创建控制台链接
    login_url_response = createConsoleLoginUrl(fillAgent(), proxy_organization_name)

    # Step 2
    # 定义文件所在的路径
    file_path = "../test/blank.pdf"
    # 合同名
    flow_name = "我的第一个合同"
    # 将文件处理为Base64编码后的文件内容
    file_base64 = convertImageFileToBase64(file_path)

    # 此处为快速发起；如果是正式接入，构造签署人，请参考函数内说明，构造需要的场景参数
    flow_approver_infos = BuildApprovers()

    # 发起合同
    resp = createFlowByFileDirectly(file_base64, flow_approver_infos, flow_name)

    print("您的控制台入口为：")
    print(login_url_response.ConsoleUrl)
    print("\r\n\r\n")

    # 返回合同Id
    print("您创建的合同id为：")
    print(resp.get("FlowId"))
    print("\r\n\r\n")

    # 返回签署的链接
    print("签署链接为：")
    print(resp.get("Url"))
    print("\r\n\r\n")

    # Step 3 下载合同
    # 返回合同下载链接
    print("请访问以下地址下载您的合同：")
    print(resp.get("downloadUrl"))
    print("\r\n\r\n")

if __name__ == '__main__':
    ByFileQuickStart()

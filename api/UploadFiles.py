from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.essbasic.v20210526 import essbasic_client, models
from tencentcloud.essbasic.v20210526.models import UploadFile

from byfile.Byfile import convertImageFileToBase64
from common.CreateFlowUtils import fillAgent
from config.Config import *


def uploadFiles(agent, file_infos):
    """
         UploadFiles 用于生成pdf资源编号（FileIds）来配合“用PDF创建流程”接口使用，使用场景可详见“用PDF创建流程”接口说明。
         调用时需要设置Domain, 正式环境为 file.ess.tencent.cn
         测试环境为 https://file.test.ess.tencent.cn
         详细参考 https://cloud.tencent.com/document/api/1420/71479
    """
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户SecretId，SecretKey,此处还需注意密钥对的保密
        # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = FileServiceEndPoint

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = essbasic_client.EssbasicClient(cred, "", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.UploadFilesRequest()
        #
        # 1.TEMPLATE - 模板； 文件类型：.pdf
        # 2.DOCUMENT - 签署过程及签署后的合同文档 / 图片控件,文件类型：.pdf /.jpg /.png

        # 应用相关信息，AppId 和 ProxyOrganizationOpenId 必填
        req.Agent = agent
        # 上传文件内容数组，最多支持20个文件
        req.FileInfos = file_infos
        # 文件对应业务类型
	    #1. TEMPLATE - 模板； 文件类型：.pdf/.doc/.docx/.html
	    #2. DOCUMENT - 签署过程及签署后的合同文档/图片控件 文件类型：.pdf/.doc/.docx/.jpg/.png/.xls.xlsx/.html
        req.BusinessType = 'DOCUMENT'

        # 返回的resp是一个UploadFilesResponse的实例，与请求对象对应
        resp = client.UploadFiles(req)

        return resp
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()
    FilePath = "../test/blank.pdf"
    FileInfo = UploadFile()
    FileInfo.FileBody = convertImageFileToBase64(FilePath)
    FileInfos = [FileInfo]
    resp = uploadFiles(Agent, FileInfos)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

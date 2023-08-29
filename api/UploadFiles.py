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

        req.Agent = agent

        req.FileInfos = file_infos

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

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from byfile.Byfile import convertImageFileToBase64
from common.CreateFlowUtils import initClient, fillAgent


def createSealByImage(agent, seal_name, seal_image):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.CreateSealByImageRequest()

        req.Agent = agent

        req.SealName = seal_name

        req.SealImage = seal_image

        # 返回的resp是一个CreateSealByImageResponse的实例，与请求对象对应
        return client.CreateSealByImage(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    SealName = "印章名称"
    SealImage = convertImageFileToBase64("../test/test_seal.png")

    resp = createSealByImage(Agent, SealName, SealImage)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

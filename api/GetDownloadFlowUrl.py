from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models
from tencentcloud.essbasic.v20210526.models import DownloadFlowInfo

from common.CreateFlowUtils import initClient, fillAgent


def getDownloadFlowUrl(agent, down_load_flows):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.GetDownloadFlowUrlRequest()

        req.Agent = agent

        req.DownLoadFlows = down_load_flows

        # 返回的resp是一个GetDownloadFlowUrlResponse的实例，与请求对象对应
        return client.GetDownloadFlowUrl(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    downloadFlowInfo = DownloadFlowInfo()
    downloadFlowInfo.FileName = "文件夹名称"
    downloadFlowInfo.FlowIdList = ["******************"]

    DownLoadFlows = [downloadFlowInfo]

    resp = getDownloadFlowUrl(Agent, DownLoadFlows)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

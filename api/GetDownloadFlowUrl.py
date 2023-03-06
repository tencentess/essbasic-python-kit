from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models
from tencentcloud.essbasic.v20210526.models import DownloadFlowInfo

from common.CreateFlowUtils import initClient, fillAgent


def getDownloadFlowUrl(agent, down_load_flows):
    """
        此接口（GetDownloadFlowUrl）用于创建电子签批量下载地址，让合作企业进入控制台直接下载，支持客户合同（流程）按照自定义文件夹形式 分类下载。
        当前接口限制最多合同（流程）50个.
        详细参考 https://cloud.tencent.com/document/api/1420/66368
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.GetDownloadFlowUrlRequest()

        # 传入相关参数
        # 第三方平台应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        req.Agent = agent
        # 文件夹数组，签署流程总数不能超过50个，一个文件夹下，不能超过20个签署流程
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

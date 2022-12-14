from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCancelMultiFlowSignQRCode(agent, qr_code_id):
    """
        ChannelCancelMultiFlowSignQRCode 
        用于取消一码多扫二维码。该接口对传入的二维码ID，若还在有效期内，可以提前失效
        详细参考 https://cloud.tencent.com/document/api/1420/75453
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCancelMultiFlowSignQRCodeRequest()

        # 传入相关参数
        # 渠道应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        req.Agent = agent
        # 二维码ID
        req.QrCodeId = qr_code_id

        # 返回的resp是一个ChannelCancelMultiFlowSignQRCodeResponse的实例，与请求对象对应
        return client.ChannelCancelMultiFlowSignQRCode(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 渠道应用相关信息
    Agent = fillAgent()
    # 二维码ID
    QrCodeId = "******************"
    resp = channelCancelMultiFlowSignQRCode(Agent, QrCodeId)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateBatchCancelFlowUrl(agent, flow_ids):
    """
        ChannelCreateBatchCancelFlowUrl
        指定需要批量撤销的签署流程Id，获取批量撤销链接
        客户指定需要撤销的签署流程Id，最多100个，超过100不处理；
        接口调用成功返回批量撤销合同的链接，通过链接跳转到电子签小程序完成批量撤销;
        可以撤回：未全部签署完成；不可以撤回（终态）：已全部签署完成、已拒签、已过期、已撤回。
        注意:
        能撤回合同的只能是合同的发起人或者发起企业的超管、法人
        详细参考 https://cloud.tencent.com/document/api/1420/78264
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateBatchCancelFlowUrlRequest()

        # 传入相关参数
        # 渠道应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        req.Agent = agent
        # 签署流程Id数组
        req.FlowIds = flow_ids

        # 返回的resp是一个ChannelCreateBatchCancelFlowUrlResponse的实例，与请求对象对应
        return client.ChannelCreateBatchCancelFlowUrl(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 渠道应用相关信息
    Agent = fillAgent()
    FlowIds = ["******************"]

    resp = channelCreateBatchCancelFlowUrl(Agent, FlowIds)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

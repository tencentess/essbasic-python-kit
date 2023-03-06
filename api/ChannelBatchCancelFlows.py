from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelBatchCancelFlows(agent, flow_ids, cancel_message, cancel_message_format):
    """
        ChannelBatchCancelFlows
        指定需要批量撤销的签署流程Id，批量撤销合同
        客户指定需要撤销的签署流程Id，最多100个，超过100不处理；接口失败后返回错误信息
        注意:
        能撤回合同的只能是合同的发起人或者发起企业的超管、法人
        详细参考 https://cloud.tencent.com/document/api/1420/80391
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelBatchCancelFlowsRequest()

        # 传入相关参数
        # 第三方平台应用相关信息
	    # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        req.Agent = agent
        # 签署流程Id数组，最多100个，超过100不处理
        req.FlowIds = flow_ids
        # 撤回原因，最大不超过200字符
        req.CancelMessage = cancel_message
        # 撤销理由自定义格式；选项：
        # 0 默认格式
        # 1 只保留身份信息：展示为【发起方】
        # 2 保留身份信息+企业名称：展示为【发起方xxx公司】
        # 3 保留身份信息+企业名称+经办人名称：展示为【发起方xxxx公司-经办人姓名】
        req.CancelMessageFormat = cancel_message_format

        # 返回的resp是一个ChannelBatchCancelFlowsResponse的实例，与请求对象对应
        return client.ChannelBatchCancelFlows(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()
    FlowIds = ["******************"]
    CancelMessage = ""
    CancelMessageFormat = 3

    resp = channelBatchCancelFlows(Agent, FlowIds, CancelMessage, CancelMessageFormat)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

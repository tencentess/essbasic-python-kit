from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCancelFlow(agent, flow_id, cancel_message, cancel_message_format):
    """
        ChannelCancelFlow
        第三方应用集成撤销签署流程接口，可以撤回：未全部签署完成；不可以撤回（终态）：已全部签署完成、已拒签、已过期、已撤回。
        注意:
        能撤回合同的只能是合同的发起人或者发起企业的超管、法人
        详细参考 https://cloud.tencent.com/document/api/1420/81869
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCancelFlowRequest()

        # 传入相关参数
        # 第三方平台应用相关信息
        req.Agent = agent
        # 签署流程编号
        req.FlowId = flow_id
        # 撤回原因，最大不超过200字符
        req.CancelMessage = cancel_message
        # 撤销理由自定义格式；选项：
        # 0 默认格式
        # 1 只保留身份信息：展示为【发起方】
        # 2 保留身份信息+企业名称：展示为【发起方xxx公司】
        # 3 保留身份信息+企业名称+经办人名称：展示为【发起方xxxx公司-经办人姓名】
        req.CancelMessageFormat = cancel_message_format

        # 返回的resp是一个ChannelCancelFlowResponse的实例，与请求对象对应
        return client.ChannelCancelFlow(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()
    FlowId = "******************"
    CancelMessage = ""
    CancelMessageFormat = 3

    resp = channelCancelFlow(Agent, FlowId, CancelMessage, CancelMessageFormat)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

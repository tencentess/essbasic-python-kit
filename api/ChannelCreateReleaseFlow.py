from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateReleaseFlow(agent, need_relieved_flow_id, relive_info, released_approvers, callback_url):
    """
        第三方应用集成发起解除协议，主要应用场景为：基于一份已经签署的合同，进行解除操作。
        合同发起人必须在电子签已经进行实名。
        详细参考 https://cloud.tencent.com/document/api/1420/83461
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateReleaseFlowRequest()

        # 传入相关参数
        # 第三方平台应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        req.Agent = agent
        # 待解除的流程编号（即原流程的编号）
        req.NeedRelievedFlowId = need_relieved_flow_id
        # 解除协议内容
        # 详细参考 https://cloud.tencent.com/document/api/1420/61525#RelieveInfo
        req.ReliveInfo = relive_info
        # 非必须，解除协议的本企业签署人列表，默认使用原流程的签署人列表；
        # 当解除协议的签署人与原流程的签署人不能相同时（例如原流程签署人离职了），需要指定本企业的其他签署人来替换原流程中的原签署人，
        # 注意需要指明ApproverNumber来代表需要替换哪一个签署人，解除协议的签署人数量不能多于原流程的签署人数量
        req.ReleasedApprovers = released_approvers
        # 签署完回调url，最大长度1000个字符
        req.CallbackUrl = callback_url

        # 返回的resp是一个ChannelCreateReleaseFlowResponse的实例，与请求对象对应
        return client.ChannelCreateReleaseFlow(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()
    NeedRelievedFlowId = "******************"
    ReliveInfo = models.RelieveInfo()
    ReliveInfo.Reason = "******************"
    ReliveInfo.RemainInForceItem = "******************"
    ReliveInfo.OriginalExpenseSettlement = "******************"
    ReliveInfo.OriginalOtherSettlement = "******************"
    ReliveInfo.OtherDeals = "******************"

    releasedApprover = models.ReleasedApprover()
    releasedApprover.OrganizationName = "******************"
    releasedApprover.ApproverNumber = 0
    releasedApprover.ApproverType = "******************"
    releasedApprover.Name = "******************"
    releasedApprover.IdCardType = "******************"
    releasedApprover.IdCardNumber = "******************"
    releasedApprover.Mobile = "******************"
    releasedApprover.OrganizationOpenId = "******************"
    releasedApprover.OpenId = "******************"

    ReleasedApprovers = [releasedApprover]
    CallbackUrl = "******************"

    resp = channelCreateReleaseFlow(Agent, NeedRelievedFlowId, ReliveInfo, ReleasedApprovers, CallbackUrl)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

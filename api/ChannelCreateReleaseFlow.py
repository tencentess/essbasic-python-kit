from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateReleaseFlow(agent, need_relieved_flow_id, relive_info, released_approvers, callback_url):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateReleaseFlowRequest()

        req.Agent = agent

        req.NeedRelievedFlowId = need_relieved_flow_id

        req.ReliveInfo = relive_info

        req.ReleasedApprovers = released_approvers

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

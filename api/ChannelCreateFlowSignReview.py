from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateFlowSignReview(agent, flow_id, review_type, review_message, recipient_id):
    """
        提交企业签署流程审批结果

        在通过接口(CreateFlowsByTemplates 或者 ChannelCreateFlowByFiles)创建签署流程时，
        若指定了参数 NeedSignReview 为true,则可以调用此接口提交企业内部签署审批结果。
        若签署流程状态正常，且本企业存在签署方未签署，同一签署流程可以多次提交签署审批结果，签署时的最后一个“审批结果”有效。
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateFlowSignReviewRequest()

        # 传入相关参数
        # 渠道应用相关信息
        req.Agent = agent
        # 签署流程编号
        req.FlowId = flow_id
        # 企业内部审核结果
        # PASS: 通过
        # REJECT: 拒绝
        # SIGN_REJECT: 拒签(流程结束)
        req.ReviewType = review_type
        # 审核原因
        # 当 ReviewType 是 REJECT 时此字段必填, 字符串长度不超过200
        req.ReviewMessage = review_message
        # 签署节点审核时需要指定
        req.RecipientId = recipient_id

        # 返回的resp是一个ChannelCreateFlowSignReviewResponse的实例，与请求对象对应
        return client.ChannelCreateFlowSignReview(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 渠道应用相关信息
    Agent = fillAgent()

    FlowId = "******************"
    ReviewType = "******************"
    ReviewMessage = "******************"
    RecipientId = "******************"

    resp = channelCreateFlowSignReview(Agent, FlowId, ReviewType, ReviewMessage, RecipientId)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

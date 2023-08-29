from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateFlowSignReview(agent, flow_id, review_type, review_message, recipient_id):

    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateFlowSignReviewRequest()

        req.Agent = agent

        req.FlowId = flow_id

        req.ReviewType = review_type

        req.ReviewMessage = review_message

        req.RecipientId = recipient_id

        # 返回的resp是一个ChannelCreateFlowSignReviewResponse的实例，与请求对象对应
        return client.ChannelCreateFlowSignReview(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    FlowId = "******************"
    ReviewType = "******************"
    ReviewMessage = "******************"
    RecipientId = "******************"

    resp = channelCreateFlowSignReview(Agent, FlowId, ReviewType, ReviewMessage, RecipientId)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

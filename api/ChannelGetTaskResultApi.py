from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelGetTaskResultApi(agent, task_id):
    """
        第三方应用集成查询转换任务状态
        详细参考 https://cloud.tencent.com/document/api/1420/78773
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelGetTaskResultApiRequest()

        # 传入相关参数
        # 第三方平台应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        req.Agent = agent
        # 任务Id，通过ChannelCreateConvertTaskApi接口获得
        req.TaskId = task_id

        # 返回的resp是一个ChannelGetTaskResultApiResponse的实例，与请求对象对应
        return client.ChannelGetTaskResultApi(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    TaskId = "******************"

    resp = channelGetTaskResultApi(Agent, TaskId)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateConvertTaskApi(agent, resource_type, resource_name, resource_id):
    """
        平台企业创建文件转换任务
        详细参考 https://cloud.tencent.com/document/api/1420/78774
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateConvertTaskApiRequest()

        # 传入相关参数
        # 第三方平台应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        req.Agent = agent
        # 资源类型 取值范围doc,docx,html,xls,xlsx之一
        req.ResourceType = resource_type
        # 资源名称，长度限制为256字符
        req.ResourceName = resource_name
        # 资源Id，通过UploadFiles获取
        req.ResourceId = resource_id

        # 返回的resp是一个ChannelCreateConvertTaskApiResponse的实例，与请求对象对应
        return client.ChannelCreateConvertTaskApi(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息
    Agent = fillAgent()

    ResourceType = "excel"
    ResourceName = "资源名称"
    ResourceId = "******************"

    resp = channelCreateConvertTaskApi(Agent, ResourceType, ResourceName, ResourceId)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

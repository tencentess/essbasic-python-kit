from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateMultiFlowSignQRCode(agent, template_id, flow_name):
    """
        用于创建一码多扫流程签署二维码。
        适用场景：无需填写签署人信息，可通过模板id生成签署二维码，签署人可通过扫描二维码补充签署信息进行实名签署。常用于提前不知道签署人的身份信息场景，例如：劳务工招工、大批量员工入职等场景。
        适用的模板仅限于B2C（1、无序签署，2、顺序签署时B静默签署，3、顺序签署时B非首位签署）、单C的模板，且模板中发起方没有填写控件。
        详细参考 https://cloud.tencent.com/document/api/1420/75452
     """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateMultiFlowSignQRCodeRequest()

        # 第三方平台应用相关信息。
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 必填。
        req.Agent = agent
        # 模板Id
        req.TemplateId = template_id
        # 签署流程名称，最大长度200个字符
        req.FlowName = flow_name

        # 返回的resp是一个ChannelCreateMultiFlowSignQRCodeResponse的实例，与请求对象对应
        return client.ChannelCreateMultiFlowSignQRCode(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 第三方平台应用相关信息。
    Agent = fillAgent()
    TemplateId = "******************"
    FlowName = "******************"
    resp = channelCreateMultiFlowSignQRCode(Agent, TemplateId, FlowName)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

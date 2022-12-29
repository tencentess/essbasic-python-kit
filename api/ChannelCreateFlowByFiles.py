from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models
from tencentcloud.essbasic.v20210526.models import FlowApproverInfo, Component

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateFlowByFiles(agent, flow_approver_infos, flow_name, file_id):
    """
        用于渠道版通过文件创建签署流程。
        注意事项：该接口需要依赖“多文件上传”接口生成pdf资源编号（FileIds）进行使用。
        此接口静默签能力不可直接使用，需要运营申请
        详细参考 https://cloud.tencent.com/document/api/1420/73068
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateFlowByFilesRequest()

        # 签署流程名称，长度不超过200个字符
        req.FlowName = flow_name
        # 签署文件资源Id列表，目前仅支持单个文件
        req.FileIds = [file_id]

        # 渠道应用相关信息。 
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        req.Agent = agent
        # 签署流程签约方列表，最多不超过5个参与方
        req.FlowApprovers = flow_approver_infos

        # 其他更多参数和控制，参考文档 https://cloud.tencent.com/document/api/1420/73068
        # 也可以结合test case传参

        # 返回的resp是一个ChannelCreateFlowByFilesResponse的实例，与请求对象对应
        return client.ChannelCreateFlowByFiles(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 从UploadFiles接口获取到的fileId
    FileId = "********************************"
    # 签署流程名称, 最大长度200个字符
    FlowName = "我的第一份文件合同"
    # 渠道应用相关信息
    Agent = fillAgent()
    FlowApproverInfos = []

    # 签署方参与信息
    flowApproverInfo = FlowApproverInfo()
    # 签署人类型
    # PERSON-个人/自然人；
    # PERSON_AUTO_SIGN-个人自动签（定制化场景下使用）；
    # ORGANIZATION-企业（企业签署方或模板发起时的企业静默签）；
    # ENTERPRISESERVER-企业静默签（文件发起时的企业静默签字）。
    flowApproverInfo.ApproverType = "PERSON"
    # 操作人的名字
    flowApproverInfo.Name = "*****"
    # 操作人的手机号
    flowApproverInfo.Mobile = "**************"
    component = Component()
    # 参数控件X位置，单位px
    component.ComponentPosX = 146.15625
    # 参数控件Y位置，单位px
    component.ComponentPosY = 472.78125
    # 参数控件宽度，默认100，单位px，表单域和关键字转换控件不用填
    component.ComponentWidth = 112
    # 参数控件高度，默认100，单位px，表单域和关键字转换控件不用填
    component.ComponentHeight = 40
    # 控件所属文件的序号(文档中文件的排列序号，从0开始)
    component.FileIndex = 0

    # 如果是Component控件类型，则可选的字段为：
    # TEXT - 普通文本控件；
    # DATE - 普通日期控件；跟TEXT相比会有校验逻辑
    # DYNAMIC_TABLE - 动态表格控件
    # 如果是SignComponent控件类型，则可选的字段为
    # SIGN_SEAL - 签署印章控件；
    # SIGN_DATE - 签署日期控件；
    # SIGN_SIGNATURE - 用户签名控件；
    # SIGN_PERSONAL_SEAL - 个人签署印章控件；
    # 表单域的控件不能作为印章和签名控件
    component.ComponentType = "SIGN_SIGNATURE"
    # 参数控件所在页码，从1开始
    component.ComponentPage = 1
    # 印章ID，传参DEFAULT_COMPANY_SEAL表示使用默认印章。
    # 控件填入内容，印章控件里面，如果是手写签名内容为PNG图片格式的base64编码。
    component.ComponentValue = ""
    
    FlowApproverInfo.SignComponents = [component]
    FlowApproverInfos.append(flowApproverInfo)

    resp = channelCreateFlowByFiles(Agent, FlowApproverInfos, FlowName, FileId)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models
from tencentcloud.essbasic.v20210526.models import FlowApproverInfo, Component

from common.CreateFlowUtils import initClient, fillAgent


def channelCreateFlowByFiles(agent, flow_approver_infos, flow_name, file_id):
    """
     *  用来通过上传后的pdf资源编号来创建待签署的合同流程。
     *  适用场景1：适用非制式的合同文件签署。一般开发者自己有完整的签署文件，可以通过该接口传入完整的PDF文件及流程信息生成待签署的合同流程。
     *  适用场景2：可通过改接口传入制式合同文件，同时在指定位置添加签署控件。可以起到接口创建临时模板的效果。如果是标准的制式文件，建议使用模板功能生成模板ID进行合同流程的生成。
     *  注意事项：该接口需要依赖“多文件上传”接口生成pdf资源编号（FileIds）进行使用。
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ChannelCreateFlowByFilesRequest()

        req.FlowName = flow_name
        req.FileIds = [file_id]
        req.Agent = agent
        req.FlowApprovers = flow_approver_infos

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
    # 签署人类型，PERSON - 个人；
    # ORGANIZATION - 企业；
    # ENTERPRISESERVER - 企业静默签;
    # 注：ENTERPRISESERVER
    # 类型仅用于使用文件创建流程（ChannelCreateFlowByFiles）接口；并且仅能指定发起方企业签署方为静默签署；
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

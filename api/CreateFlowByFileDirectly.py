# 通过文件base64直接发起签署流程，返回flowid
from tencentcloud.essbasic.v20210526.models import UploadFile

from api.ChannelCreateFlowByFiles import channelCreateFlowByFiles
from api.CreateSignUrls import createSignUrls
from api.DescribeResourceUrlsByFlows import describeResourceUrlsByFlows
from api.UploadFiles import uploadFiles
from common.CreateFlowUtils import fillAgent


def createFlowByFileDirectly(fileBase64, FlowApproverInfos, FlowName):
    """
    通过文件base64直接发起签署流程，返回flowId
    """
    flowIdAndUrl = {}
    Agent = fillAgent()
    # 设置uploadFile参数, 这里可以修改传入数量
    FileInfo = UploadFile()
    FileInfo.FileBody = fileBase64

    FileInfos = [FileInfo]
    uploadFilesResponse = uploadFiles(Agent, FileInfos)

    FileId = uploadFilesResponse.FileIds[0]

    # 创建签署流程
    createFlowByFilesResponse = channelCreateFlowByFiles(Agent, FlowApproverInfos, FlowName, FileId)

    FlowId = createFlowByFilesResponse.FlowId
    FlowIds = [FlowId]
    # 获取签署链接
    createSignUrlsResponse = createSignUrls(Agent, FlowIds)
    Url = createSignUrlsResponse.SignUrlInfos[0].SignUrl
    flowIdAndUrl["FlowId"] = FlowId
    flowIdAndUrl["Url"] = Url

    # 获取下载链接
    describeResourceUrlsByFlowsResponse = describeResourceUrlsByFlows(Agent, FlowIds)
    downloadUrl = describeResourceUrlsByFlowsResponse.FlowResourceUrlInfos[0].ResourceUrlInfos[0].Url
    flowIdAndUrl["downloadUrl"] = downloadUrl

    return flowIdAndUrl

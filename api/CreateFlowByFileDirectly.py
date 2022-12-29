# 通过文件base64直接发起签署流程，返回flowid
from tencentcloud.essbasic.v20210526.models import UploadFile

from api.ChannelCreateFlowByFiles import channelCreateFlowByFiles
from api.CreateSignUrls import createSignUrls
from api.DescribeResourceUrlsByFlows import describeResourceUrlsByFlows
from api.UploadFiles import uploadFiles
from common.CreateFlowUtils import fillAgent


def createFlowByFileDirectly(file_base64, flow_approver_infos, flow_name):
    """
    CreateFlowByFileDirectly 通过文件base64直接发起签署流程，返回flowId和签署链接
    本接口是对于发起合同几个接口的封装，详细参数需要根据自身业务进行调整
    UploadFiles--ChannelCreateFlowByFiles--CreateSignUrls
    """
    flow_id_and_url = {}
    agent = fillAgent()
    # 设置uploadFile参数, 这里可以修改传入数量
    file_info = UploadFile()
    file_info.FileBody = file_base64

    file_infos = [file_info]
    upload_files_response = uploadFiles(agent, file_infos)

    file_id = upload_files_response.FileIds[0]

    # 创建签署流程
    create_flow_by_files_response = channelCreateFlowByFiles(agent, flow_approver_infos, flow_name, file_id)

    flow_id = create_flow_by_files_response.FlowId
    flow_ids = [flow_id]
    # 获取签署链接
    create_sign_urls_response = createSignUrls(agent, flow_ids)
    url = create_sign_urls_response.SignUrlInfos[0].SignUrl
    flow_id_and_url["FlowId"] = flow_id
    flow_id_and_url["Url"] = url

    # 获取下载链接
    describe_resource_urls_by_flows_response = describeResourceUrlsByFlows(agent, flow_ids)
    download_url = describe_resource_urls_by_flows_response.FlowResourceUrlInfos[0].ResourceUrlInfos[0].Url
    flow_id_and_url["downloadUrl"] = download_url

    return flow_id_and_url

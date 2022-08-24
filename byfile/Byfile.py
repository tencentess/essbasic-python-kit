import base64

from tencentcloud.essbasic.v20210526.models import FlowApproverInfo, Component


def BuildApprovers():
    # 个人签署方参数
    personName = "***"
    personMobile = "**********"

    # 企业签署方参数
    organizationName = "***"
    organizationOpenId = "**********"
    openId = "**********"

    # 用列表存储(此处根据自己签署的类型选择对应的传入参数，如单c就只传入一次个人签署方，BtoC就传入一个个人签署方，一个企业签署方)
    flowApproverInfoList = []

    # 传入个人签署方
    flowApproverInfoList.append(BuildPersonApprover(personName, personMobile))
    # 传入企业签署方
    # flowApproverInfoList.append(BuildOrganizationApprover(organizationName, organizationOpenId, openId))
    # 传入企业静默签署
    # flowApproverInfoList.append(BuildServerSignApprover())

    return flowApproverInfoList


# 打包个人签署方信息
def BuildPersonApprover(personName, personMobile):
    # 签署方参与信息
    flowApproverInfo = FlowApproverInfo()

    # 操作人的名字
    flowApproverInfo.Name = personName
    # 操作人的手机号
    flowApproverInfo.Mobile = personMobile
    # 签署人类型，PERSON - 个人；
    # ORGANIZATION - 企业；
    # ENTERPRISESERVER - 企业静默签;
    # 注：ENTERPRISESERVER
    # 类型仅用于使用文件创建流程（ChannelCreateFlowByFiles）接口；并且仅能指定发起方企业签署方为静默签署；
    flowApproverInfo.ApproverType = "PERSON"
    #  模板控件信息
    #  签署人对应的签署控件
    component = BuildComponent(146.15625, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flowApproverInfo.SignComponents = [component]
    return flowApproverInfo


# 打包企业签署方参与者信息
def BuildOrganizationApprover(organizationName, organizationOpenId, openId):
    # 签署方参与信息
    flowApproverInfo = FlowApproverInfo()

    flowApproverInfo.OrganizationName = organizationName
    flowApproverInfo.OrganizationOpenId = organizationOpenId
    flowApproverInfo.OpenId = openId
    # 签署人类型，PERSON - 个人；
    # ORGANIZATION - 企业；
    # ENTERPRISESERVER - 企业静默签;
    # 注：ENTERPRISESERVER
    # 类型仅用于使用文件创建流程（ChannelCreateFlowByFiles）接口；并且仅能指定发起方企业签署方为静默签署；
    flowApproverInfo.ApproverType = "ORGANIZATION"
    #  模板控件信息
    #  签署人对应的签署控件
    component = BuildComponent(146.15625, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flowApproverInfo.SignComponents = [component]

    return flowApproverInfo


# 打包企业静默签署方参与者信息
def BuildServerSignApprover():
    flowApproverInfo = FlowApproverInfo()

    # 签署人类型，PERSON - 个人；
    # ORGANIZATION - 企业；
    # ENTERPRISESERVER - 企业静默签;
    # 注：ENTERPRISESERVER
    # 类型仅用于使用文件创建流程（ChannelCreateFlowByFiles）接口；并且仅能指定发起方企业签署方为静默签署；
    flowApproverInfo.ApproverType = "ENTERPRISESERVER"
    #  模板控件信息
    #  签署人对应的签署控件
    component = BuildComponent(146.15625, 472.78125, 112, 40, 0, "SIGN_SIGNATURE", 1, "")
    flowApproverInfo.SignComponents = [component]

    return flowApproverInfo


def BuildComponent(componentPosX, componentPosY, componentWidth, componentHeight, fileIndex, componentType,
                   componentPage, componentValue):
    component = Component()
    # 参数控件X位置，单位px
    component.ComponentPosX = componentPosX
    # 参数控件Y位置，单位px
    component.ComponentPosY = componentPosY
    # 参数控件宽度，默认100，单位px，表单域和关键字转换控件不用填
    component.ComponentWidth = componentWidth
    # 参数控件高度，默认100，单位px，表单域和关键字转换控件不用填
    component.ComponentHeight = componentHeight
    # 控件所属文件的序号(文档中文件的排列序号，从0开始)
    component.FileIndex = fileIndex
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
    component.ComponentType = componentType
    # 参数控件所在页码，从1开始
    component.ComponentPage = componentPage
    # 印章ID，传参DEFAULT_COMPANY_SEAL表示使用默认印章。
    # 控件填入内容，印章控件里面，如果是手写签名内容为PNG图片格式的base64编码。
    component.ComponentValue = componentValue

    return component


# 将文件处理为Base64编码后的文件内容
def convertImageFileToBase64(filePath):
    with open(filePath, 'rb') as f:
        a = base64.b64encode(f.read())
    return str(a, encoding='utf-8')

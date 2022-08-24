"""
    基础配置，调用API之前必须填充的参数
"""

# 腾讯云ak/sk (secretId/secretKey) 调用API的密钥对，通过腾讯云后台CAM控制台获取
SecretId = "****************"
SecretKey = "****************"
# AppId
AppId = "****************"

# 腾讯电子签颁发给渠道侧合作企业的应用ID
ProxyAppId = "****************"

# 渠道/平台合作企业的企业ID
ProxyOrganizationOpenId = "****************"

# 渠道/平台合作企业经办人（操作员）ID
ProxyOperatorOpenId = "****************"

# 企业方静默签用的印章Id，电子签控制台获取
ServerSignSealId = "****************"

# API域名，现网使用 ess.tencentcloudapi.com
EndPoint = "essbasic.test.ess.tencent.cn"

# 文件服务域名，现网使用 file.ess.tencent.cn
FileServiceEndPoint = "file.test.ess.tencent.cn"

# 模板ID
TemplateId = "****************"

# 模板批量发起时数量设置（默认为1，可修改）
COUNT = 1

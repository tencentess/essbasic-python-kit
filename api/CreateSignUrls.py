from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.essbasic.v20210526 import models

from common.CreateFlowUtils import initClient, fillAgent

'''
跳转小程序的几种方式：主要是设置不同的EndPoint

通过链接Url直接跳转到小程序，不需要返回
设置EndPoint为WEIXINAPP，得到链接打开即可。（与短信提醒用户签署形式一样）。
通过链接Url打开H5引导页-->点击跳转到小程序-->签署完退出小程序-->回到H5引导页-->跳转到指定JumpUrl
设置EndPoint为CHANNEL，指定JumpUrl，得到链接打开即可。
客户App直接跳转到小程序-->小程序签署完成-->返回App
跳转到小程序的实现，参考官方文档（分为全屏、半屏两种方式）
全屏方式：
（https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html）
半屏方式：
（https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html）
其中小程序的原始Id，请联系<对接技术人员>获取，或者查看小程序信息自助获取。
使用CreateSignUrls，设置EndPoint为APP，得到path。
客户小程序直接跳到电子签小程序-->签署完成退出电子签小程序-->回到客户小程序
实现方式同App跳小程序。
'''
def createSignUrls(agent, flow_ids):
    """
        创建跳转小程序查看或签署的链接；自动签署的签署方不创建签署链接；
        详细参考 https://cloud.tencent.com/document/api/1420/61522
    """
    try:
        # 实例化一个client
        client = initClient()

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.CreateSignUrlsRequest()

        # 渠道应用相关信息
        # 此接口Agent.ProxyOrganizationOpenId、Agent. ProxyOperator.OpenId、Agent.AppId 和 Agent.ProxyAppId 均必填。
        req.Agent = agent
        # 签署流程编号数组，最多支持100个
        req.FlowIds = flow_ids

        # 返回的resp是一个CreateSignUrlsResponse的实例，与请求对象对应
        return client.CreateSignUrls(req)
    except TencentCloudSDKException as err:
        print(err)


'''
    测试
'''
if __name__ == '__main__':
    # 渠道应用相关信息
    Agent = fillAgent()
    # 发起合同成功的签署流程Id
    FlowIds = ["****************"]
    resp = createSignUrls(Agent, FlowIds)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

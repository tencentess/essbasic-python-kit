# 腾讯电子签渠道版API接入工具包

## 项目说明
项目通过pip引入了腾讯云sdk，补充了调用电子签渠道版API所需要的内容，并提供了调用的样例。使用前请先在项目中导入腾讯云sdk。

```
pip install --upgrade tencentcloud-sdk-python
```


## 通过 pip 安装腾讯云sdk
通过 maven 获取腾讯云sdk是使用 Python SDK 的推荐方法，pip是Python 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。关于 pip 详细可参考 pip 官网。
1. 安装pip
详见官网
[pip官网](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o)

  1.1  Windows环境
   Python 自带一个ensurepip模块，可以在 Python 环境中安装 pip。
```
# py -m ensurepip --upgrade
```

下载 Python 脚本get-pip.py，它使用一些引导逻辑来安装 pip。
[get-pip.py下载](https://bootstrap.pypa.io/get-pip.py)

打开终端/命令提示符，cd进入包含文件的 get-pip.py文件夹并运行：

```
 # py get-pip.py
```
   1.2  Linux环境
```
# python -m ensurepip --upgrade
```
下载 Python 脚本get-pip.py，它使用一些引导逻辑来安装 pip。
[get-pip.py下载](https://bootstrap.pypa.io/get-pip.py)

打开终端/命令提示符，cd进入包含文件的 get-pip.py文件夹并运行：
```
# python get-pip.py
```

在控制台输入如下命令，如果能看到 Maven 相关版本信息，则说明 Maven 已经安装成功：
```
# pip list
```

tips：请注意，如果同时有 python2 和 python3 环境， python3 环境需要使用 pip3 命令安装。

2. 使用pip导入依赖

```
# pip install --upgrade tencentcloud-sdk-python
```

## 目录文件说明
### api
api目录是对电子签渠道版所有API的简单封装，以及调用的Example（可以直接运行main函数进行测试）。
如果需要API更加高级的功能，需要结合业务修改api的封装。

注意部分参数可能与用户配置的不一致，需要调整

### byfile
byfile目录是电子签渠道版的核心场景之一：通过文件发起的快速上手样例。
**ByFileQuickStart一键使用文件发起流程：上传文件获取fileId -> 创建签署流程 -> 获取签署链接**
业务方可以结合自己的业务调整，用于正式对接。

### bytemplate
bytemplate目录是电子签渠道版的核心场景之一 ：通过模版发起的快速上手样例。
**ByTemplateQuickStart一键使用模板id发起流程:创建流程 -> 创建电子文档 -> 等待文档异步合成 -> 开启流程 -> 获取签署链接**
业务方可以结合自己的业务调整，用于正式对接。

### common
用于构造默认电子签客户端调用实例， 以及一些公共参数的组装

### config
里面定义调用电子签渠道版API需要的一些核心参数。

### testdata
blank.pdf是一个空白的pdf用于快速发起合同的测试。

## 电子签渠道版官网入口
[腾讯电子签渠道版](https://cloud.tencent.com/document/product/1420/61534)
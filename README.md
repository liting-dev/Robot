## Demo 简介
本示例使用腾讯云 Serverless 云函数实现：企业微信机器人在工作日每隔一小时提醒“起来活动一下”，并使用腾讯云自定义监控告警功能监测该服务是否正常运行。

## 教程
### 准备工作
1. 在本地安装 Serverless Framework CLI 用于部署 Demo ：

MacOS/Linux 系统
打开命令行，输入以下命令：
```
$ curl -o- -L https://slss.io/install | bash
```

Windows 系统
Windows 系统支持通过 chocolatey 进行安装。打开命令行，输入以下命令：
```
$ choco install serverless
```

详情可参考[安装教程](https://cloud.tencent.com/document/product/583/44753)

2. 下载 Demo 代码至本地

3. [注册登录腾讯云账号](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F),进入[秘钥管理](https://console.cloud.tencent.com/cam/capi)，创建秘钥对，将秘钥对复制记录。




### 一. 创建机器人
企业微信群聊右键选择【添加群机器人】，输入机器人名称，添加完成后复制 webhook 地址并记录。


### 二. 修改代码
在本地打开 Demo 代码，修改 Robot/src/index.py 里的「企业微信机器人」 webhook 为上述地址。
修改 Robot/serverless.yml 里的 secretid ,secretkey 。

### 三. 部署
在 Robot 目录下执行部署命令,即可将 demo 部署至云函数。
```
cd Robot
sls deploy
```

### 四. 查看 Demo 
进入云函数控制台的函数列表即可查看已部署的 Robot 函数。
点击函数名，进入代码编辑页，可点击【测试】触发企业微信机器人消息。

### 五. 查看自定义监控
如果你想监控云函数里的业务指标或自定义异常指标，可使用[自定义监控告警](https://cloud.tencent.com/document/product/583/41142)。
本示例上报了发送成功和失败的指标

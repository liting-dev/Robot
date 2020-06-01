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


2. [注册登录腾讯云账号](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F),进入[秘钥管理](https://console.cloud.tencent.com/cam/capi)，创建秘钥对，将秘钥对复制记录。




### 一. 创建机器人
企业微信群聊右键选择「添加群机器人」，输入机器人名称，添加完成后复制 webhook 地址并记录。
![](https://main.qcloudimg.com/raw/26675d5eb7fb9d2f9e541f6df273075a.png)

### 二. 下载并修改代码

下载代码
```
sls create --template-url https://github.com/liting-dev/Robot
```
1. 在本地打开 Demo 代码，修改 `Robot/src/index.py` 里的「企业微信机器人 webhook」为上述地址。
![](https://main.qcloudimg.com/raw/f8fb4e203bfc9b39c260aadad65b3b6d.png)

2. 修改 `Robot/serverless.yml` 里的 `secretid`,`secretkey` 。
![](https://main.qcloudimg.com/raw/38c372bee4260ed1acf5ffea5fe98d24.png)

3. 修改`Robot/.env` 里的 `TENCENT_SECRET_ID`,`TENCENT_SECRET_KEY` 。
![](https://main.qcloudimg.com/raw/f1ff08b9d1e15584fdf1437e1b1a7b8f.png)

### 三. 部署
在 Robot 目录下执行部署命令,即可将 demo 部署至云函数。
```
cd Robot
sls deploy
```

### 四. 查看 Demo 
进入[云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)的函数列表即可查看已部署的 Robot 函数。
点击函数名，进入代码编辑页，可点击「测试」触发企业微信机器人消息。
![](https://main.qcloudimg.com/raw/bc43f72e14f39be4e87ecd6a96a0f623.png)
![](https://main.qcloudimg.com/raw/4d2986f63bbf08a717dadd9f58c51d5b.png)

### 五. 查看自定义监控
如果你想监控云函数里的业务指标或自定义异常指标，可使用[自定义监控告警](https://cloud.tencent.com/document/product/583/41142)。
本示例上报了发送成功和失败的指标,可以在[自定义监控页面](https://console.cloud.tencent.com/monitor/indicator-view?date=2020-05-28&quickTime=)查看:
![](https://main.qcloudimg.com/raw/49d3a0d963faf5333b5a7eb20bd08a69.png)

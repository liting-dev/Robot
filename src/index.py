# -*- coding: utf8 -*-

import os
import json
import time
#import urllib2
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.monitor.v20180724 import monitor_client, models

try:
    from urllib import urlencode
    from urllib2 import Request, urlopen
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen

#自定义监控初始化函数，指定region和secrecId、secretKey
def initMonitor(secretId,secretKey):
    try:
        # 获取region地区，这里填写云函数所在的地域
        region = "ap-guangzhou"

        cred = credential.Credential(secretId,secretKey )

        client = monitor_client.MonitorClient(cred, region)
    except TencentCloudSDKException as err:
        print(err)
    return client

#自定义监控上报函数，传入函数名称，指标名称，指标值
def putData(client,instanceName,MetricName,Value):
    req = models.PutMonitorDataRequest() 
    req.AnnounceInstance = instanceName
    req.AnnounceTimestamp = int(time.time())
    req.Metrics = [
      {"MetricName": MetricName,"Value": Value}
    ]
    resp = client.PutMonitorData(req)
    return resp.to_json_string()


def main_handler(event, context):
    
    url = '企业微信机器人 webhook'
    data = {
        "msgtype": "text",
        "text": {
            "content": "起来活动一下"
        }
    }
    data = json.dumps(data).encode("utf-8")
    secretid = os.environ.get("secretid")
    secretkey = os.environ.get("secretkey")
    
    client = initMonitor(secretid, secretkey)

    try:
        req_attr = Request(url, data)
    except Exception as e:
         #上报数据时，指标名称填写namespace和函数名称，中间用"|"分割
        print(putData(client,"default|Robot","fail_count",1))
        print('error:',e)
    finally:
        resp_attr = urlopen(req_attr)
        print(putData(client,"default|Robot","suc_count",1))

    return resp_attr.read().decode("utf-8")

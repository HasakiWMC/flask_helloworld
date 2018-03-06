import json
from meisheng.rcscloudapi import RCSCLOUDAPI #引入江苏美圣短信接口类
#获取帐号信息

result=RCSCLOUDAPI.getAccount()
print(result)

'''
发送模板短信
'''
result=RCSCLOUDAPI.sendTplSms("4bf832a5a60b4e2fbd1fde258c73dcdf","18013550018", "@1@=1122")
print(result)

'''
输出接口返回值
'''
# api_json=json.loads(result)
# print (api_json)
#print (api_json["code"])
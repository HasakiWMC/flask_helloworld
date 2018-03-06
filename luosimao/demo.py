#!usr/bin/env python  
# -*- coding:utf-8 _*-  
# -*- coding: utf-8 -*-
import requests
import json


def send_messag_example():
    resp = requests.post("http://sms-api.luosimao.com/v1/send.json",
                         auth=("api", "key-d5317619803c8444a1be32e907edaf83"),
                         data={
                             "mobile": "18013550018",
                             "message": "hello,wolrd【铁壳测试】"
                         }, timeout=3, verify=False)
    result = json.loads(resp.content)
    print(result)


if __name__ == "__main__":
    send_messag_example()

# -*- coding:utf-8 -*-
from elasticsearch import Elasticsearch
import time
"""
    Python操作Elasticsearch
    连接操作(判断是否连接成功)
"""

# try:
#     es =Elasticsearch(['http://192.168.84.150:9201'], vertify_certs=True)
#     if not es.ping():
#         raise ValueError("Connection failed")
# except ValueError:
#     print("123")

es =Elasticsearch(['http://192.168.84.30:9201'], vertify_certs=True)
time.sleep(5)

try:
    if not es.ping():
        raise ValueError("Connection failed")
    else:
        print("Connection Successful")
except ValueError as Err:
    print(Err)

# def connectES():
#     while(1):
#         try:
#             if es.ping():
#                 print("Connect Successful...")
#                 break
#             else:
#                 print("Connecting...")
#         except Exception as Err:
#             print("...")
# connectES()
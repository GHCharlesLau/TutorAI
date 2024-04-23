# -*- coding: utf-8 -*-
# @Created_at: 2024/4/23 23:38
# @Author: Charles
# @Site: 
# @File: client.py.py
# @Software: PyCharm 
# @Comment:

import requests

data = {"inputText": "I like apples and don't like mangoes."}
data2 = {"inputText": "what kind of fruit do I like eating?"}
r = requests.post("http://127.0.0.1:5000/api/sparkBlueCat", json=data2)  # POST方法传入json参数
print(r.headers)
print(r.text)


from datetime import datetime
from flask import Flask, render_template, request, Response, jsonify
from wxcloudrun.thirdPartyApi.SparkBlueCat import text, getText, checklen
from wxcloudrun.thirdPartyApi.SparkBlueCat import appid, api_key, api_secret, Spark_url, domain
from wxcloudrun.thirdPartyApi import SparkApi
import json

# 应用初始化：创建Flask实例
app = Flask(__name__)

#　定义路由函数，访问相关地址可获得相应内容
@app.route('/api/sparkBlueCat', methods=['POST'])
def sparkBlueCat():
    # 此函数应能够处理客户端发来的json数据
    # inputText = input("\n" + "Charles: ")
    inputText = request.json['inputText']  # 获取post请求的json数据中的文本
    question = checklen(getText("user", inputText))
    SparkApi.answer = ""  # 清空历史回答，但似乎对全局answer不起作用
    # print("BlueCat: ", end="")  # 可不用,只是为了加名称，连接下行代码的打印输出
    SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
    answer = SparkApi.answer  # 捕获模型输出
    result = {"answer": answer}
    getText("assistant", SparkApi.answer)  # 加载BlueCat的历史会话
    # return Response(json.dumps(content),  mimetype='application/json')  # 写法一：使用json包和Response函数
    return jsonify(result)  # 写法二：使用flask自带jsonify工具函数


if __name__ == '__main__':
    app.run(port=5000, debug=True)

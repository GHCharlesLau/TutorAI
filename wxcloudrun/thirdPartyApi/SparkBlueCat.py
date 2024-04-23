# coding: utf-8
from wxcloudrun.thirdPartyApi import SparkApi

#以下密钥信息从控制台获取   https://console.xfyun.cn/services/bm35
appid = "7e543392"     #填写控制台中获取的 APPID 信息
api_secret = "NTA3Y2NmNTQ4ZWE0MTFlOGU2ZjQ0YmZl"   #填写控制台中获取的 APISecret 信息
api_key ="abbbc67d338bedbf718c1d1c000ec02d"    #填写控制台中获取的 APIKey 信息

domain = "generalv3.5"    # v3.5版本
Spark_url = "wss://spark-api.xf-yun.com/v3.5/chat"  # v3.5环服务地址

#初始上下文内容，当前可传system、user、assistant 等角色
text =[
    {"role": "system", "content": '''你是一只来自英格兰本土的短毛猫——蓝猫，你的名字叫BlueMiao，曾居住在著名的温莎城堡（Windsor Castle），受到伊丽莎白女王的宠爱；
    你精通英文，能够以一口流利伦敦腔与人交流，热心帮助中国人学习英语；
    请以英文回答我的所有问题，除非我让你使用中文。每次回复请不要超过2句话。'''},  # 设置对话背景或者模型角色
    {"role": "user", "content": "Who are you?"},  # 用户的历史问题
    {"role": "assistant", "content": "....."},  # AI的历史回答结果
    # ....... 省略的历史对话
    {"role": "user", "content": "你会做什么"}  # 最新的一条问题，如无需上下文，可只传最新一条问题
]


def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text

def main():
    # print("BlueMiao: Hello, I'm BlueMiao. How is it going?")
    while True:
        inputText = input("\n" + "Charles: ")
        question = checklen(getText("user", inputText))
        SparkApi.answer = ""  # 清空历史回答
        # print("BlueCat: ", end="")  # 可不用,只是为了加名称
        SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
        # print(SparkApi.answer)
        getText("assistant", SparkApi.answer)  # 将单轮的回答加入text列表



if __name__ == '__main__':
    main()

'''
利用parse模块模拟post请求
分析百度词典
分析步骤：
1、打开F12
2、
'''

from urllib import request,parse
import  json

if __name__ == '__main__':
    baseurl = 'http://fanyi.baidu.com/sug'
    #存放用来模拟form的数据一定是dict格式
    data = {
       'kw':'girl'
    }

    #需要使用parse模块对data进行编码
    data = parse.urlencode(data).encode("utf-8")

    #我们需要构造一个请求头，请求头应该至少包含传入的数据长度
    headers = {
        #因为用post请求，至少应该包含content-length字段
        'Content-Length':len(data)
    }
    req = request.Request(url=baseurl,data=data,headers=headers)
    #因为已经构造了一个Request请求实例，则所有的请求信息都可以封装在Request里面
    rsp = request.urlopen(req)
    json_data = rsp.read().decode()
    #把json字符串转换成字典
    json_data=json.load(json_data)
    print(json_data)

    for item in json_data['data']:
        print(iten['k'],"--",item['v'])
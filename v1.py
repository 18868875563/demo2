'''
使用urllib.request请求一个网页，并且打印出来
'''
from  urllib import request

if __name__ == '__main__':
    url ='http://www.baidu.com'
    #打开相应的url并把相应页面作为返回
    rsp = request.urlopen(url)
    #把返回结果读取出来，读取出来的类型为bytes
    html = rsp.read()
    #如果想把bytes内容转化成字符串，需要解码
    html = html.decode("utf-8")
    print(html)

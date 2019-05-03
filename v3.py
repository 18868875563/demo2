import  chardet
import urllib
from  urllib import request

if __name__ == '__main__':
    url ='http://www.baidu.com'
    #打开相应的url并把相应页面作为返回
    rsp = request.urlopen(url)
    #把返回结果读取出来，读取出来的类型为bytes
    html = rsp.read()
    #print(html)
    print (rsp.info())
    print (rsp.geturl())
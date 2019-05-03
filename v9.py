'''
访问一个网址
更改自己的UserAgent进行伪装
'''
from urllib import  request,error
if __name__ == '__main__':
    url =  'http://wwww.baidu.com'
    try:
        #headers = {}
        #headers['User-Agent']=''
        #req = request.Request(url,headers=headers)
        req = request.Request(url)
        req.add_header("key","value")
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print("HTTPError:{0}".format(e.reason))
        print("HTTPError:{0}".format(e))
    except error.URLError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))
    except Exception as e:
        print(e)
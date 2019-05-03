'''
使用代理访问百度网站
'''
from urllib import  request,error

if __name__ == '__main__':
    url = 'http://www,baidu.com'

    #设置代理地址
    proxy = {'http':'120.194.18.90:81'}
    #创建proxy_hanlder
    proxy_handler = request.ProxyHandler(proxy)
    #创建opener
    opener = request.build_opener(proxy_handler)
    #安装opener
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
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
'''
URLError的使用
'''

from urllib import request,error
if __name__ == '__main__':
     url = 'http://www.baiduuuuuuuuuuu.com'
     try:
         req = request.Request(url)
         rsp = request.urlopen(req)
         html = rsp.read().decode()
         print(html)
     except error.URLError as e:
        print("URLError:{o}".format(e.reason))
        print("URLError:{o}".format(e))
     except Exception as e:
        print(e)
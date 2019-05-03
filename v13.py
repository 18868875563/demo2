from urllib import  request,parse
from  http import  cookiejar

#创建cookiejar的实例
cookie = cookiejar.CookieJar()
#创建cookiejar的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handler = request.HTTPHandler()
#创建https请求管理器
https_handler = request.HTTPSHandler()
#创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''
    url = "http://www.renren.com/PLogin.do"
    data = {
        "email":"13119144223",
        "password":"123456"
    }
    #把数据进行编码
    data = parse.urlencode(data)
    #创建一个请求对象
    req = request.Request(url,data=data.encode())
    #使用opener发起请求
    rsp = opener.open(req)
def getHomePage():
    url = "http://www.renren.com/965187997/profile"
    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("rsp.html", "w") as f:
        f.write(html)
if __name__

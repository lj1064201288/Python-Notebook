from urllib import request, parse

'''
掌握url进行参数编码的方法
需要使用parse
'''
if __name__ == '__main__':

    url = "https://baidu.com/s?"
    wd = input('Input your keyword:')

    # 想要使用的data,需要用字典结构
    qs = {
        "wd": wd
    }

    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Host':'baidu.com'
    }

    # 转换url编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    rep = request.Request(url=fullurl,headers=header, method='POST')

    # 如果直接用可读的带参数的url, 是不能访问的

    rsp = request.urlopen(rep)

    html = rsp.read()

    # 使用get取值保证不会出错
    html = html.decode()

    print(html)
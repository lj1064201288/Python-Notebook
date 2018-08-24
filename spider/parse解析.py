from urllib import parse, request

'''
掌握对urllib进行参数编码的方法
需要使用parse模块
'''
if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'
    wd = input("请输入你要搜索的内容:")


    # 要使用data 需要字典结构组成

    qs = {
        'wd':wd
    }

    headers = {
        'User-Augent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Host':'baidu.com'
    }


    # 转化为url格式进行编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)
    fullurl = request.Request(url=fullurl,headers=headers,method='GET')


    # 如果直接用刻度的带参数的url, 是无法访问的

    rsp = request.urlopen(fullurl)
    rsp = rsp.read()

    # 使用get取值保证不会出错
    html = rsp.decode()

    print(html)

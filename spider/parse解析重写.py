from urllib import request, parse

if __name__ == '__main__':

    url = "https://s.taobao.com/search?"
    q = input("请输入你要搜索的商品:")

    qs = {
        'q': q
    }

    headers = {
        'User-Augent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Host':'taobao.com'
    }

    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    rsp = request.Request(url=fullurl, headers=headers, method='POST')

    rsp = request.urlopen(fullurl)
    rsp = rsp.read()

    html = rsp.decode()
    print(html)
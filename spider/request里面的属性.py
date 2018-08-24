import urllib

if __name__ == '__main__':
    url = 'https://www.58.com'

    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL:{0}".format(rsp.geturl()))
    print("Into:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))

    html = rsp.read()

    # 使用get取值保证不会出错
    html.decode()
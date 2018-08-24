from urllib import request
import chardet

if __name__ == '__main__':

    url = 'http://www.baidu.com'

    rsp = request.urlopen(url)


    print(type(rsp))
    print(rsp)

    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))

    rsp = rsp.read()

    cs = chardet.detect(rsp)


    html = rsp.decode(cs.get('encoding','utf-8'))
    print(html)



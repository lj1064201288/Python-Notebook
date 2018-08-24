import chardet
import urllib
'''
利用request下载页面
自动检测页面的编码
'''
if __name__ == '__main__':
    url = 'https://baidu.com'

    rsp = urllib.request.urlopen(url)
    rsp = rsp.read()

    #利用chardet自动检测
    cs = chardet.detect(rsp)
    print(type(cs))
    print(cs)


    #使用get取值保证不会出错
    response = rsp.decode(cs.get('encoding', 'utf-8'))
    print(response)
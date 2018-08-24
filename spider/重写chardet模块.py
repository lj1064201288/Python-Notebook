import chardet
import urllib

'''
利用request下载页面编码
'''

if __name__ == '__main__':

    url = 'https://www.taobao.com'

    rsp = urllib.request.urlopen(url)
    rsp = rsp.read()

    #'使用chardet自动检测'
    cs = chardet.detect(rsp)
    print(type(cs))
    print(cs)

    #'使用get访问避免错误'
    html = rsp.decode(cs.get('encoding','utf-8'))
    print(html)
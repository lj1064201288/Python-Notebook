import urllib
import chardet

if __name__ == '__main__':
    url = 'http://www.baidu.com/'

    rsp = urllib.request.urlopen(url)

    html = rsp.read()

    cs = chardet.detect(html)
    print(type(cs))

    print(cs)

    html = html.decode(cs.get("encoding", "utf-8"))

    print(html)
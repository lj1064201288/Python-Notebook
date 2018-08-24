import urllib

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    http = urllib.request.urlopen(url)
    http = http.read()
    
    rsp = http.decode()
    print(rsp)
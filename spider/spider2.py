from urllib import request

if __name__ == '__main__':
    url = "https://www.taobao.com"

    rep = request.Request(url)
    rep = rep.add_header("User-Agent", "36Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.")

    res = request.urlopen( rep )
    res = res.read()

    http = res.decode("utf-8")

    print(http)
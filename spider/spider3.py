from urllib import error, request

if __name__ == '__main__':

    url = "https://www.taobao.com/"

    try:
        req = request.Request(url)
        req.add_header("User_Agent", "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19")

        rsp = request.urlopen(req)
        rsp = rsp.read()


        rpe = rsp.decode()

        print(rpe)
    except Exception as e:
        print(e)
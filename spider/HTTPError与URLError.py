'''
URLError的使用
'''
from urllib import request,error

if __name__ == '__main__':

    url = "http://www.assd.asr.asawqq.cn/wwda"

    try:

        rep = request.Request(url)
        rsp = request.urlopen(rep)
        http = rep.read().decode()
        print(http)

    except error.HTTPError as e:
        print('HTTPError:{0}'.format(e.reason))
        print("HTTPError:{0}".format(e))

    except error.URLError as e:
        print('URLError:{0}'.format(e.reason))
        print("URLError:{0}".format(e))

    except Exception as e:
        print(e)
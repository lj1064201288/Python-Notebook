from urllib import parse, request
import json

if __name__ == '__main__':

    baseurl = "http://fanyi.baidu.com/sug"

    data = {
        'kw':'girl'
    }

    data = parse.urlencode(data).encode('utf-8')
    print(type(data))

    headers = {
        'Content-Length':len(data)
    }

    rsp = request.urlopen(baseurl, data=data)

    json_data = rsp.read().decode()
    print(type(json_data))
    print(json_data)

    json_data = json.loads(json_data)
    print(type(json_data))
    print(json_data)

    for item in json_data['data']:
        print(item['k'], "----", item['v'])


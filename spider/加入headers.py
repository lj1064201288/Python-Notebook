from urllib import parse, request
import json


if __name__ == '__main__':

    baseurl = 'http://fanyi.baidu.com/sug'

    data = {
        'kw':'girl'
    }

    data = parse.urlencode(data).encode('utf-8')
    print(type(data))

    headers = {
        'Content-Length':len(data)
    }

    json_data = request.Request(baseurl, data=data, headers=headers)
    print(type(json_data))
    print(json_data)

    json_data = request.urlopen(json_data).read().decode()
    print(json_data)
    print(type(json_data))

    json_data = json.loads(json_data)
    print(type(json_data))
    print(json_data)

    for item in json_data['data']:
        print(item['k'], "----", item['v'])



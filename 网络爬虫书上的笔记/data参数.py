from urllib import request, parse

data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf-8')
response = request.urlopen('https://python.org',data=data)
print(response.read())
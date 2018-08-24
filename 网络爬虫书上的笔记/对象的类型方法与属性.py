from urllib import request


response = request.urlopen('https://www.python.org')

print(response.status)
print(response.getheaders())
# print(response.getheaders('Server'))
# print(response.read())
# prin t(response.readinto())
# print(response.closed) print(response.fileno())
# print(response.msg)
# print(response.version)
# print(response.reatus)
# print(response.reason)
# print(response.debuglebel)



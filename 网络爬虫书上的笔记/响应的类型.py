from urllib import request

reponse = request.urlopen('https://www.python.org')
print(type(reponse))